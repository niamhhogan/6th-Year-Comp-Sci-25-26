""" A function is a reusable block of code that performs a specific task.
    Functions are useful for reducing repetition and improving readability 
"""

#Example 1
def greet(): #function heading
    print("Hello, welcome to the class!")
greet() #calling the function

"""Task 1:
 Write a function say_goodbye that prints Goodbye, see you next time! and call it."""
def say_goodbye():
    print("Goodbye, see you next  time!")
say_goodbye()

#Example 2
def greet_person(name, age): #using parameters in the function
    print(f"Hello, {name}!, You are {age} years old") #using a formatted string
greet_person("Niamh","old") #calling the function

""" Task 2:  
Write a function calculate_area that takes the length and width of a rectangle and prints the area.
Example call: calculate_area(5, 10) should output The area is 50 """

def calculate_area(length, width):
    print("The area is: ", length*width)
calculate_area(37,43)



#Example 3
def add_numbers(a, b):
    return a + b #return stores the value, which can then be used later in the program 
result = add_numbers(3, 7)
print(f"The result is {result}")

""" Task 3:
Write a function find_max that takes two numbers and returns the larger one.
Example call: find_max(3, 8) should return 8. """





#Example 4: Currency Converter
def convert_to_euro(dollars, exchange_rate):
    return dollars * exchange_rate
amount = convert_to_euro(50, 0.9)
print(f"50 dollars is equal to {amount} euros.")  

""" Task 4:
Write a function convert_temperature that converts a temperature from Celsius to Fahrenheit.
Formula: F = (C * 9/5) + 32 """





"""
# ** Quiz ** 
**10 Multiple-Choice Questions**

1. What keyword is used to define a function in Python?  
   a) function  
   b) define 
   c) def 
   d) func  
  

2. What is the purpose of a function?  
   a) To store data.  
   b) To reuse a block of code.  
   c) To print variables.  
   d) To define variables.  
   

3. How do you call a function named `say_hello`?  
   a) say_hello[] 
   b) call say_hello
   c) say_hello()  
   d) run say_hello 


4. What does the following function return?  

   def add(a, b):
       return a + b
   print(add(2, 3))
   
   a) 5
   b) add(2, 3) 
   c) a + b  
   d) Error  


5. What is a parameter?  
   a) A keyword that defines a function.  
   b) A variable that stores a value inside a function.  
   c) A value you pass into a function.  
   d) A function call.  
    

6. What will this code print?  
   
   def greet(name):
       print(f"Hi {name}!")
   greet("Tom")
 
   a) Hi name! 
   b) Hi Tom! 
   c) Hi greet!  
   d) Error  
    

7. Which function will return the value `25`?  
   a) def square(x):
           return x * x
      print(square(5))
      
   b) def square(x):
           print(x * x)  
      square(25)
     
   c) def square(x):
           return x + x 
      print(square(25))
      
   d) None of the above.  
   

8. What does the `return` keyword do?  
   a) Ends the program.  
   b) Outputs a value from a function.  
   c) Stops the function from running.  
   d) Declares a parameter.  
   
9. Can a function have multiple parameters?  
   a) Yes  
   b) No  
 

10. What is the output of this code?  
   
    def multiply(a, b):
        return a * b
    print(multiply(4, 5))

    a) 20
    b) 45
    c) 9
    d) Error  
 
"""
