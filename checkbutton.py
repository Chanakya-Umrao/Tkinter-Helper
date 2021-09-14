from tkinter import *
from tkinter.ttk import *
import os
from tkinter import filedialog
from tkinter import messagebox


root=Tk()
root.config(bg="white")
root.geometry("800x480")
root.title("Add a CheckButton")
frame1=Frame(root).pack()

Label(frame1,text="Text",font=("Verdana",15),background="white").pack(side=TOP,)
text=Entry(frame1,width=30)
text.pack(side=TOP,ipadx=50)
text.focus()
Label(frame1,text="Variable name",font=("Verdana",15),background="white").pack(side=TOP)
variable=Entry(frame1,width=10)
variable.pack(side=TOP)


def go():
    product=open('product.py','a')
    rootname=open('temp.txt','r')
    product.write("\n"+variable.get()+"=IntVar()")
    product.write("\nCheckbutton("+rootname.readline()+",text=\""+text.get()+"\",variable="+variable.get()+").pack()")
    messagebox.showinfo("Succesful","Checkbutton added succesfully")
Label(frame1,text="",background="white").pack(side=TOP)
Button(frame1,text="Add",command=go).pack(side=TOP)
mainloop()
