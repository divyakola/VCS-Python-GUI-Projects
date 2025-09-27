import tkinter as tk
from tkinter import messagebox

# Prices (can be modified easily)
prices = {
    'idli': 10,
    'dosa': 30,
    'meals': 80,
    'biryani': 120,
    'samosa': 15,
    'pakoda': 25,
    'tea': 10,
    'coffee': 15,
    'juice': 30
}

# Function to calculate total
def calculate_total():
    try:
        total = (
            var_idli.get() * prices['idli'] +
            var_dosa.get() * prices['dosa'] +
            var_meals.get() * prices['meals'] +
            var_biryani.get() * prices['biryani'] +
            var_samosa.get() * prices['samosa'] +
            var_pakoda.get() * prices['pakoda'] +
            var_tea.get() * prices['tea'] +
            var_coffee.get() * prices['coffee'] +
            var_juice.get() * prices['juice']
        )
        result.set(f"Total Bill: ₹{total:.2f}")
    except:
        messagebox.showerror("Error", "Invalid Input")

# Clear all fields
def clear_all():
    var_idli.set(0)
    var_dosa.set(0)
    var_meals.set(0)
    var_biryani.set(0)
    var_samosa.set(0)
    var_pakoda.set(0)
    var_tea.set(0)
    var_coffee.set(0)
    var_juice.set(0)
    result.set("")

# Exit the app
def close_app():
    root.destroy()

# GUI Window
root = tk.Tk()
root.title("Restaurant Billing System")
root.geometry("500x600")
root.resizable(False, False)

# Result variable
result = tk.StringVar()

# IntVars for items
var_idli = tk.IntVar()
var_dosa = tk.IntVar()
var_meals = tk.IntVar()
var_biryani = tk.IntVar()
var_samosa = tk.IntVar()
var_pakoda = tk.IntVar()
var_tea = tk.IntVar()
var_coffee = tk.IntVar()
var_juice = tk.IntVar()

# Section: Tiffins
tk.Label(root, text="Tiffins", font=("Arial", 12, "bold")).pack()
tk.Label(root, text="Idli (₹10)").pack()
tk.Entry(root, textvariable=var_idli).pack()
tk.Label(root, text="Dosa (₹30)").pack()
tk.Entry(root, textvariable=var_dosa).pack()

# Section: Lunch
tk.Label(root, text="Lunch", font=("Arial", 12, "bold")).pack(pady=5)
tk.Label(root, text="Meals (₹80)").pack()
tk.Entry(root, textvariable=var_meals).pack()
tk.Label(root, text="Biryani (₹120)").pack()
tk.Entry(root, textvariable=var_biryani).pack()

# Section: Snacks
tk.Label(root, text="Snacks", font=("Arial", 12, "bold")).pack(pady=5)
tk.Label(root, text="Samosa (₹15)").pack()
tk.Entry(root, textvariable=var_samosa).pack()
tk.Label(root, text="Pakoda (₹25)").pack()
tk.Entry(root, textvariable=var_pakoda).pack()

# Section: Drinks
tk.Label(root, text="Drinks", font=("Arial", 12, "bold")).pack(pady=5)
tk.Label(root, text="Tea (₹10)").pack()
tk.Entry(root, textvariable=var_tea).pack()
tk.Label(root, text="Coffee (₹15)").pack()
tk.Entry(root, textvariable=var_coffee).pack()
tk.Label(root, text="Juice (₹30)").pack()
tk.Entry(root, textvariable=var_juice).pack()

# Total Display
tk.Label(root, textvariable=result, font=("Arial", 14, "bold"), fg="blue").pack(pady=10)

# Buttons Frame
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Calculate", width=12, command=calculate_total).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Clear", width=12, command=clear_all).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Exit", width=12, command=close_app).grid(row=0, column=2, padx=10)

root.mainloop()
