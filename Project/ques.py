from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
from controller import MySql


class Question:
    def __init__(self,root,username):
        self.root=root
        self.username=username
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
        frame1.place(x=480,y=100,width=900,height=500)

        #Elements in frame

        title=Label(frame1,text="Question" , font=("time new roman",20,"bold"),bg= "white" ,fg ="green").place(x=260,y=30)
        # self.R1 = Radiobutton(frame1,text="Radio",value=2)
        # self.R1.place(x=50,y=100)
       
       
        que1=Label(frame1,text="Was your overall grade in the terminal examinations an A?" , font=("time new roman",15,"bold"),bg= "white" ,fg ="gray").place(x=30,y=80)
        self.que1 = ttk.Combobox(frame1,font=("time new roman",13),state = 'readonly',justify=CENTER)
        self.que1['values'] = ("Select","yes","no")
        self.que1.place(x=30,y=110,width=250)
        self.que1.current(0)
        que2=Label(frame1,text="Was your overall grade in the terminal examinations an B?" , font=("time new roman",15,"bold"),bg= "white" ,fg ="gray").place(x=30,y=140)
        self.que2 = ttk.Combobox(frame1,font=("time new roman",13),state = 'readonly',justify=CENTER)
        self.que2['values'] = ("Select","yes","no")
        self.que2.place(x=30,y=170,width=250)
        self.que2.current(0)
        que3=Label(frame1,text="Did you win the first prize in any interhouse sports event?" , font=("time new roman",15,"bold"),bg= "white" ,fg ="gray").place(x=30,y=200)
        self.que3 = ttk.Combobox(frame1,font=("time new roman",13),state = 'readonly',justify=CENTER)
        self.que3['values'] = ("Select","yes","no")
        self.que3.place(x=30,y=230,width=250)
        self.que3.current(0)
        que4=Label(frame1,text="Did you win the first prize in any other  interhouse co-curricular acitivity?" , font=("time new roman",15,"bold"),bg= "white" ,fg ="gray").place(x=30,y=260)
        self.que4 = ttk.Combobox(frame1,font=("time new roman",13),state = 'readonly',justify=CENTER)
        self.que4['values'] = ("Select","yes","no")
        self.que4.place(x=30,y=290,width=250)
        self.que4.current(0)
        que5=Label(frame1,text="Did you win the first prize in any interschool sports event?" , font=("time new roman",15,"bold"),bg= "white" ,fg ="gray").place(x=30,y=320)
        self.que5 = ttk.Combobox(frame1,font=("time new roman",13),state = 'readonly',justify=CENTER)
        self.que5['values'] = ("Select","yes","no")
        self.que5.place(x=30,y=350,width=250)
        self.que5.current(0)
        que6=Label(frame1,text="Did you win the second prize in any interschool sports event" , font=("time new roman",15,"bold"),bg= "white" ,fg ="gray").place(x=30,y=380)
        self.que6 = ttk.Combobox(frame1,font=("time new roman",13),state = 'readonly',justify=CENTER)
        self.que6['values'] = ("Select","yes","no")
        self.que6.place(x=30,y=410,width=250)
        self.que6.current(0)
        # que1=Label(frame1,text="Overall grade in the terminal examinations an A? (90%-/100%)" , font=("time new roman",15,"bold"),bg= "white" ,fg ="gray").place(x=50,y=140)
        # que1=Label(frame1,text="Overall grade in the terminal examinations an A? (90%-/100%)" , font=("time new roman",15,"bold"),bg= "white" ,fg ="gray").place(x=50,y=140)
        # que1=Label(frame1,text="Overall grade in the terminal examinations an A? (90%-/100%)" , font=("time new roman",15,"bold"),bg= "white" ,fg ="gray").place(x=50,y=140)

        # que1=Label(frame1,text="Overall grade in the terminal examinations an A? (90%-/100%)" , font=("time new roman",15,"bold"),bg= "white" ,fg ="gray").place(x=50,y=140)
        # que1=Label(frame1,text="Overall grade in the terminal examinations an A? (90%-/100%)" , font=("time new roman",15,"bold"),bg= "white" ,fg ="gray").place(x=50,y=140)
        
        
        submit=Button(frame1,text ="Submit",font=("time new roman",15),bd=0,cursor="hand2",command=self.submit_ans).place(x=30,y=440)

       
    def submit_ans(self):
        # if self.text_username.get() =="":
        #     messagebox.showerror("Error","Username can't be Empty",parent=self.root)
        # if self.text_password.get() =="":
        #     messagebox.showerror("Error","Username can't be Empty",parent=self.root)
        # else:
        #     messagebox.showinfo("Success","Register Sucessfull",parent=self.root)
            ms=MySql()
            grade=''
            total=0
            if self.que1.get() == "yes":
                total+=100
            if self.que2.get() == "yes":
                total+=100
            if self.que3.get() == "yes":
                total+=100
            if self.que4.get() == "yes":
                total+=100
            if self.que5.get() == "yes":
                total+=100
            if self.que6.get() == "yes":
                total+=100
            if total <= 600 and total >=400 :
                grade="A"
            elif total <= 400 and total >=300:
                grade="B"
            elif total <= 300 and total >=200:
                grade="C"
            elif total <=200 and total >= 100:
                grade="D"
            elif total <= 100 and total >=0:
                grade="F"
            result = ms.set_grade(self.username, grade)
            if result["success"] == True:
                messagebox.showinfo("Success","Submission Sucessfull",parent=self.root)

            else:
                messagebox.showerror("Error",result["error"],parent=self.root)

# root=Tk()

# obj=Ques(root)

# root.mainloop()
