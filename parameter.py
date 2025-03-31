import tkinter as tk
from tkinter import ttk, messagebox
import math

def update_inputs(*args):
    for widget in input_frame.winfo_children():
        widget.destroy()

    global length_entry, width_entry  

    shape = shape_var.get()
    
    if shape in ["Rectangle", "Triangle"]:
        ttk.Label(input_frame, text="Length/Base:").grid(row=0, column=0)
        length_entry = ttk.Entry(input_frame)
        length_entry.grid(row=0, column=1)

        ttk.Label(input_frame, text="Width/Height:").grid(row=1, column=0)
        width_entry = ttk.Entry(input_frame)
        width_entry.grid(row=1, column=1)

    elif shape == "Square" or shape == "Circle":
        ttk.Label(input_frame, text="Side Length (or Radius for Circle):").grid(row=0, column=0)
        length_entry = ttk.Entry(input_frame)
        length_entry.grid(row=0, column=1)

    if shape == "Circle":
        mode_menu["values"] = ["Circumference", "Area"]
        mode_var.set("Circumference")
    else:
        mode_menu["values"] = ["Perimeter", "Area"]
        mode_var.set("Perimeter")

def calculate():
    shape = shape_var.get()
    mode = mode_var.get()

    try:
        if shape == "Rectangle":
            length = float(length_entry.get())
            width = float(width_entry.get())
            result = 2 * (length + width) if mode == "Perimeter" else length * width

        elif shape == "Square":
            length = float(length_entry.get())
            result = 4 * length if mode == "Perimeter" else length ** 2

        elif shape == "Triangle":
            base = float(length_entry.get())
            height = float(width_entry.get())
            if mode == "Perimeter":
                messagebox.showerror("Error", "Perimeter requires 3 sides for a triangle!")
                return
            result = 0.5 * base * height

        elif shape == "Circle":
            radius = float(length_entry.get())
            result = 2 * math.pi * radius if mode == "Circumference" else math.pi * (radius ** 2)

        result_label.config(text=f"Result: {result:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values!")

root = tk.Tk()
root.title("Shape Calculator")
root.geometry("400x350")

ttk.Label(root, text="Select Shape:").pack()
shape_var = tk.StringVar()
shape_var.set("Rectangle")
shape_menu = ttk.Combobox(root, textvariable=shape_var, values=["Rectangle", "Square", "Triangle", "Circle"], state="readonly")
shape_menu.pack()
shape_menu.bind("<<ComboboxSelected>>", update_inputs)

ttk.Label(root, text="Select Mode:").pack()
mode_var = tk.StringVar()
mode_var.set("Perimeter")
mode_menu = ttk.Combobox(root, textvariable=mode_var, values=["Perimeter", "Area"], state="readonly")
mode_menu.pack()

input_frame = ttk.Frame(root)
input_frame.pack(pady=10)

calculate_button = ttk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(pady=10)

result_label = ttk.Label(root, text="Result: ", font=("Arial", 12))
result_label.pack()

credit_label = ttk.Label(root, text="Made by ARG Studios", font=("Arial", 10, "italic"))
credit_label.pack(side="bottom", pady=5)

update_inputs()
root.mainloop()
