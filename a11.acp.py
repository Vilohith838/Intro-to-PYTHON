import tkinter as tk

def check_strength(*args):
    password = password_var.get()
    length = len(password)
    
    if length == 0:
        result_label.config(text="Strength: None", fg="black")
    elif length < 6:
        result_label.config(text="Strength: Weak", fg="red")
    elif length < 12:
        result_label.config(text="Strength: Medium", fg="orange")
    else:
        result_label.config(text="Strength: Strong", fg="green")

root = tk.Tk()
root.title("Password Checker")
root.geometry("300x200")

password_var = tk.StringVar()
password_var.trace_add("write", check_strength)

tk.Label(root, text="Enter Password:", font=("Arial", 10)).pack(pady=10)

entry = tk.Entry(root, textvariable=password_var, show="*", font=("Arial", 12))
entry.pack(pady=5)

result_label = tk.Label(root, text="Strength: None", font=("Arial", 12, "bold"))
result_label.pack(pady=20)

root.mainloop()