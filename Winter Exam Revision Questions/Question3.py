"""
Question 3 – Class Temperature Report 
 

Starting Code: 

day = input("Enter the day of the week: ") 
temperature = float(input("Enter the temperature for that day (°C): ")) 
print(day, "temperature:", temperature, "°C") 
 

(i) Modify the code so that it asks the user to enter the temperature for each day of the week using a for loop and stores all values in a list called temperatures. 
 
(ii) Use a second list called days containing the names of the days of the week. 
 
(iii) Validate that each temperature entered is between -20 and 50. If not, display "Invalid temperature" and ask again. 
 
(iv) After all temperatures are entered, calculate and display: 
• The average weekly temperature (rounded to one decimal place) 
• The highest and lowest temperatures 
• The day that had the highest and lowest temperature (using .index()) 
 
(v) Add an if–elif–else statement to describe the week: 
• Average above 20 → "Warm week" 
• Average between 10 and 20 → "Mild week" 
• Average below 10 → "Cold week" 
 
(vi) Add comments to explain each section of your code. 
 
(vii) Test your program with sample values to ensure it works correctly and displays the correct results. 

 """

#SOLUTION


# Create an empty list to store the days
days = []

# Create an empty list to store temperatures
temperatures = []

#generate list of days from user
while True:
    day=input("Enter the day of the week. When finished type 'end': ").capitalize().strip()
    if day=="End":
        break
    else:
        days.append(day)

# Loop through each day to collect temperature input
for i in range(len(days)):
    temp = float(input(f"Enter the temperature for {days[i]} (°C): "))

    # Validate that temperature is between -20 and 50
    while temp < -20 or temp > 50:
        print("Invalid temperature. Please enter a value between -20 and 50.")
        temp = float(input(f"Enter the temperature for {day} (°C): "))

    # Add valid temperature to the list
    temperatures.append(temp)

# Calculate statistics
average_temp = round(sum(temperatures) / len(temperatures), 1)
highest_temp = max(temperatures)
lowest_temp = min(temperatures)

# Find which day had the highest and lowest temperature
highest_day = days[temperatures.index(highest_temp)]
lowest_day = days[temperatures.index(lowest_temp)]

# Display the weekly report
print("\nClass Temperature Report")
print("-------------------------")
for i in range(len(days)):
    print(f"{days[i]}: {temperatures[i]}°C")

# Display summary statistics
print("\nWeekly Summary")
print(f"Average temperature: {average_temp}°C")
print(f"Highest temperature: {highest_temp}°C on {highest_day}")
print(f"Lowest temperature: {lowest_temp}°C on {lowest_day}")

# Describe the week based on average temperature
if average_temp > 20:
    print("Warm week")
elif average_temp >= 10:
    print("Mild week")
else:
    print("Cold week")


 
