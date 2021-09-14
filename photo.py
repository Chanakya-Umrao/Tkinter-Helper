from tkinter import *
from tkinter.ttk import *
import os
from tkinter import filedialog
from tkinter import messagebox


root=Tk()
root.config(bg="white")
root.geometry("800x480")
root.title("Add Image")
Label(root,text="Pick the Image location from the disk:",font=("Verdana",15),background="white").pack()
def loc():
    limage=filedialog.askopenfilename(parent=root,title="Pick the image",filetypes=[('PNG file (*.png)', '*.png')]);
    rootname=open("temp.txt",'r')
    product=open("product.py",'a+')
    product.write("\nrimage=PhotoImage(file=\""+limage+"\")")
    product.write("\nLabel("+rootname.readline()+",image=rimage).pack()")
    rootname.close()
    product.close()
    messagebox.showinfo("Succesful","Image Added Successfully")
    
Button(root,text="Pick",command=loc).pack()
mainloop()
