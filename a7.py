import tkinter as tk

def convert():
    inches = float(entry.get())
    cm = inches * 2.54
    result.config(text=str(cm) + " cm")

root = tk.Tk()
root.title("Inches to Centimeters")

label = tk.Label(root, text="Enter length in inches:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Convert", command=convert)
button.pack()

result = tk.Label(root, text="")
result.pack()

root.mainloop()