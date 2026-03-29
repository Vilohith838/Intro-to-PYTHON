import tkinter as tk
from datetime import datetime

def calculate_age():
    try:
        d = int(day_entry.get())
        m = int(month_entry.get())
        y = int(year_entry.get())
        birth_date = datetime(y, m, d)
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        result_label.config(text="Age: " + str(age))
    except:
        result_label.config(text="Invalid input")

root = tk.Tk()
root.title("Age Calculator")

tk.Label(root, text="Day").grid(row=0, column=0)
tk.Label(root, text="Month").grid(row=1, column=0)
tk.Label(root, text="Year").grid(row=2, column=0)

day_entry = tk.Entry(root)
month_entry = tk.Entry(root)
year_entry = tk.Entry(root)

day_entry.grid(row=0, column=1)
month_entry.grid(row=1, column=1)
year_entry.grid(row=2, column=1)

tk.Button(root, text="Calculate Age", command=calculate_age).grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()