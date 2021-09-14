from tkinter import *
import time
root=Tk()
root.title("Home Screen")
root.geometry("650x500")
root.configure(bg="white")
titleLabel0=Label(root,text="",font=("italic",50),bg="white").pack()
titleLabel1=Label(root,text="The-Helper",font=("italic",40),bg="white").pack()
titleLabel2=Label(root,text="Now design your UI without coding",font=("italic",30),fg='purple',bg="white").pack()
titleLabel4=Label(root,text="",font=("italic",10),bg="white").pack()

nameLabel3=Label(root,text="By: CHANAKYA UMRAO",font=("stencil"),bg='white',fg='black').pack()
nameLabel6=Label(root,text="loading...",font=("aerial",10),bg='white',fg='black').pack()


def waitfn():
    import os
    time.sleep(1)
    root.destroy()
    os.system('menu.py')


root.after(5000,waitfn)

root.mainloop()

