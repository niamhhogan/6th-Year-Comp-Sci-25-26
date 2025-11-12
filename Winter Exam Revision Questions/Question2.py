"""
Question 2 – Shopping Bill Calculator 

Starting Code: 

item_name = input("Please enter the item name: ") 
item_price = float(input("Please enter the item price: ")) 
item_quantity = int(input("Please enter the quantity: ")) 
total_cost = item_price * item_quantity 
print("The total cost is €", total_cost) 

(i) Modify the code so that the program welcomes the user using a function called welcome().
(ii) Use a loop to allow the user to keep entering items until they type 'end'.
(iii) Store each item name in a list called item_names and each total cost in a list called item_totals.
(iv) After the loop ends, display all items and their total costs in a formatted list using f-strings.
(v) Calculate and display:
    • The total number of items purchased
    • The overall bill total (using sum())
    • The most expensive item purchased (using max())
(vi) Add validation to make sure item prices and quantities entered are positive.
(vii) Add comments to explain each section of your code.
"""
#SOLUTION

# Function to welcome the user
def welcome():
    name = input("Please enter your name: ")
    print(f"\nWelcome, {name}. Let's calculate your shopping bill.\n")

# Call the welcome function
welcome()

# Create empty lists to store item names and total costs
item_names = []
item_totals = []

# Loop to allow the user to keep entering items until they type 'end'
while True:
    item_name = input("Enter item name (or type 'end' to finish): ").strip().capitalize()
    if item_name == "End":
        break
    else:
        item_names.append(item_name)

# Loop through each item to get price and quantity
for i in range(len(item_names)):

    # Validate price input
    item_price = float(input(f"Enter the price of {item_names[i]} (€): "))
    while item_price <= 0:
        print("Invalid entry: Price must be a positive number.")
        item_price = float(input(f"Enter the price of {item_names[i]} (€): "))

    # Validate quantity input
    item_quantity = int(input(f"Enter the quantity of {item_names[i]}: "))
    while item_quantity <= 0:
        print("Quantity must be a positive number.")
        item_quantity = int(input(f"Enter the quantity of {item_names[i]}: "))

    # Calculate total cost for this item
    total_cost = round(item_price * item_quantity, 2)

    # Store total in list
    item_totals.append(total_cost)

    print(f"{item_names[i]} added to your bill.\n")

# After loop ends, display all items and totals
print("\nShopping Summary")
for i in range(len(item_names)):
    print(f"{item_names[i]}: €{item_totals[i]}")

# Calculate totals and display bill summary
if len(item_names) > 0:
    total_items = len(item_names)
    overall_total = round(sum(item_totals), 2)
    most_expensive = max(item_totals)
    most_expensive_item = item_names[item_totals.index(most_expensive)]

    print("\nBill Summary")
    print(f"Total number of items: {total_items}")
    print(f"Overall bill total: €{overall_total}")
    print(f"Most expensive item: {most_expensive_item} (€{most_expensive})")
else:
    print("\nNo items were entered.")
