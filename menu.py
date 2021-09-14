from tkinter import *
from tkinter.ttk import *
import os

root=Tk()
root.geometry("300x380")
root.title("Tkinter Helper")
root.config(background="white")

def wd():
    os.system("wd.py")
def ws():
    os.system("widget_selection.py")

Label(root,text="Welcome to the helper",font=("italic",12),foreground='purple',background="white").pack()
Button(root,text="Create Window",command=wd).pack()
Button(root,text="Add Widget to the existing",command=ws).pack()

root.mainloop()
