"""
6th Year Computer Science
Class 5: Validation Checks and Algorithms
"""

"""
Validation Checks: Return True or False
.isdigit() - Checks if all characters in a string are digits (0–9). 
.isalpha() - Checks if all characters are alphabetic (A–Z, a–z).
.isalnum() - Checks if all characters are either alphabetic or numeric (letters or digits).
"""

#isdigit() example 1: Returning true or false
seven="7"
print(seven.isdigit())

#isdigit() example 2: using it in a conditional statement
user_age = input("Enter your age: ")

if user_age.isdigit():
    print("Valid age entered.")
else:
    print("Invalid input. Please enter numbers only.")


#isalpha() example 
name = input("Enter your first name: ")

if name.isalpha():
    print("Valid name.")
else:
    print("Invalid name. Please use letters only.")
    
    
#isalnum() example
username = input("Create a username: ")

if username.isalnum():
    print("Valid username.")
else:
    print("Invalid username. Use only letters and numbers (no spaces or symbols).")


#LC EXAM Q
def is_valid_eircode(test_eircode):

    # This function checks whether 'test eircode' is a valid Eircode or not
    # It returns True if 'test eircode' is a valid Eircode. False otherwise.

    # Uses:
    # s.isalpha () -> True if s contains alphabetic only; False otherwise
    # s.isdigit () -> True if s contains digits only; False otherwise
    # s.isalnum () -> True if s contains alpha-numeric only; False otherwise

    if not test_eircode[0].isalpha():
        return False

    # if the second character isn't a digit or the third character isn't a
    # digit the Eircode is invalid so return False
    if ((not test_eircode[1].isdigit()) or (not test_eircode[2].isdigit())):
        return False

    if not test_eircode[-4:].isalnum():
        return False

    return True

#Worksheet with full exam question printed out in class




