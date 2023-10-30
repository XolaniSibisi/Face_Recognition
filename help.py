from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
import csv


class Help:
    def __init__(self, root):
        self.root = root
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry(f"{screen_width}x{screen_height}")
        self.root.title("Automated Attendance System")
        
        # title
        title_lbl = Label(self.root, text="HELP", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1354, height=45)
        
        # logo
        img_top = Image.open(r"Images\logo.png")
        img_top = img_top.resize((1354, 720), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1354, height=720)
        
        dev_lbl = Label(f_lbl, text="For any queries, please contact us at: AutomatedAttendance@gmail.com", font=("times new roman", 20, "bold"), bg="white", fg="darkgreen")
        dev_lbl.place(x=164, y=260, width=1024, height=45)
        
if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
        