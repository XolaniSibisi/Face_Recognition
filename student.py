from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

# Set window size to the screen's size or any desired size
        root.geometry(f"{screen_width}x{screen_height}")
        self.root.title("Automated Attendance System")

        # Variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_Student_no = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

       
        # Background Image
        img3 = Image.open(r"images\Untitled.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1500, height=710)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1354, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=0, y=80, width=1354, height=650)

        # Left Label Frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=680, height=580)

        img_left = Image.open(r"images\student1.jpg")
        img_left = img_left.resize((650, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=650, height=130)

        # Current Course Information
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=665, height=116)

        # Department
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"), state="read only")
        dep_combo["values"] = ("Select Department", "Computer Science", "IT", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("times new roman", 12, "bold"), state="read only")
        course_combo["values"] = ("Select Course", "SBSC20", "SBSC25", "SBSC10", "SBSC05")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("times new roman", 12, "bold"), state="read only")
        year_combo["values"] = ("Select Year", "2023-24", "2024-25", "2025-26", "2026-27")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=("times new roman", 12, "bold"), state="read only")
        semester_combo["values"] = ("Select Semester", "Semester 1", "Semester 2")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class Student Information
        class_Student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        class_Student_frame.place(x=5, y=250, width=665, height=300)

        # Student ID
        studentID_label = Label(class_Student_frame, text="Student ID:", font=("times new roman", 12, "bold"), bg="white")
        studentID_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentID_entry = ttk.Entry(class_Student_frame, textvariable=self.var_std_id, width=20, font=("times new roman", 12, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student name
        studentName_label = Label(class_Student_frame, text="Student Name:", font=("times new roman", 12, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_name, width=20, font=("times new roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class Division
        classDivision_label = Label(class_Student_frame, text="Class Division:", font=("times new roman", 12, "bold"), bg="white")
        classDivision_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        classDivision_combo = ttk.Combobox(class_Student_frame, textvariable=self.var_div, font=("times new roman", 12, "bold"), state="read only", width=18)
        classDivision_combo["values"] = ("Select", "A", "B", "C")
        classDivision_combo.current(0)
        classDivision_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        
        # Student_no Number
        Student_noNumber_label = Label(class_Student_frame, text="Student Number:", font=("times new roman", 12, "bold"), bg="white")
        Student_noNumber_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        Student_noNumber_entry = ttk.Entry(class_Student_frame, textvariable=self.var_Student_no, width=20, font=("times new roman", 12, "bold"))
        Student_noNumber_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        gender_label = Label(class_Student_frame, text="Gender:", font=("times new roman", 12, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_Student_frame, textvariable=self.var_gender, font=("times new roman", 12, "bold"), state="read only", width=18)
        gender_combo["values"] = ("Select", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Date of Birth
        dob_label = Label(class_Student_frame, text="Date of Birth:", font=("times new roman", 12, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_Student_frame, textvariable=self.var_dob, width=20, font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label = Label(class_Student_frame, text="Email:", font=("times new roman", 12, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_Student_frame, textvariable=self.var_email, width=20, font=("times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone Number
        phone_label = Label(class_Student_frame, text="Phone Number:", font=("times new roman", 12, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_Student_frame, textvariable=self.var_phone, width=20, font=("times new roman", 12, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        address_label = Label(class_Student_frame, text="Address:", font=("times new roman", 12, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_Student_frame, textvariable=self.var_address, width=20, font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher Name
        teacherName_label = Label(class_Student_frame, text="Teacher Name:", font=("times new roman", 12, "bold"), bg="white")
        teacherName_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacherName_entry = ttk.Entry(class_Student_frame, textvariable=self.var_teacher, width=20, font=("times new roman", 12, "bold"))
        teacherName_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # Radio Buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_Student_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=5, column=0)
        
        radiobtn2 = ttk.Radiobutton(class_Student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=5, column=1)

        # Button Frame
        btn_frame = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=655, height=70)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0,)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1,)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2,)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3,)

        btn_frame1 = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=235, width=655, height=35)

        take_photo_btn = Button(btn_frame1, command=self.generate_dataset, text="Take Photo Sample", width=36, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=4,)

        update_photo_btn = Button(btn_frame1, text="Update Photo Sample", width=35, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=5,)

        # Right Label Frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=700, y=10, width=645, height=580)

        img_right = Image.open(r"images\fr_system.png")
        img_right = img_right.resize((700, 150), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=630, height=130)

        # Search System
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search Student", font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=135, width=630, height=120)

        search_label = Label(search_frame, text="Search By:", font=("times new roman", 12, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), state="read only")
        search_combo["values"] = ("Select", "Student Number", "Email")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(search_frame, width=40, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        search_btn.grid(row=2, column=1, padx=4)

        showAll_btn = Button(search_frame, text="Show All", width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row=2, column=2, padx=4)

        # Table Frame
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=260, width=630, height=290)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("Student_no", "dep", "course", "year", "sem", "id", "name", "div", "gender", "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("Student_no", text="Student Number")
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentID")
        self.student_table.heading("name", text="StudentName")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"
        
        self.student_table.column("Student_no", width=100)
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # ======================Function Declaration======================

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required", parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                               self.var_Student_no.get(),
                                                                                                               self.var_dep.get(),
                                                                                                               self.var_course.get(),
                                                                                                               self.var_year.get(),
                                                                                                               self.var_semester.get(),
                                                                                                               self.var_std_id.get(),
                                                                                                               self.var_std_name.get(),
                                                                                                               self.var_div.get(),
                                                                                                               self.var_gender.get(),
                                                                                                               self.var_dob.get(),
                                                                                                               self.var_email.get(),
                                                                                                               self.var_phone.get(),
                                                                                                               self.var_address.get(),
                                                                                                               self.var_teacher.get(),
                                                                                                               self.var_radio1.get()
                                                                                                               ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    # ===========================Fetch Data===========================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="",database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close() 

    # ===========================Get Cursor===========================
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        
        self.var_Student_no.set(data[0]),
        self.var_dep.set(data[1]),
        self.var_course.set(data[2]),
        self.var_year.set(data[3]),
        self.var_semester.set(data[4]),
        self.var_std_id.set(data[5]),
        self.var_std_name.set(data[6]),
        self.var_div.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # ===========================Update Function===========================
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", user="root",password="", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Student_no=%s,Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                                            self.var_Student_no.get(),
                                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                                            self.var_std_id.get()
                                                                                                                                                                                                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Student details successfully update completed", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    # ===========================Delete Function===========================
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", user="root",password="", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    # ===========================Reset Function===========================
    def reset_data(self):
        self.var_Student_no.set(""),
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select Division"),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")
        
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root",password="", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                    my_cursor.execute("update student set Student_no=%s,Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s", (
                    self.var_Student_no.get(),
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get() == id+1
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    
                    # If no face is detected, return None
                    if len(faces) == 0:
                        return None
        
                    # Return the first detected face
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                    

                cap = cv2.VideoCapture(0)
                img_id = 0
                
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)
                        
                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                

                messagebox.showinfo("Result", "Generating dataset completed!!!")

            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

 

                                                                                                                                                                                                    


                                                                                                                                                                                                                    

        
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()