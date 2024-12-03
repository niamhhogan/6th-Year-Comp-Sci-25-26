# ** Functions Lesson Plan: Intermediate Level **

"""
In this lesson, we will explore more advanced functions. 
We will use conditional statements, Boolean logic, and user input inside functions. 
We will also practice debugging code.
"""

# Example 1: Using Conditional Statements in a Function
def check_even(number): 
    if number % 2 == 0: 
        return True 
    else: 
        return False

# Call the function
print(check_even(4)) # Should return True
print(check_even(7)) # Should return False

""" Task 1: 
Write a function is_teenager that takes an age as input and returns True if the age is between 13 and 19 (inclusive) and False otherwise. 
Call the function with at least two examples to test it.
"""
#Task 1 Solutions
#using parameters as input
def is_teenager(age):
    if age >= 13 and age <=19:
        return True
    else:
        return False

print(is_teenager(12))
print(is_teenager(15))

#using an input statement
def is_teenager_2():
    age=int(input("How old are you?"))
    if age >= 13 and age <=19:
        return True
    else:
        return False
print(is_teenager_2())




# Example 2: Using Boolean Logic and Input in Functions
def check_login(username, password): 
    if username == "admin" and password == "1234": 
        return "Login Successful"
    else: 
        return "Login Failed"

# Test the function
print(check_login("admin", "1234"))  # Should return "Login Successful"
print(check_login("user", "pass"))  # Should return "Login Failed"

""" Task 2: 
Write a function validate_pin that takes a 4-digit PIN as input and checks:
    - The PIN must contain exactly 4 digits.
    - All characters in the PIN must be numbers.
The function should return "Valid PIN" if both conditions are true, and "Invalid PIN" otherwise. 
Example call: validate_pin("1234") should return "Valid PIN".
"""

"""
#Task 2 using code we already knew: 
def validate_pin():
    pin=int(input("Enter your PIN: "))
    if pin >9999 and pin < 1000:
        print("PIN must contain exactly 4 digits")
    elif pin == 1234:
        print("Valid PIN")
    else:
        print("Invalid PIN")
print(validate_pin())
"""

def validate_pin():
    pin = input("Enter your 4-digit PIN: ") #value stored as a string
    
    # Check if the PIN has exactly 4 characters and all are digits
    if len(pin) == 4 and pin.isdigit(): #.isdigit() is a built in function
        return "Valid PIN"
    else:
        return "Invalid PIN"

print(validate_pin())

# .isalpha() checks if the string contains letters
        
        

# Task 3: Debugging Task
"""
The following function is meant to return the square of a number, but there are errors in the code. 
Find and fix the errors.
"""

#fixed version:
def square(number):
    if number < 0:
        print("Invalid input, number must be positive")
    else: 
        return number ** 2 

print(square(4))  # Should return 16
print(square(-3)) # Should print an error message


# Example 4: Using Multiple Conditions in Functions
def grade_calculator(score):
    if score >= 90:
        return "H1"
    elif score >= 80:
        return "H2"
    elif score >= 70:
        return "H3"
    elif score >= 60:
        return "H4"
    elif score >= 50:
        return "H5"
    elif score >= 40:
        return "H6"
    else:
        return "Fail"

# Test the function
print(grade_calculator(85)) # Should return "H2"
print(grade_calculator(59)) # Should return "H5"

""" Task 4: 
Write a function check_discount that takes age and is_member as inputs:
    - If the age is below 18 or above 60, or if is_member is True, return "Eligible for discount".
    - Otherwise, return "Not eligible for discount".
Example calls:
check_discount(15, False) -> "Eligible for discount"
check_discount(30, True) -> "Eligible for discount"
"""

# ** Quiz **
"""
**10 Multiple-Choice Questions**

1. What does a function with `return` do?  
   a) Prints a value to the console.  
   b) Ends the program.  
   c) Stores a value for later use.  
   d) Declares a variable.  
   

2. What is Boolean logic?  
   a) Math operations.  
   b) Combining true/false values with AND, OR, NOT.  
   c) Returning numbers.  
   d) Declaring functions.  
   

3. What will the following code return?  
   
   def check_even(n):
       return n % 2 == 0
   print(check_even(8))

   a) True  
   b) False  
   c) None  
   d) Error  


4. What keyword allows functions to take input from the user?  
   a) print  
   b) input  
   c) return  
   d) define  
   

5. What is wrong with the following function?  

   def greet(name):
       print(f"Hello, {name}!")

   greet()

   a) No default parameter is given.  
   b) The function is not returning anything.  
   c) Syntax error.  
   d) Nothing is wrong.  


6. How would you call a function named `calculate_tax` with a value of 100?  
   a) calculate_tax  
   b) calculate_tax[100]  
   c) calculate_tax(100)  
   d) tax_calculate(100)  


7. What will the following code output?  

   def test(a, b):
       return a and b

   print(test(True, False))

   a) True  
   b) False  
   c) Error  
   d) None  


8. Which is an example of a valid function name?  
   a) 1function  
   b) function_name  
   c) def_function  
   d) name()  


9. What is the purpose of a conditional statement in a function?  
   a) To execute code based on a condition being true or false.  
   b) To call another function.  
   c) To return variables.  
   d) To define inputs.  
   

10. What will this code output?  

    def multiply_by_two(num):
        return num * 2

    print(multiply_by_two(5))

    a) 5  
    b) 10  
    c) multiply_by_two  
    d) Error  
"""
