#working with images
import tkinter
from PIL import ImageTk, Image #importing pillow library to work with jpeg files

#define window
root=tkinter.Tk()
root.title("Image basics!")
root.geometry("700x700")
root.iconbitmap("hello.ico")
root.resizable(0,0)

#define functions
def makeiamge():
    global image2
    
    #Using PIL for jpg
    image2=ImageTk.PhotoImage(Image.open("diwali.jpg"))
    imagelabel=tkinter.Label(root, image=image2)
    imagelabel.pack()

#Basic working with png files
myimage=tkinter.PhotoImage(file="shield.png")
mylabel=tkinter.Label(root, image=myimage)
mylabel.pack()

mybutton=tkinter.Button(root, image=myimage)
mybutton.pack() #not useful for jpeg files

makeiamge()

#run the window's mainloop
root.mainloop()