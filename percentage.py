# take marks as input from user
print("enter marks obtained  in 4 subjects:")
maths = int(input("maths: "))
english = int(input("english: "))
science = int(input("science: "))
hindi = int(input("hindi: "))

# lets calculate the percentage of marks
sum = maths+english+science+hindi

perc = (sum/400)*100

print(end = "percentage mark =")
print(perc)