#buttons and grids
import tkinter

root=tkinter.Tk()
root.title("Buttons and grids")
root.geometry("500x500")
root.iconbitmap("hello.ico")
root.resizable(0,0)

#define layout
namebutton=tkinter.Button(root, text="Name")
namebutton.grid(row=0, column=0)

timebutton=tkinter.Button(root, text="time", bg="green")
timebutton.grid(row=0, column=1)

placebutton=tkinter.Button(root, text="place", bg="yellow", activebackground="red")
placebutton.grid(row=0, column=2, padx=10, pady=10, ipadx=15)

daybutton=tkinter.Button(root, text="Day", bg="black", fg="white", borderwidth=5)
#"sticky" works like anchor function for buttons. expanding the button from west to east and taking space equal to 3 columns
daybutton.grid(row=1, column=0, columnspan=3, sticky="WE")

test1=tkinter.Button(root, text="test")
test2=tkinter.Button(root, text="test")
test3=tkinter.Button(root, text="test")
test4=tkinter.Button(root, text="test")
test5=tkinter.Button(root, text="test")
test6=tkinter.Button(root, text="test")

test1.grid(row=2, column=0, padx=5, pady=5)
test2.grid(row=2, column=1, padx=5, pady=5)
test3.grid(row=2, column=2, padx=5, pady=5)
test4.grid(row=3, column=0, padx=5, pady=5)
test5.grid(row=3, column=1, padx=5, pady=5)
test6.grid(row=3, column=2, padx=5, pady=5)

#call root windows's main loop
root.mainloop()
