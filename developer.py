from tkinter import *
from PIL import ImageTk, Image

class Developer:
    def __init__(self, root):
        self.root = root
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry(f"{screen_width}x{screen_height}")
        self.root.title("Automated Attendance System")
        self.root.config(bg="white")
        
        # title
        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1354, height=45)
        
        # logo
        img_top = Image.open(r"Images\logo.png")
        img_top = img_top.resize((1354, 720), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1354, height=720)
        
        dev_lbl = Label(f_lbl, text="Automated Attendance System is developed by: Xolani Sibsi", font=("times new roman", 20, "bold"), bg="white", fg="darkgreen")
        dev_lbl.place(x=164, y=260, width=1024, height=45)
        
        dev_lbl = Label(f_lbl, text="For any queries, please contact us at: dev@gmail.com, 071 111 1111", font=("times new roman", 20, "bold"), bg="white", fg="darkgreen")
        dev_lbl.place(x=164, y=310, width=1024, height=45)
        
        dev_lbl = Label(f_lbl, text="Special thanks to: UJ & Accenture", font=("times new roman", 20, "bold"), bg="white", fg="darkgreen")
        dev_lbl.place(x=164, y=360, width=1024, height=45)
        
        dev_lbl = Label(f_lbl, text="Version: 1.0", font=("times new roman", 20, "bold"), bg="white", fg="darkgreen")
        dev_lbl.place(x=164, y=410, width=1024, height=45)
        

        
if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
