#TEMPERATURE CONVERTER
#Ask the user to input temperature in Celsius.
print(".........Temperature Converter........")
try:
    celcius = float(input("Enter  temperature in Celsius: "))
#Convert it to Fahrenheit using: F = (C * 9/5) + 32 , 
    fahrenheit = (celcius * 9/5) + 32
    print(f"{celcius}C is equal to {fahrenheit}F ")
except ValueError:
            print("Invalid input! Please enter a numeric value for Celsius.")
# Then reverse: Ask for Fahrenheit, convert it to Celsius.
try:
    fahrenheit_2 = float(input("Enter temperature in Fahrenheit :" )) 
    fahrenheit_reverse = (fahrenheit_2 - 32) * 5/9
    print(f"{fahrenheit_2}F is equal to {fahrenheit_reverse}C ")
except ValueError:
            print("Invalid input! Please enter a numeric value for Fahrenheit.")
#Handle wrong input types using try-except.
