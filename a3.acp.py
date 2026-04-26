import matplotlib.pyplot as plt

students_names = ["sanjay", "rahul", "karan", "wasim", "ramesh", "ajay", "sartaj", "priya"]
students_marks = [35, 50, 20, 45, 25, 40, 30, 48]

mark_perc = []
for x in students_marks:
    res = (x / 50) * 100
    mark_perc.append(res)

def mark_line_chart():
    plt.plot(students_names, students_marks)
    plt.title("Students Marks Graph")
    plt.xlabel("Students Names")
    plt.ylabel("Students Marks")
    plt.show()

def percentage_bar_chart():
    plt.bar(students_names, mark_perc)
    plt.title("Students Percentage Graph")
    plt.xlabel("Students Names")
    plt.ylabel("Student Percentage")
    plt.show()

mark_line_chart()
percentage_bar_chart()