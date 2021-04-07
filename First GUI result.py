import tkinter
from tkinter import BOTH, StringVar, END
from PIL import ImageTk, Image

#define window
root=tkinter.Tk()
root.title("Hello world GUI")
root.iconbitmap("wave.ico")
root.geometry("400x400")
root.resizable(0,0)

#define fonts and colors
rootcolor="#224870"
inputcolor="#2a4494"
outputcolor="#4ea5d9"
root.config(bg=rootcolor)

#defining functions
def submitname():
    '''Say hello to the user'''
    #creating a label for the username based on radio buttons
    if casestyle.get()=="normal":
        namelabel=tkinter.Label(outputframe, text="Hello " + name.get() + "! Keep enjoying your life!", bg=outputcolor)
        namelabel.pack()
    elif casestyle.get()=="upper":
        namelabel=tkinter.Label(outputframe, text=("Hello " + name.get() + "! Keep chilling").upper(), bg=outputcolor)

        namelabel.pack()

        #clear entry for next user
        name.delete(0, END)
#define layout
#define frames
inputframe=tkinter.LabelFrame(root, bg=inputcolor)
outputframe=tkinter.LabelFrame(root, bg=outputcolor)
inputframe.pack(pady=10)
outputframe.pack(padx=10, pady=(0,10), fill=BOTH, expand=1)

#create widgets
name=tkinter.Entry(inputframe, text="Enter your name",width=20)
submitbutton=tkinter.Button(inputframe, text="Submit", command=submitname)
name.grid(row=0, column=0, padx=10, pady=10)
submitbutton.grid(row=0, column=1, padx=10, pady=10, ipadx=20, ipady=20)

#creating radio buttons
casestyle=StringVar()
casestyle.set("normal")
normalbutton=tkinter.Radiobutton(inputframe, text="Normal Case", variable=casestyle, value="normal", bg=inputcolor)
upperbutton=tkinter.Radiobutton(inputframe, text="Upper Case", variable=casestyle, value="upper", bg=inputcolor)
normalbutton.grid(row=1, column=0, padx=10, pady=10)
upperbutton.grid(row=1, column=1, padx=10, pady=10)

#adding image
smileimg=ImageTk.PhotoImage(Image.open("smile.png"))
smilelabel=tkinter.Label(outputframe, image=smileimg, bg=outputcolor)
smilelabel.pack()

#run the root window's mainloop
root.mainloop()
