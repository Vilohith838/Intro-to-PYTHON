import tkinter as tk

def calculate():
    p = float(principal_entry.get())
    t = float(time_entry.get())
    r = float(rate_entry.get())

    si = (p * t * r) / 100
    ci = p * ((1 + r/100) ** t) - p

    si_result.config(text="Simple Interest: " + str(round(si, 2)))
    ci_result.config(text="Compound Interest: " + str(round(ci, 2)))

root = tk.Tk()
root.title("Interest Calculator")

tk.Label(root, text="Principal").grid(row=0, column=0)
principal_entry = tk.Entry(root)
principal_entry.grid(row=0, column=1)

tk.Label(root, text="Time").grid(row=1, column=0)
time_entry = tk.Entry(root)
time_entry.grid(row=1, column=1)

tk.Label(root, text="Rate").grid(row=2, column=0)
rate_entry = tk.Entry(root)
rate_entry.grid(row=2, column=1)

tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2)

si_result = tk.Label(root, text="")
si_result.grid(row=4, column=0, columnspan=2)

ci_result = tk.Label(root, text="")
ci_result.grid(row=5, column=0, columnspan=2)

root.mainloop()