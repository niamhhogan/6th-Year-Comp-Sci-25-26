"""6th Year Computer Science – Programming Practice Questions 

Question 1 – Fuel Efficiency Calculator 
 
Starting Code: 

car_model = input("Please enter the car model: ") 
fuel_used = float(input("Please enter the amount of fuel used (in litres): ")) 
distance_travelled = float(input("Please enter the distance travelled (in km): ")) 
efficiency = (distance_travelled / fuel_used) 
print(car_model, "has a fuel efficiency of", efficiency, "km per litre") 
 

(i) Modify the code so that: 
• The program greets the user by their name before asking for any inputs. 
• Use a function called welcome() to do this. 
• Use an f-string in your print statement. 
 
(ii) Ask the user to enter the car model, fuel used, and distance travelled, and round the fuel efficiency to one decimal place. 
 
(iii) Add validation so that if fuel_used or distance_travelled is less than or equal to zero, print "Invalid entry". Otherwise, calculate and display the efficiency as before. 
 
(iv) Add an if–elif–else statement to display a rating based on the fuel efficiency: 
• Above 20 → "Excellent efficiency" 
• Between 10 and 20 → "Average efficiency" 
• Below 10 → "Poor efficiency" 
 
(v) Add comments # to explain what each section of your code does. 
 
(vi) Test your program with sample values to ensure it works correctly and handles invalid data.
"""

#SOLUTION
# Function to greet the user by name
def welcome():
    name = input("Please enter your name: ")
    print(f"Welcome, {name}! Let's calculate your car's fuel efficiency.\n")

# Call the welcome function
welcome()

# Ask the user to input car details
car_model = input("Please enter the car model: ")

# Ask for fuel used and distance travelled, convert to float
fuel_used = float(input("Please enter the amount of fuel used (in litres): "))
distance_travelled = float(input("Please enter the distance travelled (in km): "))

# Validate inputs to make sure values are greater than zero
if fuel_used <= 0 or distance_travelled <= 0:
    print("Invalid entry.")
else:
    # Calculate fuel efficiency
    efficiency = round(distance_travelled / fuel_used, 1)
    print(f"{car_model} has a fuel efficiency of {efficiency} km per litre.")

    # Determine rating based on efficiency value
    if efficiency > 20:
        print("Efficiency rating: Excellent efficiency.")
    elif efficiency >= 10:
        print("Efficiency rating: Average efficiency.")
    else:
        print("Efficiency rating: Poor efficiency.")
