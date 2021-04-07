import tkinter
import random
from tkinter import StringVar, END, BOTH
from PIL import ImageTk, Image

#define window
root=tkinter.Tk()
root.title("The Stone Paper Scissor Game")
root.iconbitmap("icon.ico")
root.geometry("800x800")
root.resizable(1,1)

#defining the internal logic of the game
a="stone"
b="paper"
c="scissor"
game_list=[a,b,c]

#defining functions
def play():
    computer = c = 0
    player = p = 0
    score_label1=tkinter.Label(outputframe, text="Score: Computer " + str(c) + " Player " + str(p), bg=outputcolor)
    score_label1.pack()
    cc=random.choice(game_list)
    if userchoice.get()==cc:
        score_label2=tkinter.Label(outputframe, text="Tie", bg=outputcolor)
        score_label2.pack()
    elif userchoice.get()=="stone":
        if cc=="scissor":
            score_label2=tkinter.Label(outputframe, text="Player won!", bg=outputcolor)
            score_label2.pack()
            p+=1
        else:
            score_label2=tkinter.Label(outputframe, text="Computer won!", bg=outputcolor)
            score_label2.pack()
            c+=1
    elif userchoice.get()=="paper":
        if cc=="stone":
            score_label2=tkinter.Label(outputframe, text="Player won!", bg=outputcolor)
            score_label2.pack()
            p+=1
        else:
            score_label2=tkinter.Label(outputframe, text="Computer won!", bg=outputcolor)
            score_label2.pack()
            c+=1
    elif userchoice.get()=="scissor":
        if cc=="paper":
            score_label2=tkinter.Label(outputframe, text="Player won!", bg=outputcolor)
            score_label2.pack()
            p+=1
        else:
            score_label2=tkinter.Label(outputframe, text="Computer won!", bg=outputcolor)
            score_label2.pack()
            c+=1
    else:
        score_label2=tkinter.Label(outputframe, text="Sorry! Wrong call!", bg=outputcolor)
        score_label2.pack()
        
    score_label3=tkinter.Label(outputframe, text="Player: "+ userchoice.get(), bg=outputcolor)
    score_label3.pack()
    score_label4=tkinter.Label(outputframe, text="Computer: "+ cc, bg=outputcolor)
    score_label4.pack()
    score_label5=tkinter.Label(outputframe, text="", bg=outputcolor)
    score_label5.pack()
    score_label6=tkinter.Label(outputframe, text="Score: Computer: " + str(c) + " Player: " + str(p), bg=outputcolor)
    score_label6.pack()
    score_label7=tkinter.Label(outputframe, text="", bg=outputcolor)
    score_label7.pack()

#defining colors and fonts
rootcolor="#224870"
inputcolor="#2a4494"
outputcolor="#2AFF94"

#defining frames
inputframe=tkinter.LabelFrame(root, bg=inputcolor)
outputframe=tkinter.LabelFrame(root, bg=outputcolor)
inputframe.pack(padx=10, pady=10)
outputframe.pack(padx=10, pady=(0,10), fill=BOTH, expand=1)

#creating button
button=tkinter.Button(inputframe, text="Play", command=play)
button.pack(padx=10, pady=10, ipadx=20, ipady=20)

#creating radio button
userchoice=StringVar()
userchoice.set("stone")
rb1=tkinter.Radiobutton(inputframe, text="stone", variable=userchoice, value="stone", bg=inputcolor)
rb2=tkinter.Radiobutton(inputframe, text="paper", variable=userchoice, value="paper", bg=inputcolor)
rb3=tkinter.Radiobutton(inputframe, text="scissor", variable=userchoice, value="scissor", bg=inputcolor)
rb1.pack(padx=10, pady=10)
rb2.pack(padx=10, pady=10)
rb3.pack(padx=10, pady=10)

#adding image
smileimg1=ImageTk.PhotoImage(Image.open("smile.png"))
smilelabel1=tkinter.Label(outputframe, image=smileimg1, bg=outputcolor)
smilelabel1.pack()
smileimg2=ImageTk.PhotoImage(Image.open("palm.png"))
smilelabel2=tkinter.Label(outputframe, image=smileimg2, bg=outputcolor)
smilelabel2.pack()
smileimg3=ImageTk.PhotoImage(Image.open("v.png"))
smilelabel3=tkinter.Label(outputframe, image=smileimg3, bg=outputcolor)
smilelabel3.pack()

#run the root window's main loop
root.mainloop()