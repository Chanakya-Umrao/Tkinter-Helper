from tkinter import *
from tkinter.ttk import *
import os

root=Tk()
root.config(bg="white")
root.geometry("800x480")
root.attributes("-fullscreen",True)
root.title("Selection Page")


def close():
    root.destroy()
    
tvar=[IntVar() for i in range(10)]
menu1=Menu(root,tearoff=100)
submenu=Menu(menu1)
root.config(menu=menu1)
menu1.add_command(label="X",command=close)

def go():
    if tvar[0].get()==0:
        os.system("menubar.py")
    elif tvar[0].get()==1:
        os.system("label.py")
    elif tvar[0].get()==2:
        os.system("entry.py")
    elif tvar[0].get()==3:
        os.system("photo.py")
    elif tvar[0].get()==4:
        os.system("checkbutton.py")
    elif tvar[0].get()==5:
        os.system("radiobutton.py")
    elif tvar[0].get()==6:
        os.system("button.py")
    else:
        os.system("optionmenu.py")
    tvar[0].set(-1)
    



Label(root,text="Choose from below available widgets that suits to your GUI application",background="navy",font=("Verdana",25),foreground="white").pack()

Label(root,text="",background="white",font=("Verdana",25)).pack()
Radiobutton(root,text="Menu Bar",variable=tvar[0],value=0).pack()

Label(root,text="",background="white",font=("Verdana",25)).pack()
Radiobutton(root,text="Label",variable=tvar[0],value=1).pack()

Label(root,text="",background="white",font=("Verdana",25)).pack()
Radiobutton(root,text="Entry",variable=tvar[0],value=2).pack()

Label(root,text="",background="white",font=("Verdana",25)).pack()
Radiobutton(root,text="Photo",variable=tvar[0],value=3).pack()

Label(root,text="",background="white",font=("Verdana",25)).pack()
Radiobutton(root,text="CheckButton",variable=tvar[0],value=4).pack()

Label(root,text="",background="white",font=("Verdana",25)).pack()
Radiobutton(root,text="Radiobutton",variable=tvar[0],value=5).pack()

Label(root,text="",background="white",font=("Verdana",25)).pack()
Radiobutton(root,text="Button",variable=tvar[0],value=6).pack()

Label(root,text="",background="white",font=("Verdana",25)).pack()
Radiobutton(root,text="OptionMenu",variable=tvar[0],value=7).pack()






def finish():
    temp=open("product.py",'a+')
    temp1=open("temp.txt",'r')
    temp.write("\n"+temp1.readline()+".mainloop()")
    temp.close()
    temp1.close()
    os.system("product.py")

Button(root,text="Add",command=go).pack(side=LEFT,padx=600,pady=100);
Button(root,text="Finish",command=finish).pack(side=LEFT,padx=0)
root.mainloop()
