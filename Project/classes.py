from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
from controller import MySql


class Class:
    def __init__(self,root,class_):
        self.root=root
        self.class_=class_
        #basic window
        self.root.title("Window")
        self.root.geometry("1520x900+0+0")
        
        #Background Image

        self.bg = ImageTk.PhotoImage(file="Images/bg.png")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=0,relheight=0)

       

        #Svg

        # Read the Image
        image = Image.open("Images/tcr.webp")
 
        # Resize the image using resize() method
        resize_image = image.resize((501, 581))

        self.left = ImageTk.PhotoImage(resize_image)



        left=Label(self.root,image=self.left).place(x=100,y=100,width=401,height=501)

        #class Frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        #Elements in frame
        
        title=Label(frame1,text=f"Class {self.class_}"  , font=("time new roman",20,"bold"),bg= "white" ,fg ="green").place(x=260,y=30)
        ms=MySql()
        result = ms.get_grades(self.class_)
        if result["success"] == True:
            messagebox.showinfo("Success","fetched Sucessfull",parent=self.root)
            print(result["result"])
            lenght = len(result["result"])
            xx =50 
            yy = 60
            title=Label(frame1,text="Name" , font=("time new roman",20,"bold"),bg= "white" ,fg ="green").place(x=xx,y=yy)
            titleg=Label(frame1,text="grades" , font=("time new roman",20,"bold"),bg= "white" ,fg ="green").place(x=xx+350,y=yy)

            for i in range (0,lenght):
                a=result["result"][i]
                name = a[1] + " " + a[2]
                grade = a[7]
                yy+=40
                title=Label(frame1,text=f"{name}" , font=("time new roman",20,"bold"),bg= "white" ,fg ="green").place(x=xx,y=yy)
                titleg=Label(frame1,text=f"{grade}" , font=("time new roman",20,"bold"),bg= "white" ,fg ="green").place(x=xx+350,y=yy)


        else:
            messagebox.showerror("Error",result["error"],parent=self.root)

        
       
       
       
        
        
            


# root=Tk()

# obj=Login(root)

# root.mainloop()
