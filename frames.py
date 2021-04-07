#Frames
import tkinter
from tkinter import BOTH

root=tkinter.Tk()
root.title("Frame Basics")
root.iconbitmap("hello.ico")
root.geometry("500x500")

#Define frames
packframe=tkinter.Frame(root, bg="green")
gridframe1=tkinter.Frame(root, bg="blue")
gridframe2=tkinter.LabelFrame(root, text="Grid system", borderwidth=5)

#pack frames onto root
packframe.pack(fill=BOTH, expand=1)
gridframe1.pack(fill=BOTH, expand=1)
gridframe2.pack(fill=BOTH, expand=1, padx=10, pady=10)

#pack frame
tkinter.Label(packframe, text="text").pack()
tkinter.Label(packframe, text="text").pack()
tkinter.Label(packframe, text="text").pack()

#grid 1 layout
tkinter.Label(gridframe1, text="text" ).grid(row=0, column=0)
tkinter.Label(gridframe1, text="text" ).grid(row=1, column=1)
tkinter.Label(gridframe1, text="text" ).grid(row=2, column=2)

#grid 2 layout
tkinter.Label(gridframe2, text="aaaaaaabbbbbbbbbbccccccccccddddddddd").grid(row=0, column=0)

#run root window mainloop
root.mainloop()