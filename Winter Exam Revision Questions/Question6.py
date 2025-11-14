""
Question 6 – Electricity Bill Calculator 
 
An energy company wants to calculate monthly electricity bills for its customers. Each customer’s name and electricity usage (in kWh) are stored in separate lists. 
Create a program that allows the company to enter this information and analyse the data. 
 
Your program should: 
• Use one function to input customer names until 'end' or 'End' is entered 
• Use a second function to input electricity usage (in kWh) until -1 is entered 
• Store the information in separate lists 
 
After all data is entered, the program should: 
• Display both lists 
• Check that the number of names matches the number of usage values 
• If they don’t match, allow the user to insert the missing value at the correct index position 
 
The company charges customers based on the following rates: 
• Up to 150 kWh → €0.20 per kWh 
• 151–300 kWh → €0.25 per kWh 
• Above 300 kWh → €0.30 per kWh 
 
Your program should: 
• Calculate and store the cost for each customer in a new list called bills 
• Display each customer’s name and bill amount rounded to two decimal places using f-strings 
• Find and display: 

The highest and lowest bill 

The average bill amount 

The customer with the highest and lowest usage 
Add validation to ensure that no negative usage values are entered.
"""

#SOLUTION

#part (i): This program collects customer electricity usage, calculates their bills, and analyses the results

# Student name:

customer_names = []
usage_list = []
bills = []

#part (ii): input customer names using while True and stop at 'end'
def input_names():
    while True:
        name = input("Enter customer name (or 'end' to finish): ").strip().capitalize()
        if name.lower() == "end":
            break
        customer_names.append(name)

#part (iii): input usage values using while True and stop at -1
def input_usage():
    customer_number = 1
    while True:
        usage = float(input(f"Enter electricity usage for customer {customer_number} (or -1 to finish): "))
        if usage == -1:
            break
        if usage < 0:
            print("Invalid entry. Usage cannot be negative.")
        else:
            usage_list.append(usage)
            customer_number += 1

#call the functions
input_names()
input_usage()

#part (iv): display both lists
print("\nCustomer Names:")
print(customer_names)
print("Electricity Usage (kWh):")
print(usage_list)

#part (v): ensure both lists match in length using while True
while True:
    if len(customer_names) == len(usage_list):
        break

    print("\nThe number of names does not match the number of usage values.")
    print(f"Names: {len(customer_names)}, Usage values: {len(usage_list)}")

    if len(customer_names) > len(usage_list):
        print("A usage value is missing.")
        index = int(input("Enter the index where the missing usage should be inserted: "))
        new_usage = float(input("Enter the missing usage value: "))
        while new_usage < 0:
            print("Usage cannot be negative.")
            new_usage = float(input("Enter the missing usage value: "))
        usage_list.insert(index, new_usage)

    else:
        print("A customer name is missing.")
        index = int(input("Enter the index where the missing name should be inserted: "))
        new_name = input("Enter the missing customer name: ").strip().capitalize()
        customer_names.insert(index, new_name)

    print("\nUpdated Customer Names:")
    print(customer_names)
    print("Updated Usage List:")
    print(usage_list)

#if no customers, end program
if len(customer_names) == 0:
    print("\nNo data entered. Program ending.")
else:
    #part (vi): calculate bills and store in a list
    for usage in usage_list:
        if usage <= 150:
            rate = 0.20
        elif usage <= 300:
            rate = 0.25
        else:
            rate = 0.30
        
        bill = usage * rate
        bill = round(bill, 2)
        bills.append(bill)

    #part (vii): display customer names with bills
    print("\nCustomer Bills:")
    for i in range(len(customer_names)):
        print(f"{customer_names[i]}: €{bills[i]}")

    #part (viii): analysis findings
    highest_bill = round(max(bills), 2)
    lowest_bill = round(min(bills), 2)
    average_bill = round(sum(bills) / len(bills), 2)

    highest_usage = max(usage_list)
    lowest_usage = min(usage_list)

    index_highest_usage = usage_list.index(highest_usage)
    index_lowest_usage = usage_list.index(lowest_usage)

    customer_highest_usage = customer_names[index_highest_usage]
    customer_lowest_usage = customer_names[index_lowest_usage]

    print("\nBill Analysis:")
    print(f"Highest bill: €{highest_bill}")
    print(f"Lowest bill: €{lowest_bill}")
    print(f"Average bill amount: €{average_bill}")
    print(f"Customer with highest usage: {customer_highest_usage} ({highest_usage} kWh)")
    print(f"Customer with lowest usage: {customer_lowest_usage} ({lowest_usage} kWh)")

