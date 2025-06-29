#create datatype tester 

fan = input("enter any value  ")
print("Python Guesses Type  ", type(fan))

#let's add some condition to check different cases
try:
     int(fan)
     print("You entered an integer!")
except:
 
 try:
   float(fan)
   print("you entered float")
 except:
   
#try:
#     str(fan)
#    print("you entered string")
#except:
#    print("you entered boolean")

    print("you enterd string")