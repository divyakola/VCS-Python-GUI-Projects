import tkinter as tk
from tkinter import messagebox

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height_cm = float(entry_height.get())
        height_m = height_cm / 100  # convert cm to meters
        bmi = weight / (height_m ** 2)
        category = ""

        # BMI Category classification
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        result.set(f"BMI: {bmi:.2f} ({category})")
    except:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Clear fields
def clear_fields():
    entry_weight.delete(0, tk.END)
    entry_height.delete(0, tk.END)
    result.set("")

# Close app
def close_app():
    root.destroy()

# Main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x280")
root.resizable(False, False)

result = tk.StringVar()

# UI Layout
tk.Label(root, text="Enter your Weight (kg):").pack(pady=5)
entry_weight = tk.Entry(root, width=30)
entry_weight.pack(pady=5)

tk.Label(root, text="Enter your Height (cm):").pack(pady=5)
entry_height = tk.Entry(root, width=30)
entry_height.pack(pady=5)

tk.Button(root, text="Calculate BMI", command=calculate_bmi, width=20).pack(pady=10)
tk.Label(root, textvariable=result, font=("Arial", 12, "bold"), fg="green").pack(pady=5)

# Buttons for Clear and Exit
frame = tk.Frame(root)
frame.pack(pady=10)
tk.Button(frame, text="Clear", width=10, command=clear_fields).grid(row=0, column=0, padx=10)
tk.Button(frame, text="Close", width=10, command=close_app).grid(row=0, column=1, padx=10)

# Run the application
root.mainloop()
