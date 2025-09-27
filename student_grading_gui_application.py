import tkinter as tk
from tkinter import messagebox

# Grade calculation logic
def calculate_grade():
    try:
        name = entry_name.get()
        m1 = float(entry_sub1.get())
        m2 = float(entry_sub2.get())
        m3 = float(entry_sub3.get())
        m4 = float(entry_sub4.get())
        m5 = float(entry_sub5.get())

        total = m1 + m2 + m3 + m4 + m5
        percent = total / 5

        # Grade assignment
        if percent >= 90:
            grade = 'A+'
        elif percent >= 80:
            grade = 'A'
        elif percent >= 70:
            grade = 'B'
        elif percent >= 60:
            grade = 'C'
        elif percent >= 50:
            grade = 'D'
        else:
            grade = 'F'

        result.set(f"Student: {name}\nTotal: {total}/500\nPercentage: {percent:.2f}%\nGrade: {grade}")
    except:
        messagebox.showerror("Input Error", "Please enter valid numeric marks.")

# Clear fields
def clear_fields():
    entry_name.delete(0, tk.END)
    entry_sub1.delete(0, tk.END)
    entry_sub2.delete(0, tk.END)
    entry_sub3.delete(0, tk.END)
    entry_sub4.delete(0, tk.END)
    entry_sub5.delete(0, tk.END)
    result.set("")

# Exit application
def close_app():
    root.destroy()

# Main window
root = tk.Tk()
root.title("Student Grading System")
root.geometry("400x500")
root.resizable(False, False)

result = tk.StringVar()

# UI layout
tk.Label(root, text="Student Grading System", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Student Name:").pack()
entry_name = tk.Entry(root, width=30)
entry_name.pack(pady=5)

tk.Label(root, text="Subject 1 Marks:").pack()
entry_sub1 = tk.Entry(root, width=30)
entry_sub1.pack(pady=2)

tk.Label(root, text="Subject 2 Marks:").pack()
entry_sub2 = tk.Entry(root, width=30)
entry_sub2.pack(pady=2)

tk.Label(root, text="Subject 3 Marks:").pack()
entry_sub3 = tk.Entry(root, width=30)
entry_sub3.pack(pady=2)

tk.Label(root, text="Subject 4 Marks:").pack()
entry_sub4 = tk.Entry(root, width=30)
entry_sub4.pack(pady=2)

tk.Label(root, text="Subject 5 Marks:").pack()
entry_sub5 = tk.Entry(root, width=30)
entry_sub5.pack(pady=2)

tk.Button(root, text="Calculate Grade", command=calculate_grade, width=20).pack(pady=10)
tk.Label(root, textvariable=result, font=("Arial", 12), fg="blue").pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)
tk.Button(frame, text="Clear", width=10, command=clear_fields).grid(row=0, column=0, padx=10)
tk.Button(frame, text="Exit", width=10, command=close_app).grid(row=0, column=1, padx=10)

root.mainloop()
