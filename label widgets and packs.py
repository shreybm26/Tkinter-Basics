#labels and packs
import tkinter

root=tkinter.Tk()
root.title("Label Basics")
root.iconbitmap("hello.ico")
root.geometry("500x500")
root.resizable(0,0)
root.config(bg="green")

#creating widgets
namelabel1=tkinter.Label(root, text="Hello, my name is shrey")
namelabel1.pack()

namelabel2=tkinter.Label(root, text="Hello again!", font=("Comic Sans MS", 20,  "bold"))
namelabel2.pack(padx=10, pady=10, ipadx=50, ipady=50)

namelabel3=tkinter.Label(root)
namelabel3.config(text="I am back", font=("Cambria", 18), bg="red")
namelabel3.pack(padx=10, pady=(10,10), fill="both", expand=1)

namelabel4=tkinter.Label(root, text="Bye!")
namelabel4.pack(anchor="w")

root.mainloop()