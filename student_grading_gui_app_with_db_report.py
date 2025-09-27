import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import csv
import os
import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Initialize DB
def init_db():
    conn = sqlite3.connect("student_results.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            sub1 REAL, sub2 REAL, sub3 REAL, sub4 REAL, sub5 REAL,
            total REAL, percentage REAL, grade TEXT
        )
    """)
    conn.commit()
    conn.close()

# Save to DB
def save_to_db():
    name = entry_name.get()
    try:
        marks = [float(entry.get()) for entry in entries]
        total = sum(marks)
        percent = total / 5
        grade = calculate_grade(percent)

        conn = sqlite3.connect("student_results.db")
        c = conn.cursor()
        c.execute("INSERT INTO results (name, sub1, sub2, sub3, sub4, sub5, total, percentage, grade) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                  (name, *marks, total, percent, grade))
        conn.commit()
        conn.close()
        messagebox.showinfo("Saved", "Result saved to database.")
    except:
        messagebox.showerror("Error", "Check all fields before saving.")

# Export to CSV
def export_to_csv():
    name = entry_name.get()
    try:
        marks = [float(entry.get()) for entry in entries]
        total = sum(marks)
        percent = total / 5
        grade = calculate_grade(percent)

        file_exists = os.path.isfile('results.csv')
        with open('results.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(['Name', 'Sub1', 'Sub2', 'Sub3', 'Sub4', 'Sub5', 'Total', 'Percentage', 'Grade'])
            writer.writerow([name, *marks, total, percent, grade])
        messagebox.showinfo("Exported", "Result exported to results.csv")
    except:
        messagebox.showerror("Error", "Check inputs before exporting.")

# Export to Excel
def export_to_excel():
    try:
        conn = sqlite3.connect("student_results.db")
        df = pd.read_sql_query("SELECT * FROM results", conn)
        conn.close()
        df.to_excel("student_results.xlsx", index=False)
        messagebox.showinfo("Success", "Data exported to student_results.xlsx")
    except Exception as e:
        messagebox.showerror("Export Error", str(e))

# Generate PDF
def generate_pdf_marksheet():
    name = entry_name.get()
    try:
        marks = [float(entry.get()) for entry in entries]
        total = sum(marks)
        percent = total / 5
        grade = calculate_grade(percent)

        filename = f"{name}_marksheet.pdf"
        c = canvas.Canvas(filename, pagesize=A4)
        c.setFont("Helvetica-Bold", 16)
        c.drawString(200, 780, "Student Marksheet")
        c.setFont("Helvetica", 12)

        c.drawString(100, 740, f"Name: {name}")
        for i, mark in enumerate(marks):
            c.drawString(100, 710 - i * 20, f"Subject {i+1}: {mark}")
        c.drawString(100, 600, f"Total: {total}/500")
        c.drawString(100, 580, f"Percentage: {percent:.2f}%")
        c.drawString(100, 560, f"Grade: {grade}")

        c.save()
        messagebox.showinfo("PDF Created", f"Marksheet saved as {filename}")
    except:
        messagebox.showerror("Error", "Please enter valid inputs first.")

# View Saved Records
def view_records():
    view_win = tk.Toplevel(root)
    view_win.title("Saved Records")
    view_win.geometry("850x300")

    tree = ttk.Treeview(view_win, columns=('ID', 'Name', 'Sub1', 'Sub2', 'Sub3', 'Sub4', 'Sub5', 'Total', 'Percentage', 'Grade'), show='headings')
    tree.pack(fill=tk.BOTH, expand=True)

    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, width=80)

    conn = sqlite3.connect("student_results.db")
    c = conn.cursor()
    c.execute("SELECT * FROM results")
    rows = c.fetchall()
    conn.close()

    for row in rows:
        tree.insert("", tk.END, values=row)

# Grade Logic
def calculate_grade(percent):
    if percent >= 90:
        return 'A+'
    elif percent >= 80:
        return 'A'
    elif percent >= 70:
        return 'B'
    elif percent >= 60:
        return 'C'
    elif percent >= 50:
        return 'D'
    else:
        return 'F'

# Clear all inputs
def clear_fields():
    entry_name.delete(0, tk.END)
    for entry in entries:
        entry.delete(0, tk.END)

def close():
    root.destroy()
    
# GUI Setup
root = tk.Tk()
root.title("Student Grading System")
root.geometry("400x600")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Student Grading System", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

tk.Label(root, text="Student Name:", bg="#f0f0f0").pack()
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

entries = []
for i in range(1, 6):
    tk.Label(root, text=f"Subject {i} Marks:", bg="#f0f0f0").pack()
    entry = tk.Entry(root)
    entry.pack(pady=3)
    entries.append(entry)

# Buttons
tk.Button(root, text="Save to DB", command=save_to_db, width=25).pack(pady=5)
tk.Button(root, text="Export to CSV", command=export_to_csv, width=25).pack(pady=5)
tk.Button(root, text="Export to Excel", command=export_to_excel, width=25).pack(pady=5)
tk.Button(root, text="Generate PDF Marksheet", command=generate_pdf_marksheet, width=25).pack(pady=5)
tk.Button(root, text="View Saved Records", command=view_records, width=25).pack(pady=5)
tk.Button(root, text="Clear", command=clear_fields, width=25).pack(pady=5)
tk.Button(root, text="Exit", command=close, width=25).pack(pady=10)

init_db()
root.mainloop()
