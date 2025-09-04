# ---------------------------------------------------------------
# 6th Year Computer Science – Python Class 1:
# Conditionals, Iteration (Nested Loops), Functions, and Unit Testing
# ---------------------------------------------------------------

"""
Leaving Certificate Learning Outcomes (Relevant Only)

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


def age_category(age: int) -> str:
    """Return 'Child' (<13), 'Teenager' (13–17), or 'Adult' (18+)."""
    if age < 13:
        return "Child"
    elif 13 <= age <= 17:
        return "Teenager"
    else:
        return "Adult"

print("Age 12 ->", age_category(12))
print("Age 15 ->", age_category(15))
print("Age 30 ->", age_category(30))

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
# SECTION D — Introduction to Unit Testing
# ===============================================================

# NOTES:
# - A unit test checks that one small piece of code (usually a function) works correctly.
# - We do this by comparing the actual output of the function with the expected output.
# - Python has a simple way to do this using "assert".
# - assert <condition> will stop the program with an error if the condition is False.
# - If all asserts pass, the program keeps running with no messages (no news is good news).
print("\nSECTION D — Unit Testing...")

# Functions to test
def add(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0


# ---------------------------------------------------------------
# Example: Using assert
# ---------------------------------------------------------------
# This test will pass because add(2, 3) really is 5
assert add(2, 3) == 5

# If you change it to assert add(2, 3) == 6, the program will stop with an error.
print("Example test passed!")


# ---------------------------------------------------------------
# Task D1: Basic Unit Tests
# ---------------------------------------------------------------
# Instructions:
# 1. Write asserts to test:
#    - add(2,3) == 5
#    - add(-1,1) == 0
#    - is_even(4) == True
#    - is_even(5) == False
# 2. If all tests pass, print "Basic tests passed!"


# ---------------------------------------------------------------
# Task D2: Extended Unit Tests
# ---------------------------------------------------------------
# Instructions:
# 1. Test rectangle_area(3,4) == 12.
# 2. Test power(2,5) == 32.
# 3. Test grade_band with one value from each category.
# 4. If all correct, print "Extended tests passed!".



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

