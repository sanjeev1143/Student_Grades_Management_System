from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
from teacher import Teacher
from admin import Admin
from register import Register

class Home:
    def __init__(self,root):
        self.root=root
        #basic window
        self.root.title("HOME")
        self.root.geometry("1520x900+0+0")
        
        #Background Image

        self.bg = ImageTk.PhotoImage(file="Images/bg.png")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

       

        

        #Regd Frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=400,y=100,width=700,height=500)

        #Elements in frame
        title=Label(frame1,text="HOME" , font=("time new roman",20,"bold"),bg= "white" ,fg ="green").place(x=260,y=30)

        admin=Button(frame1,text ="Admin",font=("time new roman",20),bd=0,cursor="hand2",command=lambda:Admin(root)).place(x=50,y=150)
        teacher=Button(frame1,text ="Teacher",font=("time new roman",20),bd=0,cursor="hand2",command=lambda:Teacher(root)).place(x=250,y=150)
        student=Button(frame1,text ="Student",font=("time new roman",20),bd=0,cursor="hand2",command=lambda:Register(root)).place(x=450,y=150)

       
    

root=Tk()

obj=Home(root)

root.mainloop()
