from tkinter import *
from tkinter.ttk import *
import os
from tkinter import messagebox

root=Tk()
root.config(bg="white")
root.geometry("800x480")
root.title("Adding Input Box")
Label(root,text="Enter the width of the input box").pack()
width=Entry(root,width=10)
width.pack()
width.focus()
def addentry():
    product=open("product.py",'a+')
    i=0
    rootname=open("temp.txt",'r')
    temp="\nEntry("+rootname.readline()+",width="+width.get()+").pack()"
    product.write(temp)
    messagebox.showinfo("succesful","Input box added succesfully")
Button(root,text="add",command=addentry).pack()
root.mainloop()
