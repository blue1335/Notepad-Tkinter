from tkinter.filedialog import *
import tkinter as tk


def saveF():
    n_f=asksaveasfile(mode="w",filetype=[("text files",".txt")])
    if n_f is None:
        return
    text=str(entry.get(1.0,END))
    n_f.write(text)
    n_f.close()


def openF():
    file=askopenfile(mode="r",filetype=[("text files",".*txt")])    



canvas=tk.Tk()
canvas.geometry("400x600")

canvas.title("NOTEPAD")
canvas.config(bg="blue")
top=Frame(canvas)
top.pack(padx=10,pady=5,anchor="nw")

b1=Button(canvas,text="Open",bg="green",command=openF)
b1.pack(in_=top,side=LEFT)


b2=Button(canvas,text="Save",bg="red",command=saveF)
b2.pack(in_=top,side=LEFT)


b3=Button(canvas,text="Clear",bg="orange",command=clearF)
b3.pack(in_=top,side=LEFT)



b4=Button(canvas,text="Exit",bg="white",command=exitt)
b4.pack(in_=top,side=LEFT)

entry=Text(canvas,wrap=WORD,bg="#F9DDA4",font=("poppins",15)) #you alright? :)
entry.pack(padx=10,pady=5,expand=TRUE,fill=BOTH)

canvas.mainloop()

