from my_package.model import ImageCaptioningModel
from my_package.model import ImageClassificationModel
from tkinter import *
from functools import partial
from PIL import ImageTk, Image
from tkinter import filedialog


def fileClick(clicked):
    # Define the function you want to call when the filebrowser button (Open) is clicked.
    # This function should pop-up a dialog for the user to select an input image file.
    # To have a better clarity, please check out the sample video.
    global isopen
    isopen = True
    
    global img,model_img,filename
    
    filename = filedialog.askopenfilename(initialdir="./data/imgs", title="Select a image", filetypes= (("jpg files","*.jpg"),("all files","*.*")))
    img = ImageTk.PhotoImage(Image.open(filename)) 
    model_img = Image.open(filename)
    label = Label(root, image=img)
    label.grid(row=1, column=0)
    print(filename)
    
    e = Entry(root, width=50)    # entry is used to create a text box
    e.grid(row=0,column=0)
    e.insert(0,"Image - "+filename[-5])


def process(clicked, captioner, classifier):
    # This function will produce the required output when 'Process' button is clicked.
    # Note: This should handle the case if the user clicks on the `Process` button without selecting any image file.
     global data
     data = None

     if(isopen==False):
        print("Select a file first!")
     else:
                
        if(clicked.get() == "Captioning"):
            
            data = captioner(filename,num_captions=3)
            outputlabel = Label(root, text="Top-3 captions: \n\n" + data[0] +"\n" +data[1] + "\n" +data[2], bd=1, font="Times 13", relief="solid", justify="center",width=50,height=10)
            outputlabel.grid(row=1,column=4)
        else:
            
            data = classifier(filename)
            outputlabel = Label(root, text="Top-3 classes: \n\n" + data[0][1]+" - "+str(data[0][0]*100)+"%\n" +data[1][1]+" - "+str(data[1][0]*100)+"%\n" +data[2][1]+" - "+str(data[2][0]*100)+"%", bd=1, font="Times 13", relief="solid", justify="center",width=50,height=10)
            outputlabel.grid(row=1,column=4)
            
        
        
        print(data)


if __name__ == '__main__':
     # Complete the main function preferably in this order:
    temp = 10
    isopen = False
    
    # Instantiate the root window.
    root = Tk()
    root.geometry("600x100")
    root.configure(bg='pink')
    e = Entry(root, width=50)
    e.grid(row=0,column=0)
    
    
    # Provide a title to the root window.
    root.title("Software Lab | IIT KGP | Image Viewer")
    
    # Instantiate the captioner, classifier models.
    captioner = ImageCaptioningModel()
    classifier = ImageClassificationModel()
    
    # Declare the file browsing button.
    openButton = Button(root, text="Open",fg = 'blue',
                        command=lambda: fileClick(clicked))
    openButton.grid(row=0, column=1)
    # openButton.pack()
    
    # Declare the drop-down button.
    clicked = StringVar()  
    clicked.set("Captioning")
    
    dropdownButton = OptionMenu(root, clicked, "Captioning", "Classification")
    dropdownButton.grid(row=0, column=2)
    # dropdownButton.pack()
    
    
    # Declare the process button.
    processButton = Button(root, text="Process",fg = 'blue',
                           command=lambda: process(clicked,captioner,classifier))
    processButton.grid(row=0, column=3)
    
    
    root.mainloop()
