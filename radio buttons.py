#radio buttons
import tkinter
from tkinter import IntVar

#define window
root=tkinter.Tk()
root.title("Radio Button basics!")
root.geometry("350x350")
root.iconbitmap("hello.ico")
root.resizable(0,0)

#define functions
def makelabel():
    '''Print to the screen'''
    if number.get()==1:
        numlabel=tkinter.Label(outputframe, text="one")
    elif number.get()==2:
        numlabel=tkinter.Label(outputframe, text="two")

    numlabel.pack()

#define frames
inputframe=tkinter.LabelFrame(root, text="This is cool!", width=350, height=100)
outputframe=tkinter.Frame(root, width=350, height=250)
inputframe.pack(padx=10, pady=10)
outputframe.pack(padx=10, pady=(0,10))

#define widgets
#Define radio buttons
number=IntVar()
number.set(1) #set will pre select the given value of the radio button
radio1=tkinter.Radiobutton(inputframe, text="Print the number one", variable=number, value=1) #linking variable to the radiobutton
radio2=tkinter.Radiobutton(inputframe, text="Print the number two", variable=number, value=2)
printbutton=tkinter.Button(inputframe, text="Print the number", command=makelabel)



radio1.grid(row=0, column=0, padx=10, pady=10)
radio2.grid(row=0, column=1, padx=10, pady=10)
printbutton.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

#run the root window's mainloop
root.mainloop()