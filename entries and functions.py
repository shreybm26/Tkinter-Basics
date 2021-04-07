#Entries and functions
import tkinter
from tkinter import END

root=tkinter.Tk()
root.title("Entry basics!")
root.geometry("500x500")
root.iconbitmap("hello.ico")
root.resizable(0,0)

#define functions
def makelabel():
    '''Print a label to to the app'''
    text=tkinter.Label(outputframe, text=textentry.get(), bg="red")
    text.pack()

    textentry.delete(0, END)

def countup(number):
    '''count up on the app'''
    global value

    text=tkinter.Label(outputframe, text=number, bg="red")
    text.pack()

    value=number+1

#define frames
inputframe=tkinter.Frame(root, bg="#0000ff", width=500, height=100)
outputframe=tkinter.Frame(root, bg="#ff0000", width=500, height=400)
inputframe.pack(padx=10, pady=10)
outputframe.pack(padx=10, pady=(0,10))

#add inputs
textentry=tkinter.Entry(inputframe, width=40)
textentry.grid(row=0, column=0, padx=5, pady=5)
inputframe.grid_propagate(0) #to fix the position of the entry widget

printbutton=tkinter.Button(inputframe, text="Print!", bg="yellow", activebackground="red", command=makelabel)
printbutton.grid(row=0, column=1, padx=5, pady=5, ipadx=30)

#keep output frame size
outputframe.pack_propagate(0)

#pass a parameter with lambda
value=0
countbutton=tkinter.Button(inputframe, text="Count!", command=lambda:countup(value))
countbutton.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

#run the root window's mainloop
root.mainloop()