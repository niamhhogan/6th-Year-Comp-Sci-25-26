"""
---------------------------------------------------------------
6th Year Computer Science – Class 3: Recursion
---------------------------------------------------------------

Learning Intentions:
- Understand what recursion means in Computer Science
- Identify a recursive function and explain its structure
- Explain the importance of the stopping point (base case)
- Recognise what happens if a base case is missing
- Describe recursion depth and Python’s recursion limit
- List the four essential parts of a recursive function
- Trace recursive calls and identify when calculations occur
- Compare pros and cons of recursion vs loops
- Apply recursion to classic problems and simple string/list tasks

Success Criteria:
- I can define recursion and recursive functions with examples
- I can correctly identify the base case, recursive case, and recursive calls
- I can explain why recursion depth is limited in Python
- I can trace factorial(4) and explain when results are returned
- I can evaluate when recursion is useful compared to loops
- I can implement and test at least three recursive functions
"""


"""
---------------------------------------------------------------
Definition of Recursion
---------------------------------------------------------------

Recursion is a way of solving problems by breaking them down into 
smaller versions of the same problem. Each solution depends on the 
solutions to its smaller subsets, until eventually we reach the 
simplest possible version, known as the *base case*.

A recursive function is a function that calls itself. Each time it 
calls itself, it passes in a smaller piece of the original problem. 
These repeated calls are called *recursive calls*. The function 
continues breaking the problem down until it reaches the base case, 
which does not call itself again and allows the results to be built 
back up.

Example:
- To sum numbers from 1 to 4:
  4 + 3 + 2 + 1
  This can be seen as 4 + (sum of 1 to 3).

Real-life Analogies
---------------------------------------------------------------

1. Russian Dolls:
   - Each doll contains a smaller one inside.
   - Opening one doll reveals the next, until you reach the 
     smallest doll (the base case).
   - This is like recursion: each problem contains a smaller 
     version of itself.

2. Walking down stairs:
   - To get to the bottom, you take one step and then repeat 
     the problem ("walk down the stairs") on the smaller staircase.
   - Eventually you reach the last step (the base case).

3. Cutting a pizza:
   - To share a pizza fairly, keep cutting it into smaller 
     pieces. The process repeats until the pieces are as 
     small as you want (the base case).

---------------------------------------------------------------
Mathematical Examples
---------------------------------------------------------------

1. Factorial (n!):
   - Defined recursively: 
        n! = n × (n-1)!   for n > 0
        0! = 1            (base case)
   - Example: 4! = 4 × 3 × 2 × 1
     Written recursively:
        4! = 4 × 3!
        3! = 3 × 2!
        2! = 2 × 1!
        1! = 1 × 0!
        0! = 1   (base case reached)
     Once the base case is reached, the results are multiplied 
     together on the way back up.

2. Fibonacci sequence:
   - Defined recursively:
        F(0) = 0
        F(1) = 1
        F(n) = F(n-1) + F(n-2)   for n ≥ 2
   - Example: F(5)
        F(5) = F(4) + F(3)
        F(4) = F(3) + F(2)
        F(3) = F(2) + F(1)
        ...
     The problem breaks into smaller Fibonacci problems, 
     until we reach the base cases F(0) and F(1).

3. Summation:
   - Defined recursively:
        sum(n) = n + sum(n-1)   for n > 0
        sum(0) = 0              (base case)
   - Example: sum(4)
        sum(4) = 4 + sum(3)
        sum(3) = 3 + sum(2)
        sum(2) = 2 + sum(1)
        sum(1) = 1 + sum(0)
        sum(0) = 0   (base case reached)
     Result: 4 + 3 + 2 + 1 + 0 = 10
"""


"""
---------------------------------------------------------------
Code Examples in Python
---------------------------------------------------------------
"""

# Example 1 – Simple countdown
def countdown(n):
    if n <= 0:  # base case
        print("Go!")
    else:       # recursive case
        print(n)
        countdown(n - 1)

# Example 2 – Factorial
def factorial(n):
    if n == 0:       # base case
        return 1
    return n * factorial(n - 1)   # recursive call

# Example 3 – Fibonacci
def fibonacci(n):
    if n <= 1:   # base cases
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example 4 – Summation
def summation(n):
    if n == 0:   # base case
        return 0
    return n + summation(n - 1)

# Example 5 – Reverse a string
def reverse_string(s):
    if len(s) <= 1:  # base case
        return s
    return reverse_string(s[1:]) + s[0]


"""
---------------------------------------------------------------
In Computer Science, what is a recursive function?
---------------------------------------------------------------
A recursive function is a function that calls itself, each time 
with a smaller or simpler input. Each call reduces the problem 
towards a stopping point (the base case).
"""
#Example:
def factorial(n):
    if n == 0:   # base case
        return 1
    return n * factorial(n - 1)

"""
- factorial(4) calls factorial(3)
- factorial(3) calls factorial(2)
- factorial(2) calls factorial(1)
- factorial(1) calls factorial(0) and stops
"""

"""
---------------------------------------------------------------
What happens if the stopping point is not determined?
---------------------------------------------------------------
If there is no base case, or if the input never reaches it, the 
function will keep calling itself forever. In Python, this leads 
to a "RecursionError: maximum recursion depth exceeded".
"""
#Example:
def bad_count(n):
    print(n)
    bad_count(n - 1)   # no base case → infinite recursion

#- Running bad_count(5) will eventually crash with RecursionError.


"""
---------------------------------------------------------------
What is another name for the stopping point?
---------------------------------------------------------------
The stopping point in recursion is called the *base case*.
"""
#Example:
#In countdown:
def countdown(n):
    if n <= 0:   # base case
        print("Go!")
    else:
        print(n)
        countdown(n - 1)
#The base case is when n <= 0.


"""
---------------------------------------------------------------
What does recursion depth mean?
---------------------------------------------------------------
Recursion depth is the number of times a function calls itself 
before reaching the base case. Each recursive call adds a new 
frame to the call stack.
"""
#Example:
#countdown(3) has a recursion depth of 3
#(calls with 3 → 2 → 1 → 0, then stops).


"""
---------------------------------------------------------------
What is the Python limit for recursion depth?
---------------------------------------------------------------
By default, Python allows around 1000 recursive calls before 
raising a RecursionError. This limit exists to prevent infinite 
recursion from crashing the program.

Example:
- factorial(995) might work
- factorial(2000) will likely raise RecursionError
"""

"""
---------------------------------------------------------------
The Four Parts of a Recursive Function
---------------------------------------------------------------
1. Input(s) – parameters passed to the function
2. Base Case – condition that stops the recursion
3. Recursive Case – where the function calls itself
4. Return Statement – builds the result back up
"""
#Example (summation):
def summation(n):
    if n == 0:        # base case
        return 0
    return n + summation(n - 1)   # recursive case + return



"""
---------------------------------------------------------------
Do the calculations happen when going down or on the way back up?
---------------------------------------------------------------

When going down, the function just makes more recursive calls. 
It hasn’t done any actual calculations yet — it is only setting 
up smaller versions of the problem.

When coming back up (after the base case is reached), the 
function finally performs the calculations as each call returns.

---------------------------------------------------------------
💡 Analogy – Climbing into a Cave
---------------------------------------------------------------
Imagine walking into a cave:
- Going down: you keep stepping deeper, leaving breadcrumbs. 
  You haven’t collected anything yet (no calculations).
- Base case: you reach the end of the cave, where the treasure is.
- Coming back up: as you retrace your steps out of the cave, 
  you pick up the treasures (the calculations are done).

---------------------------------------------------------------
🔄 Factorial Example: factorial(4)
---------------------------------------------------------------
Definition:
factorial(0) = 1   (base case)
factorial(n) = n × factorial(n - 1)   (recursive case)

Step 1 – Going Down (just calling functions):
factorial(4) → calls factorial(3)
factorial(3) → calls factorial(2)
factorial(2) → calls factorial(1)
factorial(1) → calls factorial(0)
factorial(0) = 1   ← base case reached!

Step 2 – Coming Back Up (returning and calculating):
factorial(1) = 1 × factorial(0) = 1 × 1 = 1
factorial(2) = 2 × factorial(1) = 2 × 1 = 2
factorial(3) = 3 × factorial(2) = 3 × 2 = 6
factorial(4) = 4 × factorial(3) = 4 × 6 = 24

---------------------------------------------------------------
🖼️ Visualising the Call Stack
---------------------------------------------------------------
Going Down (stacking calls):
factorial(4)
 └── factorial(3)
       └── factorial(2)
             └── factorial(1)
                   └── factorial(0) = 1   ← base case

Coming Back Up (calculations happen here):
factorial(1) = 1 × 1 = 1
factorial(2) = 2 × 1 = 2
factorial(3) = 3 × 2 = 6
factorial(4) = 4 × 6 = 24
"""



"""
---------------------------------------------------------------
Pros and Cons of Recursion vs Loops
---------------------------------------------------------------
Pros:
- Recursion matches the mathematical definition (e.g., factorial, Fibonacci)
- Makes some problems easier to express (tree traversal, divide and conquer)
- Code can be shorter and more elegant

Cons:
- Slower than loops in Python (function call overhead)
- Uses more memory (call stack for each recursive call)
- Risk of RecursionError if the base case is missing or depth is too high
- Loops are usually more efficient in practice for simple problems

Example Comparison:
# Recursive sum
def summation(n):
    if n == 0:
        return 0
    return n + summation(n - 1)

# Iterative sum
def summation_loop(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total
"""
"""
Consolidation Tasks
- Implement: product(n) recursively
- Implement: count_vowels(s) recursively
- Implement: contains(xs, x) recursively for lists
- Trace by hand: factorial(4), reverse_string('cat')
- Short answers:
  1) Define recursion in your own words
  2) What is a base case? Another name for it?
  3) What happens if the base case is missing?
  4) What is Python’s default recursion depth?
  5) Do calculations happen going down or coming back up?
  6) One advantage and one disadvantage of recursion vs loops
"""
