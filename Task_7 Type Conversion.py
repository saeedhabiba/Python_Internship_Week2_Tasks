#Create a marks percentage calculator:
#Ask user to input marks for 5 subjects (input as strings) , Convert them to integers
#let's use while loop to save time and make our code interesting one
total_marks = 0
count = 1

while count <=5:
    marks = float(input(f" Enter marks for subject {count}: "))
    total_marks += marks
    count+= 1

#Calculate the total and percentage
percentage = total_marks / 500 * 100
print(percentage)

#Print percentage along with a grade: A (90+), B (80-89), C (70-79), Fail (<70)
#we will use IF/ELSE statments
if percentage >=90:
    print("Grade A")
elif percentage >=80:
    print("Grade B")
elif percentage >=70:
    print("Grade C")
else:
     print("Fail")