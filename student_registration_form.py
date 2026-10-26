import tkinter as tk
from tkinter import ttk, messagebox

students = []  # stores all submitted student details


def submit():
    student = {
        "Name": name_var.get(),
        "Age": age_var.get(),
        "Gender": gender_var.get(),
        "Course": course_var.get(),
    }
    students.append(student)

    details = (
        f"Name: {student['Name']}\n"
        f"Age: {student['Age']}\n"
        f"Gender: {student['Gender']}\n"
        f"Course: {student['Course']}"
    )
    messagebox.showinfo("Student Details", details)


def view_all():
    if not students:
        messagebox.showinfo("All Students", "No students registered yet.")
        return

    text = ""
    for i, s in enumerate(students, start=1):
        text += (
            f"Student {i}\n"
            f"Name: {s['Name']}\n"
            f"Age: {s['Age']}\n"
            f"Gender: {s['Gender']}\n"
            f"Course: {s['Course']}\n\n"
        )
    messagebox.showinfo("All Students", text)


root = tk.Tk()
root.title("Student Registration Form")
root.geometry("400x400")

name_var = tk.StringVar()
age_var = tk.StringVar()
gender_var = tk.StringVar()
course_var = tk.StringVar()

# Name
tk.Label(root, text="Name:").pack(pady=5)
tk.Entry(root, textvariable=name_var).pack(pady=5)

# Age
tk.Label(root, text="Age:").pack(pady=5)
tk.Entry(root, textvariable=age_var).pack(pady=5)

# Gender
tk.Label(root, text="Gender:").pack(pady=5)
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()

# Course
tk.Label(root, text="Course:").pack(pady=5)
ttk.Combobox(root, textvariable=course_var, values=["BCA", "BSc", "BCom", "BA"]).pack(pady=5)

# Buttons
tk.Button(root, text="Submit", command=submit).pack(pady=10)
tk.Button(root, text="View All", command=view_all).pack(pady=5)

root.mainloop()