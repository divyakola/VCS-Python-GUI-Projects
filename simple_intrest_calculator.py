import tkinter as tk
from tkinter import messagebox

# Function to calculate simple interest
def calculate_si():
    try:
        p = float(entry_principal.get())
        r = float(entry_rate.get())
        t = float(entry_time.get())
        si = (p * r * t) / 100
        result.set(f"Simple Interest: ₹{si:.2f}")
    except:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Function to clear inputs
def clear_fields():
    entry_principal.delete(0, tk.END)
    entry_rate.delete(0, tk.END)
    entry_time.delete(0, tk.END)
    result.set("")

# Function to close the app
def close_app():
    root.destroy()

# Main window
root = tk.Tk()
root.title("Simple Interest Calculator")
root.geometry("350x300")
root.resizable(False, False)

# Result variable
result = tk.StringVar()

# UI Components
tk.Label(root, text="Principal Amount (₹):").pack(pady=5)
entry_principal = tk.Entry(root, width=30)
entry_principal.pack(pady=5)

tk.Label(root, text="Rate of Interest (%):").pack(pady=5)
entry_rate = tk.Entry(root, width=30)
entry_rate.pack(pady=5)

tk.Label(root, text="Time (years):").pack(pady=5)
entry_time = tk.Entry(root, width=30)
entry_time.pack(pady=5)

tk.Button(root, text="Calculate", command=calculate_si, width=15).pack(pady=10)
tk.Label(root, textvariable=result, font=("Arial", 12, "bold"), fg="blue").pack(pady=5)

# Buttons for Clear and Exit
frame = tk.Frame(root)
frame.pack(pady=10)
tk.Button(frame, text="Clear", width=10, command=clear_fields).grid(row=0, column=0, padx=10)
tk.Button(frame, text="Close", width=10, command=close_app).grid(row=0, column=1, padx=10)

# Run the app
root.mainloop()
