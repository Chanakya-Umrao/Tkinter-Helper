from tkinter import *
from tkinter.ttk import *
import os
from tkinter import messagebox

root=Tk()
root.geometry("1000x780")
root.title("Add Menubar")
Label(root,text="Add cascade:",font=("aerial",20)).pack()    
Label(root,text="Name of the cascade").pack()
cascadename=Entry(root)
cascadename.pack()
cascadename.focus()


temp1=open('temp.txt',"r")
rootname=temp1.readline()
temp=open("product.py","a+")
temp.write("\nmainmenu=Menu()")
temp.write("\n"+rootname+".config(menu=mainmenu)")
temp.close()
temp1.close()
def addcascade():
    temp=open("product.py","a+")
    name=cascadename.get()
    temp1=open('temp.txt',"r")
    rootname=temp1.readline()
    temp.write("\n"+name+"=Menu()")
    temp.write("\nmainmenu.add_cascade(label=\""+name+"\",menu="+name+")")
    temp.close()
    temp1.close()
    messagebox.showinfo("succesful","Cascade Added Succesfully")
    temp.close()
    
Button(root,text="Add",command=addcascade).pack()

Label(root,text="Add command:",font=("aerial",20)).pack()    
Label(root,text="Name of the cascade").pack()
ccascade=Entry(root)
ccascade.pack()
Label(root,text="Name of the command").pack()
commandname=Entry(root)
commandname.pack()
def addcommand():
    caname=ccascade.get()
    cmname=commandname.get()
    product=open("product.py","a+")
    product.write("\ndef "+cmname+"():{\n#Complete your command definition here\n}")
    product.write("\n"+caname+".add_command(label=\""+cmname+"\",command="+cmname+")") 
    
    
Button(root,text="Add",command=addcommand).pack()

root.mainloop()
