import tkinter as tk
from tkinter import messagebox
import math

def update_inputs(*args):
    for widget in input_frame.winfo_children():
        widget.destroy()

    global length_entry, width_entry  

    shape = shape_var.get()
    
    if shape == "Rectangle":
        create_label_entry("Length:", 0)
        create_label_entry("Width:", 1)

    elif shape == "Square":
        create_label_entry("Side Length:", 0)

    elif shape == "Circle":
        create_label_entry("Radius:", 0)

    elif shape == "Triangle":
        create_label_entry("Side A:", 0)
        create_label_entry("Side B:", 1)
        create_label_entry("Side C:", 2)

    update_mode_menu()

def create_label_entry(label, row):
    tk.Label(input_frame, text=label, fg="white", bg="#1E1E1E", font=("Arial", 12)).grid(row=row, column=0, padx=5, pady=5)
    entry = tk.Entry(input_frame, font=("Arial", 12), bg="#333", fg="white", bd=0, insertbackground="white")
    entry.grid(row=row, column=1, padx=5, pady=5)
    return entry

def update_mode_menu():
    for widget in mode_frame.winfo_children():
        widget.destroy()

    tk.Label(mode_frame, text="Select Mode:", fg="white", bg="#1E1E1E", font=("Arial", 12)).pack(pady=5)

    mode_options = ["Circumference", "Area"] if shape_var.get() == "Circle" else ["Perimeter", "Area"]
    
    mode_menu = tk.OptionMenu(mode_frame, mode_var, *mode_options)
    mode_menu.config(font=("Arial", 12), bg="#333", fg="white", bd=0, relief="flat", activebackground="#444")
    mode_menu.pack(pady=5)

    mode_var.set(mode_options[0])

def calculate():
    shape = shape_var.get()
    mode = mode_var.get()
    formula = ""

    try:
        if shape == "Rectangle":
            length = float(input_frame.winfo_children()[1].get())
            width = float(input_frame.winfo_children()[3].get())
            if mode == "Perimeter":
                result = 2 * (length + width)
                formula = "Perimeter = 2 × (Length + Width)"
            else:
                result = length * width
                formula = "Area = Length × Width"

        elif shape == "Square":
            length = float(input_frame.winfo_children()[1].get())
            if mode == "Perimeter":
                result = 4 * length
                formula = "Perimeter = 4 × Side"
            else:
                result = length ** 2
                formula = "Area = Side²"

        elif shape == "Triangle":
            side_a = float(input_frame.winfo_children()[1].get())
            side_b = float(input_frame.winfo_children()[3].get())
            side_c = float(input_frame.winfo_children()[5].get())

            if mode == "Perimeter":
                result = side_a + side_b + side_c
                formula = "Perimeter = Side A + Side B + Side C"
            else:
                s = (side_a + side_b + side_c) / 2
                result = math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))
                formula = "Area = √[s(s-a)(s-b)(s-c)], where s = (a+b+c)/2"

        elif shape == "Circle":
            radius = float(input_frame.winfo_children()[1].get())
            if mode == "Circumference":
                result = 2 * math.pi * radius
                formula = "Circumference = 2π × Radius"
            else:
                result = math.pi * (radius ** 2)
                formula = "Area = π × Radius²"

        result_label.config(text=f"Result: {result:.2f}")
        formula_label.config(text=f"Formula: {formula}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values!")

root = tk.Tk()
root.title("Peria")
root.geometry("350x520")
root.configure(bg="#1E1E1E")
root.resizable(False, False)

tk.Label(root, text="Select Shape:", fg="white", bg="#1E1E1E", font=("Arial", 12)).pack(pady=5)
shape_var = tk.StringVar()
shape_var.set("Rectangle")

shape_options = ["Rectangle", "Square", "Triangle", "Circle"]
shape_menu = tk.OptionMenu(root, shape_var, *shape_options, command=update_inputs)
shape_menu.config(font=("Arial", 12), bg="#333", fg="white", bd=0, relief="flat", activebackground="#444")
shape_menu.pack(pady=5)

mode_frame = tk.Frame(root, bg="#1E1E1E")
mode_frame.pack()

mode_var = tk.StringVar()
update_mode_menu()

input_frame = tk.Frame(root, bg="#1E1E1E")
input_frame.pack(pady=10)

def on_enter(e):
    e.widget.config(bg="#444")

def on_leave(e):
    e.widget.config(bg="#1976D2" if e.widget.cget("text") == "Calculate" else "#333")

calculate_button = tk.Button(root, text="Calculate", font=("Arial", 14, "bold"), fg="white", 
                             bg="#1976D2", bd=0, relief="flat", padx=20, pady=10, activebackground="#005BB5",
                             command=calculate)
calculate_button.pack(pady=10)
calculate_button.bind("<Enter>", on_enter)
calculate_button.bind("<Leave>", on_leave)

result_label = tk.Label(root, text="Result: ", fg="white", bg="#1E1E1E", font=("Arial", 14))
result_label.pack(pady=5)

formula_label = tk.Label(root, text="Formula: ", fg="white", bg="#1E1E1E", font=("Arial", 12), wraplength=320)
formula_label.pack(pady=5)

credit_label = tk.Label(root, text="Made by ARG Studios", fg="gray", bg="#1E1E1E", font=("Arial", 10))
credit_label.pack(side="bottom", pady=10)

update_inputs()
root.mainloop()
