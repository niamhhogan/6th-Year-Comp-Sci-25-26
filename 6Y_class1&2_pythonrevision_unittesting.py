# ---------------------------------------------------------------
# 6th Year Computer Science – Python Class 1:
# Conditionals, Iteration (Nested Loops), Functions, and Unit Testing
# ---------------------------------------------------------------

"""
Leaving Certificate Learning Outcomes

Strand 1: Practices and Principles
- 1.3 solve problems by deconstructing them into smaller
  units using a systematic approach in an iterative fashion
- 1.4 solve problems using skills of logic
- 1.7 develop algorithms to implement chosen solutions
- 1.22 read, write, test, and modify computer programs

Strand 2: Core Concepts
- 2.6 construct algorithms using appropriate sequences,
  selections/conditionals, loops and operators to solve a range of
  problems, to fulfil a specific requirement
- 2.7 implement algorithms using a programming language to solve
  a range of problems
- 2.9 assemble existing algorithms or create new ones that use
  functions (including recursive), procedures, and modules
- 2.19 test solutions and decisions to determine their short-term and
  long-term outcomes
- 2.20 identify and fix/debug warnings and errors in computer code
  and modify as required
- 2.22 explain the different stages in software testing
"""

# ---------------------------------------------------------------
# Learning Intentions (Today’s Lesson)
# ---------------------------------------------------------------
"""
By the end of this lesson, you will be able to:
1) Revise selections/conditionals in Python.
2) Apply iteration with nested loops to build structured outputs.
3) Create functions with single and multiple parameters (vs. arguments).
4) Explain the difference between print and return.
5) Write and run simple unit tests to check function correctness.
"""

# ===============================================================
# SECTION A — RECAP: Selections / Conditionals
# ===============================================================

# NOTES:
# - Conditionals let programs make decisions based on True/False (boolean) expressions.
# - Common operators: ==, !=, <, <=, >, >=. Combine with and/or/not.
# - Use elif for multiple branches; use else for a default branch.
# - Be careful with boundary values (e.g., 17 vs 18).


def age_category(age):
    """Return 'Child' (<13), 'Teenager' (13–17), or 'Adult' (18+)."""
    if age < 13:
        return "Child"
    elif 13 <= age <= 17:
        return "Teenager"
    else:
        return "Adult"

print("Age 12", age_category(12))
print("Age 15", age_category(15))
print("Age 30", age_category(30))

# ---------------------------------------------------------------
# Task A1: Grade Bands
# ---------------------------------------------------------------
# Instructions:
# 1. Define a function called grade_band(score).
# 2. If score is 90–100, return "Distinction".
#    If 75–89, return "Merit".
#    If 50–74, return "Pass".
#    Otherwise, return "Fail".
# 3. Test the function by printing results for at least 3 different scores.





# ===============================================================
# SECTION B — Iteration with NESTED LOOPS
# ===============================================================

# NOTES:
# - Nested loops = a loop inside another loop.
# - Typical pattern: outer loop controls ROWS; inner loop controls COLUMNS.
# - range(a, b) counts from a up to (but not including) b.
# - Formatting tables: print(..., end="\t") to keep values on one line; use print() to start a new line.


# ---------------------------------------------------------------
# Example 1: 5 x 5 multiplication table (actual values)
# ---------------------------------------------------------------
print("Example 1: 5 x 5 multiplication table")
for i in range(1, 6):          # rows
    for j in range(1, 6):      # columns
        print(i * j, end="\t") # product with tab spacing
    print()                    # move to next row
    
    

# ---------------------------------------------------------------
# Example 2: Cinema seating chart (real-world rows × seats)
# ---------------------------------------------------------------
# Purpose: show how i (rows) and j (seats) label a real seating layout.
print("\nExample 2: Cinema seating chart (Rows 1–3, Seats 1–4)")
for i in range(1, 4):          # rows
    for j in range(1, 5):      # seats
        print(f"Row {i} Seat {j}", end=" | ")
    print()


# ---------------------------------------------------------------
# Task B1: School Timetable
# ---------------------------------------------------------------
# Instructions:
# 1. Use nested loops.
# 2. Outer loop → days = ["Monday", "Tuesday", "Wednesday"]
# 3. Inner loop → periods = 1–4
# 4. Print in the format:
#    Monday Period 1
#    Monday Period 2
#    ...
#    Tuesday Period 1
#    etc.




# ===============================================================
# SECTION C — Functions: Parameters vs Arguments; print vs return
# ===============================================================

# NOTES:
# - Parameters are the placeholders in the function definition (e.g., def f(x, y):).
# - Arguments are the actual values you pass when calling (e.g., f(2, 3)).
# - print(...) shows text to the console but does NOT give you a value to reuse.
# - return ... gives back a value you can store, test, or pass into other functions.


# Example: print vs return

def add_print(a, b):
    print(a + b)   # prints the result, but you can't use it later

def add_return(a, b):
    return a + b   # returns the result, so you can use it


# Example: Area calculator function

def rectangle_area(width, height):
    area = width * height
    return area

# Using the function
area1 = rectangle_area(3, 4)
area2 = rectangle_area(5, 2.5)
print("Areas:", area1, area2)



# Example: Creating a function that capitalises text

def capitalise(word):
    return word.upper()

# Using the function
result = capitalise("computer")
print(result)  # Output: COMPUTER



# ---------------------------------------------------------------
# Task C1: Power function
# ---------------------------------------------------------------
# Instructions:
# 1. Define a function power(base, exponent).
# 2. Inside, return base raised to exponent (use ** operator).
# 3. Test the function with at least two examples.



# ===============================================================
# SECTION D — Testing
# ===============================================================

# NOTES:
# - Testing checks that code works correctly before it is used.
# - In Python we use 'assert' to compare expected vs actual results.
#
# What is 'assert'?
# - Syntax:  assert condition
# - If the condition is True  -> the program continues (no message).
# - If the condition is False -> the program stops with an AssertionError.
# - We use assert to check that the ACTUAL output of a function
#   matches the EXPECTED output we worked out in advance.
#
# Unit testing:
# - Tests ONE small piece of code in isolation (usually a single function).
# - Purpose: check if that function gives the right answer for given inputs.
# - It does not worry about the rest of the program, only that one "unit".
# - Example: rectangle_area(3,4) should return 12.
#
# Functional testing:
# - Tests a COMPLETE FEATURE from start to finish, as a user would use it.
# - Purpose: check if the feature behaves correctly overall,
#   including validation, calculation, and messages.
# - Example: the area_feature should give "Area is 12" for valid inputs
#   and an error message if inputs are invalid.


"""
Example of unit test manually:

def volCylinder(radius, height):
    volume = 3.14 * (radius**2) * height
    return volume

# step 1: create test data
test_radius = 2
test_height = 1

# step 2: calculate expected value
expected_volume = 3.14 * (test_radius**2) * test_height

# step 3: call function and pass the test values as arguments
test_answer = volCylinder(test_radius, test_height)

# step 4: check if the value returned by the function matches the expected value
passed = True
if expected_volume != test_answer:
    passed = False
    
return passed
"""


# ===============================================================
# Example wrapped into functions
# ===============================================================

def volCylinder(radius, height):
    """Return volume of a cylinder: π r^2 h (using 3.14 for π)."""
    volume = 3.14 * (radius**2) * height
    return volume

def unit_test():
    test_radius = 2
    test_height = 1
    expected_volume = 3.14 * (test_radius**2) * test_height
    test_answer = volCylinder(test_radius, test_height)
    passed = True
    if expected_volume != test_answer:
        passed = False
    return passed

print("Test passed:", unit_test())


# ===============================================================
# Examples using assert
# ===============================================================

def rectangle_area(width, height):
    return width * height

def area_feature(width, height):
    if width <= 0 or height <= 0:
        return "Error: width and height must be positive."
    area = rectangle_area(width, height)
    return f"Area is {area}"


# Example: Using assert
assert 2 + 2 == 4
# If you change it to assert 2 + 2 == 5, the program would stop with an error.
print("Assert example passed!")


# Example Unit Tests using assert (testing one function in isolation)
# We are only testing rectangle_area here, nothing else.
assert rectangle_area(3, 4) == 12
assert rectangle_area(5, 2) == 10
assert rectangle_area(2.5, 2) == 5.0
print("Unit tests passed!")


# Example Functional Tests (testing the whole feature)
# We now test area_feature, which includes input checks + calculation + message.
assert area_feature(3, 4) == "Area is 12"
assert area_feature(5, 2) == "Area is 10"
assert area_feature(-3, 4) == "Error: width and height must be positive."
assert area_feature(3, 0) == "Error: width and height must be positive."
print("Functional tests passed!")


# ===============================================================
# Task D1: Write your own unit tests
# ===============================================================

# Instructions:
# 1) Create a function add(a, b) that returns the sum of a and b.
# 2) Write asserts to test:
#    - add(2, 3) == 5
#    - add(-1, 1) == 0
#    - add(0, 0) == 0
# 3) Print "Basic unit tests passed!" if your asserts succeed.

def add(a, b):
    return a + b

# --- Unit tests for add ---
assert add(2, 3) == 5
assert add(-1, 1) == 0
assert add(0, 0) == 0
print("Basic unit tests passed!")


# ===============================================================
# Task D2: Write your own functional tests
# ===============================================================

# Instructions:
# 1) Create a simple feature called compare_feature(a, b) that:
#       - returns "First is larger"  if a > b
#       - returns "Second is larger" if b > a
#       - returns "Numbers are equal" if a == b
# 2) Write asserts to test all three cases.
# 3) Print "Functional tests passed!" if your asserts succeed.

def compare_feature(a, b):
    if a > b:
        return "First is larger"
    elif b > a:
        return "Second is larger"
    else:
        return "Numbers are equal"

# --- Functional tests ---
assert compare_feature(5, 3) == "First is larger"
assert compare_feature(2, 9) == "Second is larger"
assert compare_feature(7, 7) == "Numbers are equal"
print("Functional tests passed!")

# ===============================================================
# Comprehension Questions 
# ===============================================================

# 1. What is the difference between unit testing and functional testing?
# 2. What does assert do if the condition is True? What if it is False?
# 3. In the volCylinder test, why do we calculate an expected_volume before comparing?
# 4. Why do we test area_feature with both valid and invalid inputs?
# 5. A student writes: assert rectangle_area(3, 4) == "12". What is the mistake?

# ===============================================================
# Extra Tasks to Try
# ===============================================================

# Task A: Write a function max_of_three(a, b, c) that returns the largest number.
#         Add at least 3 unit tests using assert.

# Task B: Extend the unit tests for add(a, b) to include:
#         - negative numbers
#         - decimals

# Task C: Write a function safe_divide(a, b) that:
#         - returns "Cannot divide by zero" if b == 0
#         - otherwise returns a / b
#         Add both unit tests and functional tests.


# ===============================================================
# SECTION E — Recap / Consolidation
# ===============================================================

"""
Today we revised:
- Selections/conditionals (if, elif, else).
- Iteration with nested loops (multiplication table, cinema seating, timetable).
- Functions with parameters and arguments.
- Difference between print vs return.
- Writing and running simple unit tests with assert.
"""





