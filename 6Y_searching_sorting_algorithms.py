"""
6th Year Computer Science

Algorithms: Searching and Sorting Algorithms

Searching algorithms search something (e.g a list) for a given item
- Linear Search
- Binary Search

Sorting algorithms sort something (e.g a list) into a particular order
- Selection Sort
- Insertion Sort
- Bubble Sort
- Quicksort
"""

#----------------------------------------------------------------------------------------------

#Linear Search
""" A linear search algorithm iterates (loops) through each item in a list one at a time, comparing
it to the key. 

Analogy:
Imagine you’ve lost a word in a book and you don’t know which page it’s on.
-You start at page 1, check it, then go to page 2, then page 3, and so on — one page at a time until you find the word.
-You don’t skip any pages
-You might reach the end of the book if the word isn’t there
-This works even if the pages are out of order
"""

list_1=[10, 15, 70, 4, 28, 90]
key=28
for i in range(len(list_1)):
    if list_1[i]==key:
        location=i
print(f"Key found at: {location}")

#this is a pre made python function: .index()
print("Key found at:", list_1.index(28))


#problems: duplicate items, or the item is not there
list_2=[10,15,70,4,28,90,15]
key_2=15
for i in range(len(list_1)):
    if list_1[i]==key_2:
        location=i
print(f"Key found at: {location}") #only the first index location is found

#print(list_2.index(120)) #gives an error

#solution
list_2 = [10, 15, 70, 4, 28, 90, 15]
key_2 = 15

# create an empty list to store all matching index positions
locations = [] #initialise an empty list to store the index locations

for i in range(len(list_2)):
    if list_2[i] == key_2:
        locations.append(i)  #append the list to add in the locations

if len(locations) >0: #can also be written as if locations: 
    print(f"Key found at indices: {locations}")
else:
    print("Key not found")
    
"""Advantages and limitations of linear search algorithms:

Definition:
Checks each item in a list one by one from start to end until the target item is found (or until the list ends).

✅ Advantages
-Simple to understand and implement — great for beginners.
-Works on unsorted lists — no need to arrange data first.
-Can find multiple matches if you keep searching through the whole list.
-Good for small lists — performance is acceptable when the list is short.

⚠️ Limitations
-Slow for large lists — checks each item, so time grows as the list gets bigger (O(n) time complexity).
-Inefficient compared to other algorithms (like binary search) when the list is sorted.
-Does not stop early unless programmed to — will check the whole list even if the item is near the end (unless you break after finding it).
-More comparisons needed on average compared to more advanced search algorithms. """

#--------------------------------------------------------------------------------------------------

#Binary Seach algorithms
"""Definition:
Binary search repeatedly divides the sorted list in half to find the target item.
Instead of checking every element, it eliminates half of the remaining items each time.

Analogy:
You want to find the word “Tiger” in a dictionary.
You open the middle of the dictionary
If you see “Monkey”, you know “Tiger” comes after, so you ignore the first half
Then you open the middle of the second half
Each time you open to the middle, you halve the search space until you find “Tiger”
You skip huge sections quickly
This only works because the dictionary is sorted alphabetically"""

# Start with an unsorted list
list_1 = [10, 15, 70, 4, 28, 90]

# Binary search only works on a SORTED list
list_1.sort()
print(list_1)  # [4, 10, 15, 28, 70, 90]

def binary_search(list_, key):
    # first = index of the first item in the current search range
    # last = index of the last item in the current search range
    first = 0
    last = len(list_) - 1

    # Keep looping as long as there is still a range to search
    while first <= last:
        # Find the middle index of the current range
        middle = first + ((last - first) // 2)

        # If the middle item is the key, return its index
        if list_[middle] == key:
            return middle
        
        # If the key is LESS than the middle item,
        # search only the LEFT half (update 'last')
        elif key < list_[middle]:
            last = middle - 1
        
        # Otherwise, the key is GREATER than the middle item,
        # so search only the RIGHT half (update 'first')
        else:
            first = middle + 1

    # If we exit the loop, the key is not in the list
    return -1

# Test the function
print(binary_search(list_1, 15))  # Output: 2

"""⚡ Binary Search Algorithm
✅ Advantages
-Much faster than linear search on large lists — it cuts the list in half each step (O(log n) time complexity).
-Fewer comparisons needed, especially as the list gets bigger
-Efficient for repeated searches on the same sorted data (e.g. searching a phonebook or dictionary many times).
-Scales well — works well even on very large datasets.

⚠️ Limitations
-List must be sorted — if the data is not sorted, you must sort it first (which takes extra time).
-More complex to understand and implement than linear search.
-Not suitable for small lists — the time saved is minimal, and linear search can be simpler.
-Only works on random-access data structures like lists or arrays — not suitable for things like linked lists without extra steps.
"""

#EXAM Q: 2025 Q7 A

#------------------------------------------------------------------------------------------------------------


#Selection Sort
"""
Selection sort is a sorting algorithm that works by repeatedly finding the smallest (or largest) item from the unsorted part of the list and moving it to the front.
It gradually builds a sorted section at the start of the list.

How It Works (Step by Step):
-Start at the first index
-Find the smallest item in the entire list
-Swap it with the first item
-Move to the next index and
-Find the smallest item in the remaining unsorted part
-Swap it into place
-Repeat until the list is sorted
"""

list_1 = [10, 15, 70, 4, 28, 90]

for i in range(len(list_1)-1):
    print("Pass", i, ":", list_1)
    
    # find smallest value in the unsorted part (i+1 to end)
    next_min_value = min(list_1[i+1:])
    
    # only swap if it's smaller than the current item
    if next_min_value < list_1[i]:
        # find the index of the smallest value, starting from i+1
        next_min_index = list_1.index(next_min_value, i+1)
        
        # swap
        list_1[next_min_index] = list_1[i]
        list_1[i] = next_min_value

print("Sorted:", list_1)

"""
✅ Advantages:
- Simple to understand and implement (good for learning sorting)
- Works on any type of data (numbers, strings, etc.)
- Does not need extra memory (sorts in-place)
- Uses few swaps (at most one swap per pass)

⚠️ Limitations:
 - Very slow on large lists (O(n^2) time complexity)
 - Inefficient compared to algorithms like merge sort or quicksort
 - Not stable (equal values can change order)
 - Does not stop early even if the list becomes sorted before the end   
  """  
    
    
   
"""
Note:
using for i in range(len(list)) vs len(list)-1

for i in range(len(list_)-1):	
-Stops at second-last index	
-Efficient — no unnecessary pass	
-Standard for selection sort	

for i in range(len(list_)):
-Goes to the last index
-Does one useless extra pass
-Technically works but unnecessary
"""