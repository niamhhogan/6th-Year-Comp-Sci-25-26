"""
Question 5 – Fitness Tracker 

A fitness instructor wants to track the distance (in kilometres) that members of their running club complete each week. 
They use two lists: one for member names and one for their total weekly distance. 

Your program should:
• Use one function to input member names until 'end' or 'End' is entered 
• Use a second function to input distances until -1 is entered 
• Store the data in separate lists 

After inputting the data, the program should:
• Display all names and distances entered 
• Check that the number of names matches the number of distances 
• If not, allow the user to insert the missing name or distance in the correct index position 

Then, your program should calculate and display:
• Each member’s average speed assuming every member ran for 1 hour (e.g. 10 km = 10 km/h) 
• The highest, lowest, and average distance 
• The name of the member who ran the longest and shortest distance 

Add validation to ensure that all distances entered are positive numbers.
"""

#SOLUTION

# Create two empty lists: one for member names and one for weekly distances
member_names = []
weekly_distance = []

# Function to collect member names
def member_names_list():
    while True:
        # Ask user for member name
        name = input("Please enter member name. When finished, type 'end'. ").strip().capitalize()
        # Stop asking when user types 'end'
        if name == "End":
            break
        else:
            member_names.append(name)  # Add name to the list

# Call the function to collect member names
member_names_list()

# Function to collect weekly distances
def weekly_distance_list():
    while True:
        # Ask user for total weekly distance
        distance = int(input("Please enter total weekly distance (in km) ran. When finished type -1. "))
        # Stop asking when user types -1
        if distance == -1:
            break
        # Validation: make sure the number is positive
        elif distance <= 0:
            print("Invalid entry. Distance must be a positive number.")
        else:
            weekly_distance.append(distance)  # Add distance to the list
            
# Call the function to collect weekly distances
weekly_distance_list()

# Display all names and distances entered
print(f"Member names: {member_names}")
print(f"Weekly distance ran: {weekly_distance}")

# Check if there are missing values between the two lists
if len(member_names) > len(weekly_distance):
    print("Distance data missing. Please check the lists")
    # Ask user to enter missing distance and where to place it
    missing_distance = int(input("Please enter the missing distance: "))
    missing_index = int(input("Please enter the index position of the missing value: "))
    weekly_distance.insert(missing_index, missing_distance)
    # Show updated lists
    print("Updated lists:")
    print(f"Member names: {member_names}")
    print(f"Distance ran: {weekly_distance}")
    
if len(member_names) < len(weekly_distance):
    print("Member name missing. Please check the lists")
    # Ask user to enter missing name and where to place it
    missing_name = input("Please enter the missing name: ").capitalize()
    missing_index = int(input("Please enter the index position of the missing value: "))
    member_names.insert(missing_index, missing_name)
    # Show updated lists
    print("Updated lists:")
    print(f"Member names: {member_names}")
    print(f"Distance ran: {weekly_distance}")

# Display each member's average speed (assuming 1 hour = distance in km/h)
print("Member Names - Average Speed")
print("----------------------------")
for i in range(len(member_names)):
    print(f" {member_names[i]} - {weekly_distance[i]} km/h")

# Calculate and display weekly statistics
print("Weekly Statistics:")
print(f"The longest distance ran was: {max(weekly_distance)}km")
print(f"The shortest distance ran was: {min(weekly_distance)}km")

# Calculate average distance rounded to 2 decimal places
average_distance = round((sum(weekly_distance) / len(weekly_distance)), 2)
print(f"The average distance ran was: {average_distance}km")

# Find and display the member who ran the longest distance
longest_distance = max(weekly_distance)
ld_index = weekly_distance.index(longest_distance)
ld_member = member_names[ld_index]
print(f"The member who ran the longest distance is: {ld_member}")

# Find and display the member who ran the shortest distance
shortest_distance = min(weekly_distance)
sd_index = weekly_distance.index(shortest_distance)
sd_member = member_names[sd_index]
print(f"The member who ran the shortest distance is: {sd_member}")
