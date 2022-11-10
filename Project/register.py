from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
from login import Login
from controller import MySql


class Register:
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
        image = Image.open("Images/student.jpg")
 
        # Resize the image using resize() method
        resize_image = image.resize((550, 600))

        self.left = ImageTk.PhotoImage(resize_image)



        left=Label(self.root,image=self.left).place(x=100,y=100,width=400,height=500)

        #Regd Frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        #Elements in frame

        title=Label(frame1,text="REGISTRATION FORM" , font=("time new roman",20,"bold"),bg= "white" ,fg ="green").place(x=50,y=30)
  
        f_name=Label(frame1,text="First name" , font=("time new roman",15,"bold"),bg= "white" ,fg ="gray").place(x=50,y=100)
        self.text_fname = Entry(frame1,font=("time new roman",15),bg= "white" ,fg ="gray")
        self.text_fname.place(x=50,y=130,width=250)

        l_name=Label(frame1,text="Last name" , font=("time new roman",15,"bold"),bg= "white" ,fg ="gray").place(x=370,y=100)
        self.text_lname = Entry(frame1,font=("time new roman",15),bg= "white" ,fg ="gray")
        self.text_lname.place(x=370,y=130,width=250)

        classes=Label(frame1,text="Class" , font=("time new roman",15,"bold"),bg= "white" ,fg ="gray").place(x=50,y=170)
        self.text_class = Entry(frame1,font=("time new roman",15),bg= "white" ,fg ="gray")
        self.text_class.place(x=50,y=200,width=250)



        username=Label(frame1,text="Username" , font=("time new roman",15,"bold"),bg= "white" ,fg ="gray").place(x=370,y=170)
        self.text_username = Entry(frame1,font=("time new roman",15),bg= "white" ,fg ="gray")
        self.text_username.place(x=370,y=200,width=250)


        security=Label(frame1,text="Security Question" , font=("time new roman",15,"bold"),bg= "white" ,fg ="gray").place(x=50,y=240)
        self.cmb_security = ttk.Combobox(frame1,font=("time new roman",13),state = 'readonly',justify=CENTER)
        self.cmb_security['values'] = ("Select","Your Nick Name","Your School Name","Your Hobbies","Your Birth Place")
        self.cmb_security.place(x=50,y=270,width=250)
        self.cmb_security.current(0)
        
        answer=Label(frame1,text="Answer" , font=("time new roman",15,"bold"),bg= "white" ,fg ="gray").place(x=370,y=240)
        self.text_answer = Entry(frame1,font=("time new roman",15),bg= "white" ,fg ="gray")
        self.text_answer.place(x=370,y=270,width=250)
        password=Label(frame1,text="Password" , font=("time new roman",15,"bold"),bg= "white" ,fg ="gray").place(x=50,y=310)
        self.text_password = Entry(frame1,font=("time new roman",15),bg= "white" ,fg ="gray")
        self.text_password.place(x=50,y=340,width=250)

        cpassword=Label(frame1,text="Confirm password" , font=("time new roman",15,"bold"),bg= "white" ,fg ="gray").place(x=370,y=310)
        self.text_cpassword = Entry(frame1,font=("time new roman",15),bg= "white" ,fg ="gray")
        self.text_cpassword.place(x=370,y=340,width=250)

        self.var_chk = IntVar()
        chk =Checkbutton(frame1,text="I Agree The Terms & Conditions",variable = self.var_chk,onvalue =1,offvalue=0, bg="white", font=("times new roman",12)).place(x = 50,y=380)
        btn=Button(frame1,text ="Register",font=("time new roman",20),bd=0,cursor="hand2",command=self.register_data).place(x=50,y=420)
        btn_login=Button(self.root,text =" Sign In",font=("time new roman",20),bd=0,cursor="hand2",command=lambda: Login(root)).place(x=200,y=460,width =180)

    def register_data(self):
        if self.text_fname.get() =="" or self.text_lname.get() =="" or self.text_class.get() =="" or self.text_username.get() =="" or self.text_answer.get() =="" or self.text_password.get() =="" or self.text_cpassword.get() =="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.text_password.get() != self.text_cpassword.get() :
            messagebox.showerror("Error","Password & Confirm Password should be same",parent=self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error","Please Agree our terms & condition",parent=self.root)
        else:
            ms=MySql()
            result = ms.student_register(self.text_fname.get(), self.text_lname.get(), int(self.text_class.get()), self.text_username.get(), self.cmb_security.get(), self.text_answer.get(), self.text_cpassword.get())
            if result["success"] == True:
                messagebox.showinfo("Success","Register Sucessfull",parent=self.root)
                Login(self.root)
            else:
                messagebox.showerror("Error",result["error"],parent=self.root)



            
            
   


# root=Tk()

# obj=Register(root)

# root.mainloop()