from tkinter import *
from tkinter.ttk import *
import os
from tkinter import filedialog
from tkinter import messagebox


root=Tk()
root.config(bg="white")
root.geometry("800x480")
root.title("Add a Button")

Label(root,text="Type in the text that should appear on your button:",font=("Verdana",15),background="white").pack(side=TOP)
text=Entry(root,width=30)
text.pack(side=TOP,ipadx=50)
text.focus()

Label(root,text="Type in the command name:",font=("Verdana",15),background="white").pack(side=TOP)
cname=Entry(root,width=10)
cname.pack(side=TOP,ipadx=10)

def go():
    product=open('product.py','a+')
    rootname=open('temp.txt','r')
    product.write("\ndef "+cname.get()+"():{}")
    product.write("\nButton("+rootname.readline()+",text=\""+text.get()+"\").pack()")
    messagebox.showinfo("Succesful","Button added succesfully")
    product.close()
    rootname.close()
    



Label(root,text="",font=("Verdana",15),background="white").pack(side=TOP)
                  
Button(root,text="Add",command=go).pack(side=TOP)
mainloop()
