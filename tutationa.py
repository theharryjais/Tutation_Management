from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import sqlite3 as sql

###############Database######################

con = sql.connect(database="studentdb.sqlite")
cursor = con.cursor()
try:
    '''cursor.execute("create table students"
                   "(stu_id int,"
                   "stu_name text, "
                   "stu_mob text,"
                   "stu_course text,"
                   "reg_fee int,"
                   "bal int)")

    cursor.execute("create table course(course_name text ,course_fee int)")'''
    con.commit()

except Exception as e:
    print(e)
con.close()

#########################Window##################

win = Tk()
win.state('zoomed')
win.title("Tuition Centre Management System ")
#win.iconbitmap('C:/Users/swika/Desktop/tution.ico')

win.resizable(width=False, height=False)
header_fem = Frame(win)
header_fem.configure(bg='red')
header_fem.place(x=0, y=0, relwidth=1, relheight=0.2)

title_lbl = Label(header_fem, text='Tuition Centre Management System', bg='red',
                  font=('courier', 50, 'bold', 'underline'))
title_lbl.pack()


#################Login Page########################

def main_body():
    def login():
        u = user_entry.get()
        p = pass_entry.get()
        if len(u) == 0 or len(p) == 0:
            messagebox.showwarning('login gate', "The field Can't Be Empty")
        else:
            if u == "admin" and p == "admin":
                frm.destroy()
                login_body()
            else:
                messagebox.showerror('Login gate', "Invalid UserName/Password")

    frm = Frame(win)
    frm.configure(bg='green')
    frm.place(x=0, rely=0.2, relwidth=1, relheight=0.8)

    user_lbl = Label(frm, text='UserName', bg='green', font=('Arial', 20, 'bold'))
    user_lbl.place(relx=0.3, rely=0.2)

    user_entry = Entry(frm, font=('', 20, 'bold'), bd=7)
    user_entry.focus()
    user_entry.place(relx=0.45, rely=0.2)

    pass_lbl = Label(frm, text='Password', bg='green', font=('Arial', 20, 'bold'))
    pass_lbl.place(relx=0.3, rely=0.35)

    pass_entry = Entry(frm, font=('', 20, 'bold'), bd=7, show='*')
    pass_entry.place(relx=0.45, rely=0.35)

    log_btn = Button(frm, text='LogIn', font=('Arial', 20, 'bold'), bd=7, command=login)
    log_btn.place(relx=0.5, rely=0.5)


########################Button Main#########################

def login_body():
    def logout():
        frm.destroy()
        main_body()

    def register():
        frm.destroy()
        register_student_body()

    def find():
        frm.destroy()
        find_student_body()

    def delete():
        frm.destroy()
        delete_student_body()

    def add():
        frm.destroy()
        add_course_body()

    def update():
        frm.destroy()
        update_course_body()

    frm = Frame(win)
    frm.configure(bg='light green')
    frm.place(x=0, rely=0.2, relwidth=1, relheight=0.8)

    wel_lbl = Label(frm, text="Welcome To Oxford Tuition Centre", font=('Arial', 15, 'bold'), bg='light green')
    wel_lbl.place(relx=0, rely=0)

    log_btn = Button(frm, text="LogOut", font=('Arial', 18, 'bold'), bd=7, command=logout)
    log_btn.place(relx=0.90, rely=0)

    register_btn = Button(frm, text="Register Student", font=('Arial', 18, 'bold'), bd=7, width=15,
                          command=register)
    register_btn.place(relx=0.45, rely=.05)

    find_btn = Button(frm, text="Find Student", font=('Arial', 18, 'bold'), bd=7, width=15, command=find)
    find_btn.place(relx=0.45, rely=.25)

    del_btn = Button(frm, text="Delete", font=('Arial', 18, 'bold'), bd=7, width=15, command=delete)
    del_btn.place(relx=0.45, rely=.45)

    cour_btn = Button(frm, text="Add Course", font=('Arial', 18, 'bold'), bd=7, width=15, command=add)
    cour_btn.place(relx=0.45, rely=.65)

    upd_cors_btn = Button(frm, text="Update Course", font=('Arial', 18, 'bold'), bd=7, width=15, command=update)
    upd_cors_btn.place(relx=0.45, rely=.85)


#################################Register Student####################################

def register_student_body():
    def logout():
        frm.destroy()
        main_body()

    def home():
        frm.destroy()
        login_body()

    def register_student_db():
        id = id_entry.get()
        name = name_entry.get()
        mob = mobile_entry.get()
        cour_se = course_list.get()
        fee = fee_entry.get()
        course, course_fee = cour_se.split()

        con = sql.connect(database="studentdb.sqlite")
        cursor = con.cursor()
        if len(name) <= 0:
            messagebox.showwarning('entry ', "Student Name not be Empty")
        elif len(mob) < 10:
            messagebox.showwarning('entry', "Mobile number should be 10 digit")
        elif int(fee) <= 0 or int(fee) > int(course_fee):
            messagebox.showwarning('entry', f"Fee must be between 1 to {course_fee}")
        else:
            try:
                cursor.execute("insert into students values(?,?,?,?,?,?)",
                               (id, name, mob, course, fee, (int(course_fee) - int(fee))))
                con.commit()
                messagebox.showinfo('Arial', 'Registration Successful')
            except Exception as e:
                messagebox.showerror('entry', str(e))
            con.close()
            frm.destroy()
            register_student_body()

    frm = Frame(win)
    frm.configure(bg='light blue')
    frm.place(x=0, rely=0.2, relwidth=1, relheight=0.8)

    wel_lbl = Label(frm, text="Welcome To Oxford Tuition Centre", font=('Arial', 15, 'bold'), bg='light blue')
    wel_lbl.place(relx=0, rely=0)

    log_btn = Button(frm, text="LogOut", font=('Arial', 18, 'bold'), bd=7, command=logout)
    log_btn.place(relx=0.90, rely=0)

    home_btn = Button(frm, text="Home", font=('Arial', 18, 'bold'), bd=7, command=home)
    home_btn.place(relx=0.80, rely=0)

    con = sql.connect(database="studentdb.sqlite")
    cursor = con.cursor()
    cursor.execute("select max(stu_id) from students ")
    max_id = cursor.fetchone()
    if max_id[0] == None:
        stu_id_db = 1
    else:
        stu_id_db = max_id[0] + 1
    con.close()

    student_id = Label(frm, text='Student Id', bg='light blue', font=('', 20, 'bold'))
    student_id.place(relx=0.3, rely=0.01)

    id_entry = Entry(frm, font=('Arial', 20), bd=7)
    id_entry.insert(0, str(stu_id_db))
    id_entry.place(relx=0.5, rely=0.01)
    id_entry.configure(state='disabled')

    student_name = Label(frm, text='Student Name', bg='light blue', font=('Arial', 20, 'bold'))
    student_name.place(relx=0.3, rely=0.15)

    name_entry = Entry(frm, font=('Arial', 20), bd=7)
    name_entry.focus()
    name_entry.place(relx=0.5, rely=0.15)

    mobile_lbl = Label(frm, text='Student Mobile', bg='light blue', font=('Arial', 20, 'bold'))
    mobile_lbl.place(relx=0.3, rely=0.3)

    mobile_entry = Entry(frm, font=('Arial', 20), bd=7)
    mobile_entry.place(relx=0.5, rely=0.3)

    std_course = Label(frm, text='Select Course', bg='light blue', font=('Arial', 20, 'bold'))
    std_course.place(relx=0.3, rely=0.45)

    con = sql.connect(database="studentdb.sqlite")
    cursor = con.cursor()
    cursor.execute("select * from course")
    courses = cursor.fetchall()
    courses.insert(0, "----------Select------------")
    con.close()
    course_list = Combobox(frm, values=courses, font=('Arial', 15))
    course_list.place(relx=0.5, rely=0.45)
    course_list.current(0)

    student_fee = Label(frm, text='Registraction Fee', bg='light blue', font=('Arial', 20, 'bold'))
    student_fee.place(relx=0.3, rely=0.6)

    fee_entry = Entry(frm, font=('Arial', 20), bd=7)
    fee_entry.place(relx=0.5, rely=0.6)

    reg_btn = Button(frm, text="Register", font=('Arial', 18, 'bold'), bd=7, command=register_student_db)
    reg_btn.place(relx=0.5, rely=0.80)


################# Find Student ##########################

def find_student_body():
    def logout():
        frm.destroy()
        main_body()

    def home():
        frm.destroy()
        login_body()

    def search():
        id = serch_id_entry.get()
        con = sql.connect(database="studentdb.sqlite")
        cursor = con.cursor()
        cursor.execute("select * from students where stu_id=?", (id,))
        row = cursor.fetchone()
        if row == None:
            messagebox.showwarning('search', "Student Id not Found....")
        else:
            messagebox.showinfo('search', str(row))
            frm.destroy()
            find_student_body()

    frm = Frame(win)
    frm.configure(bg='light yellow')
    frm.place(x=0, rely=0.2, relwidth=1, relheight=0.8)

    wel_lbl = Label(frm, text="Welcome To Oxford Tuition Centre", font=('Arial', 15, 'bold'), bg='light yellow')
    wel_lbl.place(relx=0, rely=0)

    log_btn = Button(frm, text="LogOut", font=('Arial', 18, 'bold'), bd=7, command=logout)
    log_btn.place(relx=0.90, rely=0)

    home_btn = Button(frm, text="Home", font=('Arial', 18, 'bold'), bd=7, command=home)
    home_btn.place(relx=0.80, rely=0)

    serch_student_id = Label(frm, text='Student Id', bg='light yellow', font=('Arial', 20, 'bold'))
    serch_student_id.place(relx=0.25, rely=0.3)

    serch_id_entry = Entry(frm, font=('Arial', 20, 'bold'), bd=7)
    serch_id_entry.place(relx=0.45, rely=0.3)
    serch_id_entry.focus()

    srch_btn = Button(frm, text="Search", font=('Arial', 18, 'bold'), bd=7, command=search)
    srch_btn.place(relx=0.5, rely=0.5)


###################DELETE###########################


def delete_student_body():
    def logout():
        frm.destroy()
        main_body()

    def home():
        frm.destroy()
        login_body()

    def delete():
        id = deleted_id_entry.get()
        con = sql.connect(database="studentdb.sqlite")
        cursor = con.cursor()
        cursor.execute("DELETE  from students where stu_id=?", (id,))

        row = cursor.fetchone()

        if row == None:
            messagebox.showwarning('delete', "Student Id not Found....")
        else:
            messagebox.showinfo('delete', str(row))
            frm.destroy()
            delete_student_body()

    frm = Frame(win)
    frm.configure(bg='orange')
    frm.place(x=0, rely=0.2, relwidth=1, relheight=0.8)

    wel_lbl = Label(frm, text="Welcome To Oxford Tuition Centre", font=('Arial', 15, 'bold'), bg='orange')
    wel_lbl.place(relx=0, rely=0)

    log_btn = Button(frm, text="LogOut", font=('Arial', 18, 'bold'), bd=7, command=logout)
    log_btn.place(relx=0.90, rely=0)

    home_btn = Button(frm, text="Home", font=('Arial', 18, 'bold'), bd=7, command=home)
    home_btn.place(relx=0.80, rely=0)

    delete_student_id = Label(frm, text='Student Id to Delete', bg='orange', font=('Arial', 20, 'bold'))
    delete_student_id.place(relx=0.25, rely=0.3)

    deleted_id_entry = Entry(frm, font=('Arial', 20, 'bold'), bd=7)
    deleted_id_entry.place(relx=0.45, rely=0.3)
    deleted_id_entry.focus()

    del_btn = Button(frm, text="Delete", font=('Arial', 18, 'bold'), bd=7, command=delete)
    del_btn.place(relx=0.5, rely=0.5)


#############################Add Course##################

def add_course_body():
    def logout():
        frm.destroy()
        main_body()

    def home():
        frm.destroy()
        login_body()

    def add_course_db():
        n = course_name_entry.get()
        n = n.upper()
        f = course_amt_entry.get()
        con = sql.connect(database="studentdb.sqlite")
        cursor = con.cursor()
        if len(n) == 0 and len(f) == 0:
            messagebox.showwarning('entry', "Course Name And Amount not be Empty")
        else:
            try:
                cursor.execute("insert into course values(?,?)", (n, f))
                con.commit()
                messagebox.showinfo('Arial', 'Course Added')
            except Exception as e:
                messagebox.showerror('Arial', str(e))
            con.close()
            frm.destroy()
            add_course_body()

    frm = Frame(win)
    frm.configure(bg='silver')
    frm.place(x=0, rely=0.2, relwidth=1, relheight=0.8)

    wel_lbl = Label(frm, text="Welcome To Oxford Tuition Centre", font=('Arial', 15, 'bold'), bg='silver')
    wel_lbl.place(relx=0, rely=0)

    log_btn = Button(frm, text="LogOut", font=('Arial', 18, 'bold'), bd=7, command=logout)
    log_btn.place(relx=0.90, rely=0)

    home_btn = Button(frm, text="Home", font=('Arial', 18, 'bold'), bd=7, command=home)
    home_btn.place(relx=0.80, rely=0)

    course_name = Label(frm, text='Course Name', bg='silver', font=('Arial', 20, 'bold'))
    course_name.place(relx=0.25, rely=0.15)

    course_name_entry = Entry(frm, font=('Arial', 20, 'bold'), bd=7)
    course_name_entry.place(relx=0.45, rely=0.15)
    course_name_entry.focus()

    course_amt = Label(frm, text='Course Amount', bg='silver', font=('Arial', 20, 'bold'))
    course_amt.place(relx=0.25, rely=0.3)

    course_amt_entry = Entry(frm, font=('Arial', 20, 'bold'), bd=7)
    course_amt_entry.place(relx=0.45, rely=0.3)

    add_btn = Button(frm, text="Add Course", font=('Arial', 18, 'bold'), bd=7, command=add_course_db)
    add_btn.place(relx=0.5, rely=0.5)


######################Update Course##################

def update_course_body():
    def logout():
        frm.destroy()
        main_body()

    def home():
        frm.destroy()
        login_body()

    def update_course_db():
        course = update_cour_list.get()
        amt = update_amt_entry.get()
        co_urse, course_fee = course.split()

        con = sql.connect(database="studentdb.sqlite")
        cursor = con.cursor()
        cursor.execute("update course set course_fee=? where course_name=?", (amt, co_urse))
        con.commit()
        con.close()
        messagebox.showinfo('', " Course Updated...")
        frm.destroy()
        update_course_body()

    frm = Frame(win)
    frm.configure(bg='purple')
    frm.place(x=0, rely=0.2, relwidth=1, relheight=0.8)

    wel_lbl = Label(frm, text="Welcome To Oxford Tuition Centre", font=('Arial', 15, 'bold'), bg='purple')
    wel_lbl.place(relx=0, rely=0)
    home_btn = Button(frm, text="Home", font=('Arial', 18, 'bold'), bd=7, command=home)
    home_btn.place(relx=0.80, rely=0)
    log_btn = Button(frm, text="LogOut", font=('Arial', 18, 'bold'), bd=7, command=logout)
    log_btn.place(relx=0.90, rely=0)

    update_cour = Label(frm, text='Course Name', bg='purple', font=('Arial', 20, 'bold'))
    update_cour.place(relx=0.25, rely=0.15)

    con = sql.connect(database="studentdb.sqlite")
    cursor = con.cursor()
    cursor.execute("select * from course")
    courses = cursor.fetchall()
    courses.insert(0, "----------Select------------")
    con.close()

    update_cour_list = Combobox(frm, values=courses, font=('Arial', 15))
    update_cour_list.place(relx=0.5, rely=0.15)
    update_cour_list.current(0)

    update_amt = Label(frm, text='Course Amount', bg='purple', font=('Arial', 20, 'bold'))
    update_amt.place(relx=0.25, rely=0.3)

    update_amt_entry = Entry(frm, font=('Arial', 20, 'bold'), bd=7)
    update_amt_entry.place(relx=0.45, rely=0.3)


    update_btn = Button(frm, text="Update Course", font=('Arial', 18, 'bold'), bd=7, command=update_course_db)
    update_btn.place(relx=0.5, rely=0.5)


############END#################


main_body()
win.mainloop()
