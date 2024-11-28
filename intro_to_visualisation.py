""" Analysis - Visualisation """

#importing required libraries
import matplotlib.pyplot as plt
import random

#generating a list of 10 random numbers
list1=[random.randint(0,100) for i in range(10)]

#creates a line graph
plt.plot(list1)

#shows the chart created
plt.show()

#adding labels
list1=[random.randint(0,100) for i in range(10)]
plt.plot(list1)
plt.title("Randomly Generated Numbers")
plt.xlabel("List Index")
plt.ylabel("Numbers Generated")
plt.show()

#Task 1: Create a list of 20 randomly generated numbers and create a line graph including labels 

#visulisation options
#add arguments for line style and colour
plt.plot(list1, "rs") #squares, no connecting lines
plt.show()

#task 2: experiment with other colours and line styles (b:,rs and bo). Comment what each style does

#working with 2 lists
list_names=["Tom", "Mary", "Joe", "John", "Jane"]
list_ages=[25, 37, 18, 45, 33]
plt.plot(list_names, list_ages, color="green")
plt.title("People's Ages")
plt.xlabel("Name")
plt.ylabel("Age")
plt.show()

#Task 3: create two lists (people's names, amount of siblings) and then create a line graph

#different plot types
#scatter plot
plt.bar(list_names, list_ages)
plt.title("People's Ages")
plt.xlabel("Name")
plt.ylabel("Age")
plt.show()

#task 4 - can you use the above code (making the necessary changes) to produce a scatter plot?

#pie chart
student_names=["Amy", "Ben", "Ciara", "Dan", "Elle"]
student_siblings=[2, 3, 3, 1, 2]
plt.pie(student_siblings, labels=student_names) #note the 'string' values are labels, numerical values are first argument
plt.title("Student Siblings")
plt.show()

#task5: create a pie chart for subjects and hours of classes per week (e.g. English - 4 hours, Comp Sci - 4 Hours, art - 3 hours, etc. )


#Displaying multiple data sets on the same graph
student_ages=[15,16,16,15,17]
plt.plot(student_names, student_siblings) #using lists from previous example
plt.plot(student_ages) #calling plt.plot twice for each data set
plt.xlabel("Students")
plt.legend(["Number of Siblings", "Age"]) #add a legend to show which line is which
plt.show()

#tasks page 89 of text book to be completed.




