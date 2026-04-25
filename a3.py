import matplotlib.pyplot as plt

students_names =["Wasim", "Rahul", "Karan", "Wasim", "Ramesh", "Ajay", "Sartaj",
    "Priya"]
students_marks = [35,50,20,45,25,40,25,40]

mark_perc = []
for x in students_marks:
    res  = (x/50)*100
    mark_perc.append(res)

print(mark_perc)

def marks_line_chart():
  plt.plot(students_names,students_marks)
  plt.title("students marks graph")
  plt.xlabel("Students Names")
  plt.ylabel("Students Marks")
  plt.show()

marks_line_chart()  

def percentage_bar_chart():
  plt.bar(students_names,students_perc)
  plt.title("Students percentage graph") 
  plt.xlabel("Students Names")
  plt.ylabel("Students Percentage")
  plt.show()           

percentage_bar_chart()  