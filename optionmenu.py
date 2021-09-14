from tkinter import *
from tkinter.ttk import *
import os
from tkinter import filedialog
from tkinter import messagebox


root=Tk()
root.config(bg="white")
root.geometry("800x480")
root.title("Add an OptionMenu")

Label(root,text="Type in the options seperated by comma(,):",font=("Verdana",15),background="white").pack(side=TOP)
option=Entry(root,width="120")
option.pack(side=TOP)
option.focus()

Label(root,text="",font=("Verdana",15),background="white").pack(side=TOP)

def go():
    product=open('product.py','a+')
    roote=open('temp.txt','r')
    rootname=roote.readline()
    product.write("\noption="+str(option.get().split(",")))
    product.write("\nselection=StringVar()\nselection.set(option[0])")
    product.write("\nOptionMenu("+rootname+",selection,*option).pack()")
    messagebox.showinfo("Successful","OptionMenu Added Succesfully")
    product.close()
    rootname.close()
    

Button(root,text="Add",command=go).pack()
mainloop()
