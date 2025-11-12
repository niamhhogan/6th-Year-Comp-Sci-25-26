"""
Question 4 – Sales Tracker Program 

 
A small business owner wants to keep track of their weekly sales. To do this, they use two lists: one for product names and another for the total number of items sold each week. 
 
Your program should use a function to ask the user to input the product names until a value of 'end' or 'End' is entered. 
 
The program should use a separate function to ask the user to input numeric sales figures until a value of -1 is entered. 
 
Product names and sales figures should both be stored in separate lists. 
 
After all the names and sales have been entered, the program should display the entered products and sales figures. 
 
The program should also check if the number of products entered matches the number of sales figures entered. 
 
If they do not match, the program should allow the user to enter the missing product name or sales figure at the correct index position. 
 
Finally, the program should: 
• Find the highest and lowest number of items sold 
• Find the average number of items sold 
• Display the name of the product with the highest and lowest sales 
 
You may assume that each product’s sales figure represents one week of data.
"""

#SOLUTION

#create empty lists to store inputs
product_names = []
weekly_sales = []

# Function to collect product names 
def get_product_names():
    while True:
        name = input("Enter product name (or type 'end' to finish): ").strip().capitalize()
        if name == "End":
            break
        else:
            product_names.append(name)

#call the function
get_product_names()

# Function to collect weekly sales until -1 is entered (validate > 0)
def get_sales_figures():
    while True:
        figure = int(input("Enter weekly items sold (or -1 to finish): "))
        if figure == -1:
            break
        elif figure <= 0:
            print("Sales must be a positive number.")
            figure = float(input("Enter weekly items sold (or -1 to finish): "))
            if figure == -1:
                break
        else:
            weekly_sales.append(figure) # store as whole number of items

#call the function
get_sales_figures()

# Show what was entered
print("Entered product names:", product_names)
print("Entered weekly sales: ", weekly_sales)


# If the number of names doesn’t match the number of sales, let user insert the missing value
while len(product_names) != len(weekly_sales):
    print("Counts do not match.")
    print(f"Products count: {len(product_names)} | Sales count: {len(weekly_sales)}")
    if len(product_names)>len(weekly_sales):
        print("Weekly sales figure missing")
        missing_figure=int(input("Please enter the missing sales value: "))
        missing_index=int(input("Please enter the index location of the missing value"))
        weekly_sales.insert(missing_index, missing_figure)
        print("Updated lists:")
        print(f"Product names: {product_names}")
        print(f"Weekly sales: {weekly_sales}")

    
    elif len(weekly_sales)>len(product_names):
        print("Product name missing")
        missing_name=input("Please enter the missing product name: ").strip().capitalize()
        missing_index=int(input("Please enter the index location of the missing value"))
        product_names.insert(missing_index, missing_name)
        print("Updated lists:")
        print(f"Product names: {product_names}")
        print(f"Weekly sales: {weekly_sales}")

 
# Final display of paired data
print("\nSales Summary (Product : Items Sold)")
for i in range(len(product_names)):
    print(f"{product_names[i]} : {weekly_sales[i]}")

# If there is data, compute and display statistics
if len(product_names) > 0:
    highest = max(weekly_sales)
    lowest = min(weekly_sales)
    average = round(sum(weekly_sales) / len(weekly_sales), 2)

    product_highest = product_names[weekly_sales.index(highest)]
    product_lowest = product_names[weekly_sales.index(lowest)]

    print("\nWeekly Statistics")
    print(f"Highest items sold: {highest} ({product_highest})")
    print(f"Lowest  items sold: {lowest} ({product_lowest})")
    print(f"Average items sold: {average}")
else:
    print("\nNo data to analyse.")
