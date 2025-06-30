#eligibility for vote
#Enter their year of birth 
print("Let's Check Your Eligibility For Vote")
birth= int(input("Enter Your Birth Year = "))
# Calculate their age (based on current year)
calculate = (2025- birth)
print(calculate)
#for check eligibility we have to apply if-else
if calculate >=18:
   print("Congrats! You Are Eligible For Vote")
else:
   print("Sorry! You Are Not Eligible")
