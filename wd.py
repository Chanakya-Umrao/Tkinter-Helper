from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import os

root=Tk()
root.geometry("1024x760")
root.title("Creating Window")

def make():
    temp="from tkinter import *\nfrom tkinter.ttk import *\nimport os\n"
    rname=rootname.get()
    de=open("temp.txt","w")
    de.write(rname)
    de.close()
    temp=temp+rname+"=Tk() \n"
    temp=temp+rname+".geometry(\""+x.get()+"x"+y.get()+"\")"
    temp=temp+"\n"+rname+".config(bg=\""+bg.get()+"\")"
    file=open("product.py","w+")
    file.write(temp)
    messagebox.showinfo("succesful","Window created succesfully")
    file.close()

Label(root,text="").grid(row=1,column=1)
Label(root,text="Name for the root").grid(row=5,column=4)
rootname=Entry(root)
rootname.grid(row=5,column=7)
rootname.focus()
Label(root,text="").grid(row=6,column=1)
Label(root,text="Enter the desired size of the window Breadth and Length respectively:").grid(row=7,column=4)
x=Entry(root,width="5")
x.grid(row=7,column=7)
y=Entry(root,width="5")
y.grid(row=7,column=8)
Label(root,text="").grid(row=9,column=4)

Label(root,text="Background Colour").grid(row=10,column=4)
bg=Entry(root)
bg.grid(row=10,column=6)
Label(root,text="").grid(row=11,column=4)

Button(root,text="Make",command=make).grid(row=12,column=5)
root.mainloop()
