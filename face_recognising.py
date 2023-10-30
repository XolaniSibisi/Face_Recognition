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

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry(f"{screen_width}x{screen_height}")
        self.root.title("Face Recognition System")
        
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1354, height=45)
        
        img_top = Image.open(r"images\irish.jpg")
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=650)
        
        img_bottom = Image.open(r"images\id_system.webp")
        img_bottom = img_bottom.resize((950, 700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=950, height=650)
        
        #button
        b1_1 = Button(f_lbl, text="Face Recognition", command=self.face_recog, cursor="hand2", font=("times new roman", 20, "bold"), bg="blue", fg="white")
        b1_1.place(x=365, y=588, width=200, height=40)
        self.attendance_marked = {}
        
    # =================== Mark Attendance ===================
    
    def mark_attendance(self, i, n, r, d):
        timestamp_now = datetime.now()
        # If the student's attendance was recently marked, skip
        if i in self.attendance_marked:
            last_marked = self.attendance_marked[i]
            time_diff = timestamp_now - last_marked
            if time_diff.total_seconds() < 300:  # 300 seconds = 5 minutes
                return
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="face_recognizer")
            my_cursor = conn.cursor()
                
            now = datetime.now()
            d1 = now.strftime("%d/%m/%Y")
            dtString = now.strftime("%H:%M:%S")
                
            with open("attendance.csv", "a", newline="\n") as f:
                writer = csv.writer(f)
                writer.writerow([i, n, r, d, dtString, d1, "Present"])
            
            # Update the attendance_marked dictionary
            self.attendance_marked[i] = timestamp_now
            
        except mysql.connector.Error as err:
            print(f"Database Error: {err}")
        finally:
            if conn.is_connected():
                conn.close()
            
            # Update the attendance_marked dictionary
            self.attendance_marked[i] = timestamp_now
                        
    # ================== Face Recognition ===================
        
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            
            coord = []
            
            for(x,y,w,h) in features:
                cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)
                id, pred = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-pred/300)))
                
                try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="", database="face_recognizer")
                    my_cursor = conn.cursor()
                    
                    my_cursor.execute("select Student_id from student where Student_id="+str(id))
                    i = my_cursor.fetchone()
                    i = i[0]
                    
                    my_cursor.execute("select Student_no from student where Student_id="+str(id))
                    n = my_cursor.fetchone()
                    n = n[0]
                    
                    my_cursor.execute("select Name from student where Student_id="+str(id))
                    r = my_cursor.fetchone()
                    r = r[0]
                    
                    my_cursor.execute("select Dep from student where Student_id="+str(id))
                    d = my_cursor.fetchone()
                    d = d[0]
                    
                    if confidence > 77:
                        cv2.putText(img, f"ID:{i}", (x,y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                        cv2.putText(img, f"Stu_Num:{n}", (x,y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                        cv2.putText(img, f"Name:{r}", (x,y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                        cv2.putText(img, f"Department:{d}", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                        self.mark_attendance(i, n, r, d)
                        
                    else:
                        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 3)
                        cv2.putText(img, "Unknown Face", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                        
                    coord = [x,y,w,h]
                except mysql.connector.Error as err:
                    print(f"Database Error: {err}")
                finally:
                    if conn.is_connected():
                        conn.close()
                
            return coord
            
        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255,255,255), "Face", clf)
            return img
            
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
            
        video_cap = cv2.VideoCapture(0)
            
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)
                
            if cv2.waitKey(1) == 13:
                break
                
        video_cap.release()
        cv2.destroyAllWindows()
                    
                    
                
        

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
