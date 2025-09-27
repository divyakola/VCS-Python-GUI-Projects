import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime
import pandas as pd

# DB init
def init_db():
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS registrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            mobile TEXT,
            gender TEXT,
            course TEXT,
            sources TEXT,
            reg_date TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_data():
    name = entry_name.get().strip()
    email = entry_email.get().strip()
    mobile = entry_mobile.get().strip()
    gender = gender_var.get()
    course = course_var.get()
    # Gather checked sources
    sources = []
    for var, label in sources_vars:
        if var.get() == 1:
            sources.append(label)
    sources_str = ", ".join(sources)
    reg_date = datetime.now().strftime("%Y-%m-%d")

    if not (name and email and mobile and gender and course):
        messagebox.showerror("Error", "Please fill all mandatory fields.")
        return

    if not sources:
        messagebox.showerror("Error", "Please select at least one source.")
        return

    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO registrations (name,email,mobile,gender,course,sources,reg_date) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (name,email,mobile,gender,course,sources_str,reg_date))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Student registered successfully!")
    clear_fields()

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_mobile.delete(0, tk.END)
    gender_var.set(None)
    course_var.set(course_options[0])
    for var, _ in sources_vars:
        var.set(0)

def export_all_to_excel():
    conn = sqlite3.connect("students.db")
    df = pd.read_sql_query("SELECT * FROM registrations", conn)
    df.to_excel("All_Students.xlsx", index=False)
    conn.close()
    messagebox.showinfo("Exported", "All data exported to All_Students.xlsx")

def generate_daily_report():
    date = datetime.now().strftime("%Y-%m-%d")
    conn = sqlite3.connect("students.db")
    query = "SELECT * FROM registrations WHERE reg_date = ?"
    df = pd.read_sql_query(query, conn, params=(date,))
    courses = df["course"].unique()
    if len(df) == 0:
        messagebox.showinfo("No Data", "No registrations found for today.")
        return
    for course in courses:
        df_course = df[df["course"] == course]
        filename = f"{course}_{date}.xlsx".replace(" ", "_")
        df_course.to_excel(filename, index=False)
    conn.close()
    messagebox.showinfo("Report Generated", "Daily course-wise report generated.")

# GUI Setup
root = tk.Tk()
root.title("Student Registration System")
root.geometry("600x400")
root.resizable(False, False)

# Styling for label width
label_width = 15

# Name
tk.Label(root, text="Full Name:", width=label_width, anchor='w').grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root, width=30)
entry_name.grid(row=0, column=1, padx=10, pady=5)

# Email
tk.Label(root, text="Email:", width=label_width, anchor='w').grid(row=1, column=0, padx=10, pady=5)
entry_email = tk.Entry(root, width=30)
entry_email.grid(row=1, column=1, padx=10, pady=5)

# Mobile
tk.Label(root, text="Mobile No.:", width=label_width, anchor='w').grid(row=2, column=0, padx=10, pady=5)
entry_mobile = tk.Entry(root, width=30)
entry_mobile.grid(row=2, column=1, padx=10, pady=5)

# Gender
tk.Label(root, text="Gender:", width=label_width, anchor='w').grid(row=3, column=0, padx=10, pady=5)
gender_var = tk.StringVar()
frame_gender = tk.Frame(root)
frame_gender.grid(row=3, column=1, padx=10, pady=5, sticky='w')
tk.Radiobutton(frame_gender, text="Male", variable=gender_var, value="Male").pack(side='left')
tk.Radiobutton(frame_gender, text="Female", variable=gender_var, value="Female").pack(side='left')
tk.Radiobutton(frame_gender, text="Other", variable=gender_var, value="Other").pack(side='left')

# Course Dropdown
tk.Label(root, text="Select Course:", width=label_width, anchor='w').grid(row=4, column=0, padx=10, pady=5)
course_options = ["Python", "Full Stack", "Data Science", "AI & ML", "AWS", "DevOps"]
course_var = tk.StringVar(value=course_options[0])
course_combo = ttk.Combobox(root, values=course_options, textvariable=course_var, state="readonly", width=28)
course_combo.grid(row=4, column=1, padx=10, pady=5)

# How did you hear about us? (Checkbuttons)
tk.Label(root, text="How did you hear about us?", width=label_width, anchor='w').grid(row=5, column=0, padx=10, pady=5)
sources_frame = tk.Frame(root)
sources_frame.grid(row=5, column=1, padx=10, pady=5, sticky='w')

sources_labels = ["Reference", "Google", "Banners", "Friends", "Social Media"]
sources_vars = []
for i, label in enumerate(sources_labels):
    var = tk.IntVar()
    cb = tk.Checkbutton(sources_frame, text=label, variable=var)
    cb.grid(row=0, column=i, padx=5)
    sources_vars.append((var, label))

# Buttons Frame
buttons_frame = tk.Frame(root)
buttons_frame.grid(row=6, column=0, columnspan=2, pady=15)

btn_register = tk.Button(buttons_frame, text="Register", command=save_data, width=15)
btn_register.grid(row=0, column=0, padx=10)

btn_clear = tk.Button(buttons_frame, text="Clear", command=clear_fields, width=15)
btn_clear.grid(row=0, column=1, padx=10)

btn_export = tk.Button(buttons_frame, text="Export All to Excel",
                       command=export_all_to_excel, width=20)
btn_export.grid(row=1, column=0, padx=10, pady=5)

btn_report = tk.Button(buttons_frame, text="Generate Daily Report", command=generate_daily_report, width=20)
btn_report.grid(row=1, column=1, padx=10, pady=5)

btn_exit = tk.Button(buttons_frame, text="Exit", command=root.quit, width=15)
btn_exit.grid(row=2, column=0, columnspan=2, pady=10)

# Init DB and start app
init_db()
root.mainloop()
