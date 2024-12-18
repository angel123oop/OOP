from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()
root.title('Student Information System')
root.geometry("500x500")
root.configure(bg="#F9E0EC")  

title_label = Label(root, text="Student Information System", font=("Arial", 24, "bold"),  bg="#F9E0EC", fg="white")
title_label.grid(row=0, column=1, columnspan=3, pady=20)

conn = sqlite3.connect('student_information_system.db')
c = conn.cursor()

def submit():
    conn = sqlite3.connect('student_information_system.db')
    c = conn.cursor()
    c.execute("""
        INSERT INTO student_information_system VALUES(:name, :date_of_birth, :place_of_birth, :age, :gender, :address, :contact_no, :school, :year_level, :course, :mothers_name, :mothers_occupation, :fathers_name, :fathers_occupation)
    """, {
        'name': name.get(),
        'date_of_birth': date_of_birth.get(),
        'place_of_birth': place_of_birth.get(),
        'age': age.get(),
        'gender': gender.get(), 
        'address': address.get(),
        'contact_no': contact_no.get(),
        'school': school.get(),
        'year_level': year_level.get(),
        'course': course.get(),
        'mothers_name': mothers_name.get(),
        'mothers_occupation': mothers_occupation.get(),
        'fathers_name': fathers_name.get(),
        'fathers_occupation': fathers_occupation.get(),
    })
    conn.commit()
    conn.close()

    name.delete(0, END)
    date_of_birth.delete(0, END)
    place_of_birth.delete(0, END)
    age.delete(0, END)
    address.delete(0, END)
    contact_no.delete(0, END)
    school.delete(0, END)
    year_level.delete(0, END)
    course.delete(0, END)
    mothers_name.delete(0, END)
    mothers_occupation.delete(0, END)
    fathers_name.delete(0, END)
    fathers_occupation.delete(0, END)
    gender.set("")  

from tkinter import ttk

def query():
    query_window = Toplevel()
    query_window.title("View Records")
    query_window.geometry("1000x600") 
    query_window.configure(bg="#F9E0EC")

    
    query_window.rowconfigure(0, weight=1)
    query_window.columnconfigure(0, weight=1)

   
    tree = ttk.Treeview(query_window)
    tree.grid(row=0, column=0, sticky='nsew')  # Make Treeview fill the available space

    
    scrollbar = ttk.Scrollbar(query_window, orient="vertical", command=tree.yview)
    scrollbar.grid(row=0, column=1, sticky='ns')  
    tree.configure(yscrollcommand=scrollbar.set)

 
    tree['columns'] = (
        "Name", "DOB", "POB", "Age", "Sex", "Address", "Contact No",
        "School", "Year Level", "Course", "Mother's Name", "Mother's Occupation",
        "Father's Name", "Father's Occupation", "ID"
    )

  
    for col in tree['columns']:
        tree.column(col, anchor="w", width=50)  
        tree.heading(col, text=col, anchor="w")

    tree.column("#0", width=0, stretch=NO)  

   
    conn = sqlite3.connect('student_information_system.db')
    c = conn.cursor()

    
    c.execute("SELECT *, oid FROM student_information_system")
    records = c.fetchall()
    for record in records:
        tree.insert("", "end", values=record)

    
    conn.close()

   
    close_btn = Button(
        query_window,
        text="Close",
        command=query_window.destroy,
        bg="#FF69B4",
        fg="white",
        font=("Arial", 12)
    )
    close_btn.grid(row=1, column=0, pady=10, columnspan=2, sticky="e")  # Align close button


    
def delete():
    conn = sqlite3.connect('student_information_system.db')
    c = conn.cursor()
    c.execute("DELETE FROM student_information_system WHERE oid = ?", (str(delete_box.get()),))
    delete_box.delete(0, END)
    conn.commit()
    conn.close()
    
def update():
    conn = sqlite3.connect('student_information_system.db')
    c = conn.cursor()

    record_id = delete_box.get()
    c.execute("""
    UPDATE student_information_system SET
        name = :name,
        date_of_birth = :date_of_birth,
        place_of_birth = :place_of_birth,
        age = :age,
        gender = :gender,
        address = :address,
        contact_no = :contact_no,
        school = :school,
        year_level = :year_level,
        course = :course,
        mothers_name = :mothers_name,
        mothers_occupation = :mothers_occupation,
        fathers_name = :fathers_name,
        fathers_occupation = :fathers_occupation


        
    WHERE oid = :oid
    """, {
        'name': name_editor.get(),
        'date_of_birth' :date_of_birth_editor.get(),
        'place_of_birth' :place_of_birth_editor.get(),
        'age': age_editor.get(),
        'gender': gender_editor.get(),
        'address': address_editor.get(),
        'contact_no': contact_no_editor.get(),
        'school': school_editor.get(),
        'year_level': year_level_editor.get(),
        'course': course_editor.get(),
        'mothers_name' :mothers_name_editor.get(),
        'mothers_occupation' :mothers_occupation_editor.get(),
        'fathers_name' :fathers_name_editor.get(),
        'fathers_occupation' :fathers_occupation_editor.get(),
        'oid': record_id
    })

    conn.commit()
    conn.close()



def edit():
    editor = Tk()
    editor.title('Update Record')
    editor.geometry("500x500")
    editor.configure(bg="#F9E0EC")

    conn = sqlite3.connect('student_information_system.db')
    c = conn.cursor()

    record_id = delete_box.get()
    c.execute("SELECT * FROM student_information_system WHERE oid=" + record_id)
    records = c.fetchall()


    global name_editor
    global date_of_birth_editor
    global place_of_birth_editor
    global age_editor
    global gender_editor
    global address_editor
    global contact_no_editor
    global school_editor
    global year_level_editor
    global course_editor
    global mothers_name_editor
    global mothers_occupation_editor
    global fathers_name_editor
    global fathers_occupation_editor

    
    
    name_editor = Entry(editor, width=30, font=("Arial", 12))
    name_editor.grid(row=1, column=1, padx=20)
    date_of_birth_editor= Entry(editor, width=30, font=("Arial", 12))
    date_of_birth_editor.grid(row=2, column=1, padx=20)
    place_of_birth_editor= Entry(editor, width=30, font=("Arial", 12))
    place_of_birth_editor.grid(row=3, column=1, padx=20) 
    age_editor = Entry(editor, width=30, font=("Arial", 12))
    age_editor.grid(row=4, column=1, padx=20)
    gender_editor = Entry(editor, width=30, font=("Arial", 12))
    gender_editor.grid(row=5, column=1, padx=20)
    address_editor = Entry(editor, width=30, font=("Arial", 12))
    address_editor.grid(row=6, column=1, padx=20)
    contact_no_editor = Entry(editor, width=30, font=("Arial", 12))
    contact_no_editor.grid(row=7, column=1, padx=20)
    school_editor = Entry(editor, width=30, font=("Arial", 12))
    school_editor.grid(row=1, column=3, padx=20)
    year_level_editor = Entry(editor, width=30, font=("Arial", 12))
    year_level_editor.grid(row=2, column=3, padx=20)
    course_editor = Entry(editor, width=30, font=("Arial", 12))
    course_editor.grid(row=3, column=3, padx=20)
    mothers_name_editor = Entry(editor, width=30, font=("Arial", 12))
    mothers_name_editor.grid(row=4,  column=3, padx=20)
    mothers_occupation_editor = Entry(editor, width=30, font=("Arial", 12))
    mothers_occupation_editor.grid(row=5,  column=3, padx=20)
    fathers_name_editor = Entry(editor, width=30, font=("Arial", 12))
    fathers_name_editor.grid(row=6, column=3, padx=20)
    fathers_occupation_editor = Entry(editor, width=30, font=("Arial", 12))
    fathers_occupation_editor.grid(row=7,  column=3, padx=20)


    
    name_label = Label(editor, text="Name", bg="#F9E0EC", font=("Arial", 10))
    name_label.grid(row=1, column=0, pady=(10, 0))
    date_of_birth_label = Label(editor, text="Date of Birth", bg="#F9E0EC", font=("Arial", 10))
    date_of_birth_label.grid(row=2, column=0)
    place_of_birth_label = Label(editor, text="Place of Birth", bg="#F9E0EC", font=("Arial", 10))
    place_of_birth_label.grid(row=3, column=0) 
    age_label = Label(editor, text="Age", bg="#F9E0EC", font=("Arial", 10))
    age_label.grid(row=4, column=0)
    gender_label = Label(editor, text="Sex", bg="#F9E0EC", font=("Arial", 10))
    gender_label.grid(row=5, column=0)
    address_label = Label(editor, text="Address", bg="#F9E0EC", font=("Arial", 10))
    address_label.grid(row=6, column=0)
    contact_no_label = Label(editor, text="Contact No.", bg="#F9E0EC", font=("Arial", 10))
    contact_no_label.grid(row=7, column=0)
    school_label = Label(editor, text="School", bg="#F9E0EC", font=("Arial", 10))
    school_label.grid(row=1, column=2)
    year_level_label = Label(editor, text="Year Level", bg="#F9E0EC", font=("Arial", 10))
    year_level_label.grid(row=2, column=2)
    course_label = Label(editor, text="Course", bg="#F9E0EC", font=("Arial", 10))
    course_label.grid(row=3, column=2)
    mothers_name_label = Label(editor, text="Mother's Name", bg="#F9E0EC", font=("Arial", 10))
    mothers_name_label.grid(row=4, column=2)
    mothers_occupation_label = Label(editor, text="Mother's Occupation", bg="#F9E0EC", font=("Arial", 10))
    mothers_occupation_label.grid(row=5, column=2)
    fathers_name_label = Label(editor, text="Father's name", bg="#F9E0EC", font=("Arial", 10))
    fathers_name_label.grid(row=6, column=2)
    fathers_occupation_label = Label(editor, text="Father's Occupation", bg="#F9E0EC", font=("Arial", 10))
    fathers_occupation_label.grid(row=7, column=2)

    for record in records:
        name_editor.insert(0, record[0])
        date_of_birth_editor.insert(0, record[1])
        place_of_birth_editor.insert(0, record[2])
        age_editor.insert(0, record[3])
        gender_editor.insert(0, record[4])
        address_editor.insert(0, record[5])
        contact_no_editor.insert(0, record[6])
        school_editor.insert(0, record[7])
        course_editor.insert(0, record[8])
        year_level_editor.insert(0, record[9])
        mothers_name_editor.insert(0, record[10])
        mothers_occupation_editor.insert(0, record[11])
        fathers_name_editor.insert(0, record[12])
        fathers_occupation_editor.insert(0, record[13])
        
    save_btn = Button(editor, text="Save Record", command=update, bg="#FF69B4", fg="white", font=("Arial", 12))
    save_btn.grid(row=14, column=1, columnspan=2, pady=10, padx=10, ipadx=140)

    conn.commit()
    conn.close()
'''


c.execute("""CREATE TABLE "student_information_system" (
	"name"	TEXT,
	"date_of_birth"	INTEGER,
	"place_of_birth"	TEXT,
	"age"	INTEGER,
	"gender"	TEXT,
	"address"	TEXT,
	"contact_no"	INTEGER,
	"school"	TEXT,
	"year_level"	INTEGER,
	"course"	TEXT,
	"mothers_name"	TEXT,
	"mothers_occupation"	TEXT,
	"fathers_name"	TEXT,
	"fathers_occupation"	TEXT
)""")
'''

name = Entry(root, width=30,font=("Arial", 12))
name.grid(row=1, column=1, padx=20, pady=5)
date_of_birth = Entry(root, width=30,font=("Arial", 12))
date_of_birth.grid(row=2, column=1, padx=20, pady=5)
place_of_birth = Entry(root, width=30,font=("Arial", 12))
place_of_birth.grid(row=3, column=1, padx=20, pady=5)
age = Entry(root, width=30, font=("Arial", 12))
age.grid(row=4, column=1, padx=20, pady=5)
gender = StringVar(value="")  
gender_label = Label(root, text="Sex", bg="#F9E0EC", font=("Arial", 10))
gender_label.grid(row=7, column=0)
male_rb = Radiobutton(
    root, text="Male", variable=gender, value="Male", bg="#F9E0EC", font=("Arial", 10)
)
male_rb.grid(row=7, column=1, sticky="w", padx=20)
female_rb = Radiobutton(
    root, text="Female", variable=gender, value="Female", bg="#F9E0EC", font=("Arial", 10)
)
female_rb.grid(row=7, column=2, sticky="w", padx=20)
address = Entry(root, width=30, font=("Arial", 12))
address.grid(row=6, column=1, padx=20, pady=5)
contact_no = Entry(root, width=30, font=("Arial", 12))
contact_no.grid(row=5, column=1, padx=20, pady=5)
school = Entry(root, width=30, font=("Arial", 12))
school.grid(row=1, column=3, padx=20, pady=5)
year_level = Entry(root, width=30, font=("Arial", 12))
year_level.grid(row=2, column=3, padx=20, pady=5)
course = Entry(root, width=30, font=("Arial", 12))
course.grid(row=3, column=3, padx=20, pady=5)
mothers_name = Entry(root, width=30, font=("Arial", 12))
mothers_name.grid(row=4, column=3, padx=20, pady=5)
mothers_occupation = Entry(root, width=30, font=("Arial", 12))
mothers_occupation.grid(row=5, column=3, padx=20, pady=5)
fathers_name = Entry(root, width=30, font=("Arial", 12))
fathers_name.grid(row=6, column=3, padx=20, pady=5)
fathers_occupation = Entry(root, width=30, font=("Arial", 12))
fathers_occupation.grid(row=7, column=3, padx=20, pady=5)
                               


name_label = Label(root, text="Name", bg="#F9E0EC", font=("Arial", 10))
name_label.grid(row=1, column=0, pady=(10, 0))
date_of_birth_label = Label(root, text="Date of Birth", bg="#F9E0EC", font=("Arial", 10))
date_of_birth_label.grid(row=2, column=0)
place_of_birth_label = Label(root, text="Place of Birth", bg="#F9E0EC", font=("Arial", 10))
place_of_birth_label.grid(row=3, column=0) 
age_label = Label(root, text="Age", bg="#F9E0EC", font=("Arial", 10))
age_label.grid(row=4, column=0)
contact_no_label = Label(root, text="Contact No.", bg="#F9E0EC", font=("Arial", 10))
contact_no_label.grid(row=5, column=0)
address_label = Label(root, text="Address", bg="#F9E0EC", font=("Arial", 10))
address_label.grid(row=6, column=0)
gender_label = Label(root, text="Sex", bg="#F9E0EC", font=("Arial", 10))
gender_label.grid(row=7, column=0)

school_label = Label(root, text="School", bg="#F9E0EC", font=("Arial", 10))
school_label.grid(row=1, column=2)
year_level_label = Label(root, text="Year Level", bg="#F9E0EC", font=("Arial", 10))
year_level_label.grid(row=2, column=2)
course_label = Label(root, text="Course", bg="#F9E0EC", font=("Arial", 10))
course_label.grid(row=3, column=2)
mothers_name_label = Label(root, text="Mother's Name", bg="#F9E0EC", font=("Arial", 10))
mothers_name_label.grid(row=4, column=2)
mothers_occupation_label = Label(root, text="Mother's Occupation", bg="#F9E0EC", font=("Arial", 10))
mothers_occupation_label.grid(row=5, column=2)
fathers_name_label = Label(root, text="Father's Name", bg="#F9E0EC", font=("Arial", 10))
fathers_name_label.grid(row=6, column=2)
fathers_occupation_label = Label(root, text="Father's Occupation", bg="#F9E0EC", font=("Arial", 10))
fathers_occupation_label.grid(row=7, column=2)



                               
submit_btn = Button(root, text="Add Record", command=submit, bg="#FF69B4", fg="white", font=("Arial", 12))
submit_btn.grid(row=8, column=1, columnspan=1, pady=1, padx=0, ipadx=50, ipady=1)

query_btn = Button(root, text="View Records", command=query, bg="#FF69B4", fg="white", font=("Arial", 12))
query_btn.grid(row=9, column=1, columnspan=1, pady=1, padx=0, ipadx=50, ipady=1)

delete_btn = Button(root, text="Remove Record", command=delete, bg="#FF69B4", fg="white", font=("Arial", 12))
delete_btn.grid(row=8, column=3, columnspan=1, pady=1, padx=0, ipadx=50, ipady=1)

update_btn = Button(root, text="Update Record", command=edit, bg="#FF69B4", fg="white", font=("Arial", 12))
update_btn.grid(row=9, column=3, columnspan=1, pady=1, padx=0, ipadx=50, ipady=1)



delete_box = Entry(root, width=30, font=("Arial", 12))
delete_box.grid(row=11, column=2, padx=30, pady=5, ipady=10)

delete_box_label = Label(root, text="Select ID No.", bg="#F9E0EC", font=("Arial", 10))
delete_box_label.grid(row=10, column=2)


query_label = Label(root, text="", bg="#F9E0EC", font=("Arial", 10))
query_label.grid(row=33, column=2, columnspan=1)

root.mainloop()
