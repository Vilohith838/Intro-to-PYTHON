from tkinter import *
from datetime import date

root = Tk()
root.title('getting started with widgets')
root.geometry('400x300')


lb1 = Label(text="Hey There!", fg ="white", bg = "#072F5F",
height = 1, width = 300)

name_lb1 = Label(text="Full Nme!", bg = "#3895D3")
name_entry = Entry()

def display():

    name = name_entry.get()

    global Message
    message = "Welcome to the Apllication! \n Today's date is: "
    greet = "Home "+name+"\n"

    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height=3)   

btn = Button(text="Begin", command=display, height=1, 
bg = "#1261A0" , fg="white")

lb1.pack()
name_lb1.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()