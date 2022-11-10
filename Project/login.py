from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
from ques import Question
from controller import MySql

class Login:
    def __init__(self,root):
        self.root=root
        
        #basic window
        self.root.title("Registration Window")
        self.root.geometry("1520x900+0+0")
        
        #Background Image

        self.bg = ImageTk.PhotoImage(file="Images/bg.png")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

       

        #Svg

        # Read the Image
        image = Image.open("Images/svg.jpg")
 
        # Resize the image using resize() method
        resize_image = image.resize((550, 600))

        self.left = ImageTk.PhotoImage(resize_image)



        left=Label(self.root,image=self.left).place(x=100,y=100,width=400,height=500)

        #Regd Frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        #Elements in frame

        title=Label(frame1,text="LOGIN FORM" , font=("time new roman",20,"bold"),bg= "white" ,fg ="green").place(x=260,y=30)
        # self.R1 = Radiobutton(frame1,text="Radio",value=2)
        # self.R1.place(x=50,y=100)
       
       
        username=Label(frame1,text="Username" , font=("time new roman",15,"bold"),bg= "white" ,fg ="gray").place(x=50,y=140)
        self.text_username = Entry(frame1,font=("time new roman",15),bg= "white" ,fg ="gray")
        self.text_username.place(x=50,y=170,width=250)


        password=Label(frame1,text="Password" , font=("time new roman",15,"bold"),bg= "white" ,fg ="gray").place(x=50,y=250)
        self.text_password = Entry(frame1,font=("time new roman",15),bg= "white" ,fg ="gray")
        self.text_password.place(x=50,y=280,width=250)
        
        btn=Button(frame1,text ="Login",font=("time new roman",20),bd=0,cursor="hand2",command=lambda: self.login_data(root)).place(x=50,y=350)

       
    def login_data(self,root):
        if self.text_username.get() =="":
            messagebox.showerror("Error","Username can't be Empty",parent=self.root)
        if self.text_password.get() =="":
            messagebox.showerror("Error","Username can't be Empty",parent=self.root)
        else:
            #messagebox.showinfo("Success","Register Sucessfull",parent=self.root)
            ms=MySql()
            result = ms.student_login(self.text_username.get(), self.text_password.get())
            if result["success"] == True:
                messagebox.showinfo("Success","Logged Sucessfull",parent=self.root)
                Question(self.root,self.text_username.get())
            else:
                messagebox.showerror("Error",result["error"],parent=self.root)
            
            


# root=Tk()

# obj=Login(root)

# root.mainloop()
