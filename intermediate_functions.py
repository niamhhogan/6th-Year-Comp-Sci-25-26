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

# Example 3: Debugging Task
"""
The following function is meant to return the square of a number, but there are errors in the code. 
Find and fix the errors.
"""

def square(number):
    if number < 0:
        print"Invalid input, number must be positive"
    return number * 2  # This is incorrect

print(square(4))  # Should return 16
print(square(-3)) # Should print an error message

""" Task 3: 
Fix the function above so it correctly calculates the square of a positive number. If the input is negative, return an error message.
"""

# Example 4: Using Multiple Conditions in Functions
def grade_calculator(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Test the function
print(grade_calculator(85)) # Should return "B"
print(grade_calculator(59)) # Should return "F"

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
