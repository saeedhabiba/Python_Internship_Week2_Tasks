#let's design command-line survey 
#name, favorite food, birth year, favorite number, favorite language
name = input("1. May I know your full name? ")
print("oh that's great", name)
food = input("2. What is your favorite food? ")
print("Yum! That's a great choice", food)
birth_year = input("3. Kindly enter your birth year: ")
print("Interesting! Born in", birth_year )
fav_number = input("4. What is your favorite number? ")
print("Nice pick! Number", fav_number )
language = input("5. Which programming language do you prefer the most? ")
print(language,"is an excellent choice for modern development")

#summary
print("\nSURVEY SUMMARY")
print(f" {name} loves eating {food}.")
print(f" Born in {birth_year}, they hold a special liking for the number {fav_number}.")
print(f" When it comes to coding, {language} is their preferred language.")
print("═════════════════════════════════")
print(" Thank you for participating in our survey!")
