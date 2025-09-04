#Functions

def vol_sphere(r):
    volume=((4/3)*3.14*(r**3))
    return volume #using return

#to call
print("The volume of the sphere is: ", vol_sphere(10))


#Email validation example
def validate_email(email_address):
    if (email_address.count("@")==1
    and email_address.count(".")>=1
    and len(email_address) >=8):
        return True
    else:
        return False
    
email_address=input("Please enter emai address: ").strip().lower()
if (validate_email(email_address)):
    print("Email address valid")
else:
    print("Email address not valid")
    
"""Task: create a function that checks if a username is valid.

A valid username should contain:
-more than 8 characters
-no spaces
-at least 1 special character out of ! or # 
"""


"""
~~~Unit Testing~~~
- testing for bugs/errors
- unit means testing one piece (e.g. loop, function) at a time
- a unit test is another piece of code which passes arguments to the
function to be tested
- the unit test calculates the value that the function is expected to return,
the funtion returns the actual value
- the unit test then checks whether the actual value is equal to the expected
value

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
creating a function to carry out a unit test:
name of function - unitTest()
arguments - functionToTest()
unitTest() determines where functionToTest() works correctly
unitTest() return True or False

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
steps:
1. create test data
2. calculate expected value
3. call the function to test
4. check actual value returned vs expected value
5. return test result
"""

#function to test
def vol_sphere(r):
    volume=((4/3)*3.14*(r**3))
    return volume

#creating unitTest() function:
def unitTest():
    
    testR=2 #1. creating test data
    expected_val=(4/3)*3.14*(testR**3) #2. calculating expected value
    test_value=vol_sphere(testR) #3. calling the function to test
    
    passed=True 
    if expected_val != test_value: #4. checking actual v expected
        passed=False
    return passed #5. return test results
print("Test passed: ", unitTest())


#multiple test cases - uses logic instead of expected value

#function to test
def larger_number(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
    
#unit test
def unit_test():
    #creating test data
    first_nums=[1,2,3,4,5]
    second_nums=[1,1,4,-1,100]
    
    #loop through values in both lists
    fails=0
    for i in range(len(first_nums)):
        test1=first_nums[i]
        test2=second_nums[i]
        test_val=larger_number(test1,test2)
        
    #logic to compare values
        if test1>test2:
            if test1 != test_val:
                fails += 1
        else:
            if test2 != test_val:
                fails +=1
    return fails
print("Total test fails: ", unit_test())
