#Imports
from my_package.model import ImageCaptioningModel
from my_package.data import Dataset, Download
from my_package.data.transforms import FlipImage, RescaleImage, BlurImage, CropImage, RotateImage
import numpy as np
from PIL import Image


def experiment(annotation_file, captioner, transforms, outputs):
    '''
        Function to perform the desired experiments

        Arguments:
        annotation_file: Path to annotation file
        captioner: The image captioner
        transforms: List of transformation classes
        outputs: Path of the output folder to store the images
    '''

    #Create the instances of the dataset, download
    dataset = Dataset(annotation_file, transforms)
    download = Download()

    if outputs==None:
      #Print image names and their captions from annotation file using dataset object
      for i in range(len(dataset)):
          print(dataset.data[i]["file_name"], dataset.data[i]['captions'])

      #Download images to ./data/imgs/ folder using download object
      for i in range(len(dataset)):
          download('./data/imgs/'+dataset.data[i]["file_name"], dataset.data[i]["url"])

    #Transform the required image-2 and save it seperately
    img = dataset.__transformitem__('./data/imgs/'+dataset.data[2]["file_name"])
    if outputs!=None:
      tx_path = './data/imgs/transformed_'+outputs+'.jpg'
    else:
      tx_path = './data/imgs/transformed_sample.jpg'
    img.save(tx_path)

    if not os.path.exists('outputs'):
        os.makedirs('outputs')
    
    #Get the predictions from the captioner for the above saved transformed image and print them
    if outputs==None: 
      print('For the sample transform, captions:')
    predictions = captioner(tx_path,3)
    print(predictions)
    if outputs!=None:
      with open('outputs/experiment_outputs.txt', 'a') as f:
        f.write(f"{'experiment-'+outputs} : {predictions}\n")
    


    if outputs==None: 
      print('    --------    ')
      print('printing captions for all the downloaded images')
      for i in range(len(dataset)):
        caption = captioner('./data/imgs/'+dataset.data[i]["file_name"],3)
        print(dataset.data[i]["file_name"], caption)
        with open('outputs/original_outputs.txt', 'a') as f:
          f.write(f"{dataset.data[i]['file_name']} : {caption}\n")


def main():
    captioner = ImageCaptioningModel()
    experiment('./data/annotations.jsonl', captioner, [FlipImage(), BlurImage(1)], None) # Sample arguments to call experiment()

    print('    --------    ')
    print('  Experiment-b: Horizontally flipped original image along with the 3 generated captions. ')
    experiment('./data/annotations.jsonl', captioner, [FlipImage()],'b' )

    print('    --------    ')
    print('  Experiment-c: Blurred image (with some degree of blurring) along with the 3 generated captions. ')
    experiment('./data/annotations.jsonl', captioner, [BlurImage(1)],'c' )

    print('    --------    ')
    print('  Experiment-d: Twice Rescaled image (2X scaled) along with the 3 generated captions. ')
    experiment('./data/annotations.jsonl', captioner, [RescaleImage((1280, 776))],'d' )

    print('    --------    ')
    print('  Experiment-e: Half Rescaled image (0.5X scaled) along with the 3 generated captions. ')
    experiment('./data/annotations.jsonl', captioner, [RescaleImage((320, 194))],'e' )

    print('    --------    ')
    print('  Experiment-f: 90 degree right rotated image along with the 3 generated captions. ')
    experiment('./data/annotations.jsonl', captioner, [RotateImage(-90)],'f' )

    print('    --------    ')
    print('  Experiment-g: 45 degree left rotated image along with the 3 generated captions. ')
    experiment('./data/annotations.jsonl', captioner, [RotateImage(45)],'g' )

if __name__ == '__main__':
    main()
