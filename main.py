from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from student import Student
import os
from time import strftime
from datetime import datetime
from train import Train
from face_recognising import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
import tkinter

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry(f"{screen_width}x{screen_height}")
        self.root.title("Face Recognition System")

        # Background Image
        img3 = Image.open(r"images\Untitled.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=5, width=1530, height=710)

        title_lbl = Label(bg_img, text="AUTOMATED ATTENDANCE SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1354, height=45)
        
    # ==================Time============================
        def time():
            string = strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000, time)
            
        lbl = Label(title_lbl, font=("times new roman", 14, "bold"), bg="white", fg="red")
        lbl.place(x=0, y=0, width=110, height=50)
        time()

        # Student Button
        img4 = Image.open(r"images\students.jpg")
        img4 = img4.resize((200, 200), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2")
        b1.place(x=111, y=100, width=200, height=200)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=111, y=300, width=200, height=40)
        
        # Train Data Button
        img8 = Image.open(r"images\train.jpg")
        img8 = img8.resize((200, 200), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, command=self.train_data, cursor="hand2")
        b1.place(x=111, y=380, width=200, height=200)

        b1_1 = Button(bg_img, text="Train Data", command=self.train_data, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=111, y=580, width=200, height=40)

        # Detect Face Button
        img5 = Image.open(r"images\detector.jpg")
        img5 = img5.resize((200, 200), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, command=self.face_data, cursor="hand2")
        b1.place(x=422, y=100, width=200, height=200)

        b1_1 = Button(bg_img, text="Face Detector", command=self.face_data, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=422, y=300, width=200, height=40)

        # Attendance Button
        img6 = Image.open(r"images\attendance.png")
        img6 = img6.resize((200, 200), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2", command=self.attendance_data)
        b1.place(x=733, y=100, width=200, height=200)

        b1_1 = Button(bg_img, text="Attendance", cursor="hand2", command=self.attendance_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=733, y=300, width=200, height=40)
        
        # Photos Button
        img9 = Image.open(r"images\photos.jpg")
        img9 = img9.resize((200, 200), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, command=self.open_img, cursor="hand2")
        b1.place(x=422, y=380, width=200, height=220)

        b1_1 = Button(bg_img, text="Photos",command=self.open_img, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=422, y=580, width=200, height=40)

        # Help Desk Button
        img7 = Image.open(r"images\help.jpg")
        img7 = img7.resize((200, 200), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2", command=self.help_data)
        b1.place(x=1044, y=100, width=200, height=200)

        b1_1 = Button(bg_img, text="Help Desk", cursor="hand2", command=self.help_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1044, y=300, width=200, height=40)

        # Developer Button
        img10 = Image.open(r"images\developer.jpg")
        img10 = img10.resize((200, 200), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2", command=self.developer_data)
        b1.place(x=733, y=380, width=200, height=200)

        b1_1 = Button(bg_img, text="Developers", cursor="hand2", command=self.developer_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=733, y=580, width=200, height=40)

        # Exit Button
        img11 = Image.open(r"images\exit.jpg")
        img11 = img11.resize((200, 200), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2", command=self.iExit)
        b1.place(x=1044, y=380, width=200, height=200)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2", command=self.iExit, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1044, y=580, width=200, height=40)
        
    def open_img(self):
        os.startfile("data")
        
    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition", "Confirm if you want to exit", parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return    
        

        # =================Function Buttons=================
        # Student Button
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
        
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
        
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)
        
    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)
        
    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window) 




if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()