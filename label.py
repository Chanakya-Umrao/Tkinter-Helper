from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import os
root=Tk() 
root.geometry("1024x760")
root.title("Adding a Label")

Label(root,text="Type in the text that you want to add:").pack()
text=Entry(root,width=100)
text.pack()
Label(root,text="Foreground colour:").pack()
fg=Entry(root)
fg.pack()
Label(root,text="Background colour").pack()
bg=Entry(root)
bg.pack()
Label(root,text="Font-Style").pack()
font=Entry(root,width=10)
font.pack();
Label(root,text="Size").pack()
size=Entry(root,width=5)
size.pack()

def addlabel():
    product=open("product.py",'a+')
    rootname=open("temp.txt",'r')
    product.write("\nLabel("+rootname.readline()+",text=\""+text.get()+"\",background=\""+bg.get()+"\",foreground=\""+fg.get()+"\",font=(\""+font.get()+"\","+size.get()+")).pack()")
    messagebox.showinfo("Success","Label added successfully")
Label(root,text="").pack()
Button(root,command=addlabel,text="Add").pack()
root.mainloop()
