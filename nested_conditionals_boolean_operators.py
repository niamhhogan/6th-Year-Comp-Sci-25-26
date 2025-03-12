#Nested conditional = condition inside a condition

#Competition entry check
print("Competition entry eligibility checker: ")
age=int(input("What is your age? "))
resident_country=input("Are you a resident of the ROI?: (y/n) ").strip().lower()
if age >=18:
    if resident_country=="y":
        print("You are eligible to enter the competition")
    else:
        print("You are not eligible to enter the competition")
else:
    print("You are not eligible to enter the competition, you must be 18 years or older")
    

#boolean operators with conditionals
print("Car pollution level checker: ")
car_age=int(input("Enter age of car: "))
car_fuel=input("Enter car's fuel type: (petrol/diesel) ").strip().lower()
if car_age >=10 or car_fuel =="diesel":
    print("Pollution level: high")
else:
    print("Pollution level: low")
    
#Task: rewrite the competition enter checker using boolean operator
    