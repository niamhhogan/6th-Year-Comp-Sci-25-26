# Nested Loops - Lesson Examples and Tasks

# 1. Number Grid Example
# This prints coordinates in a 3x3 grid.
for i in range(1, 4):  # Outer loop (rows)
    for j in range(1, 4):  # Inner loop (columns)
        print(f"({i}, {j})", end=" ")  # Print coordinates in one line
    print()  # Moves to the next line after inner loop finishes

# Task 1: Modify the code to print a 4x4 grid instead of a 3x3 grid.


# 2. Printing a Triangle Pattern
# This prints a right-angled triangle using nested loops.
rows = 5
for i in range(1, rows + 1):  # Outer loop controls rows
    for j in range(i):  # Inner loop controls number of stars
        print("*", end=" ")  # Print star without moving to a new line
    print()  # Moves to the next line

# Task 2: Modify the code to print a reverse triangle pattern.


# 3. Multiplication Table (5x5)
# This generates a multiplication table from 1 to 5.
for i in range(1, 6):  # Outer loop for rows (1 to 5)
    for j in range(1, 6):  # Inner loop for columns (1 to 5)
        print(f"{i * j:2}", end="  ")  # Print result formatted for alignment
    print()  # Moves to the next line

# Task 3: Modify the code to generate a 10x10 multiplication table.


# 4. Chessboard Pattern
# This prints an 8x8 chessboard pattern using black and white squares.
for i in range(8):  # Outer loop for rows
    for j in range(8):  # Inner loop for columns
        if (i + j) % 2 == 0:
            print("⬛", end=" ")  # Black square
        else:
            print("⬜", end=" ")  # White square
    print()  # Moves to the next line

# Task 4: Modify the code to create a 10x10 chessboard pattern.


# 5. Challenge Task: Number Pyramid
# This prints a number pyramid where each row contains that row’s number.
rows = 5
for i in range(1, rows + 1):  # Outer loop controls rows
    for j in range(i):  # Inner loop controls repetition of numbers
        print(i, end=" ")  # Print number instead of "*"
    print()  # Moves to the next line

# Task 5: Modify the code to print a pyramid with numbers increasing in each row, like this:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


# 6. Extension Task 1: Diamond Pattern
# Modify the triangle pattern so that it prints a diamond shape.
# Example:
#     *    
#    ***   
#   *****  
#  ******* 
#   *****  
#    ***   
#     *    

# 7. Extension Task 2: Times Table Quiz
# Write a program that generates random multiplication problems using nested loops.
# Ask the user 5 questions and check if they get them correct.

# 8. Extension Task 3: Letter Grid
# Modify the number grid to print letters instead:
# A B C
# D E F
# G H I
# Hint: Use the chr() function and ASCII values.

