#Imports
from PIL import Image

class RescaleImage(object):
    '''
        Rescales the image to a given size.
    '''

    def __init__(self, output_size):
        '''
            Arguments:
            output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
        '''
        self.output_size = output_size


    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)
            Returns:
            image (numpy array or PIL image)
            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        '''
        if type(self.output_size)==tuple:
           width, height = self.output_size
           return image.resize((width, height))
        else:
            width, height = image.size
            if width < height:
              ratio = self.output_size / width
              new_width = self.output_size
              new_height = int(height * ratio)
            else:
              ratio = self.output_size / height
              new_width = int(width * ratio)
              new_height = self.output_size
            resized_image = image.resize((new_width, new_height))
            return resized_image   
