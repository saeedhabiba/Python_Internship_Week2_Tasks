#Declaring 5 different variables
name = 'Habiba'
age = 21
gpa = 3.5 +1j
semester = 4.0
employed = False

print("Original Values And Types")
print('--------------------------------------------')
print(f"{'Variable':<15} {'Name' :<15} {'Type'}")
print(f"{'Name' :<15} {name :<15} {type(name)}")
print(f"{'Age' :<15} {age :<15} {type(age)}")
print(f"{'GPA' :<15} {gpa :<15} {type(gpa)}")
print(f"{'Semester' :<15} {semester :<15} {type(semester)}")
print(f"{'Employed' :<15} {employed :<15} {type(employed)}")
print()
# Try converting each to a different type
#string conversion
print("CONVERSION OF DATATYPE")
try:
    name_convert= list(name)
    print("name =", name_convert, "| type =", type(name_convert))
except:
    print("sorry can't convert ")
#age
try:
    age_convert = float(age)
    print("age =", age_convert, "| type =", type(age_convert))
except:
    print("sorry can't convert ")
#gpa
try:
    gpa_convert = str(gpa)
    print("gpa =", gpa_convert, "| type =", type(gpa_convert))
except:
    print("sorry can't convert ")
#semester
try:
    semester_convert = int(semester)
    print("semester =", semester_convert, "| type =", type(semester_convert))
except:
    print("sorry can't convert ")
#employed
try:
    employed_convert = float(employed)
    print("employed =", employed_convert, "| type =", type(employed_convert))
except:
    print("sorry can't convert ")

print('---------------------------------------------')
print()

print("Name", name , "\nAge " , age , "\nSemester", semester, " \nGPA", gpa, "\nEmployment status ", employed)

