#let's create porfolio 
#person 1
name1 = "Muhammad"
profession1 = "Engineer"
country1 = "Pakistan"
is_employed1 = True

#header to show category
print(f"{'Name' :<15} {"profession" :<15} {"Country" :<15} {"is_employed" :<15}")
print("-" * 60) 

#15 prints spaces, str converts BooleanTrue into StringTrue
print(f"{name1 :<15} {profession1 :<15} {country1 :<15} {str (is_employed1 ):<15}")

#person 2
name2 = "Ahmad"
profession2 = "Doctor"
country2 = "Saudia Arabia"
is_employed2 = False
print(f"{name2 :<15} {profession2 :<15} {country2 :<15} {str (is_employed2 ):<15}")

#person 3
name3 = "Abdul Rafay"
profession3 = "Scientist"
country3 = "China"
is_employed3 = True
print(f"{name3 :<15} {profession3:<15} {country3:<15} {str (is_employed3) :<15}")