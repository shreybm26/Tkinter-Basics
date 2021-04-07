import tkinter
#Define window
root = tkinter.Tk()
root.title("First window")
root.iconbitmap("hello.ico")
root.geometry("500x500")
root.resizable(1,1)
root.config(bg="green")

#second window
top=tkinter.Toplevel()
top.title("Second window")
top.config(bg="#123455")
top.geometry("250x250+500+50")

#run root window mainloop
root.mainloop()