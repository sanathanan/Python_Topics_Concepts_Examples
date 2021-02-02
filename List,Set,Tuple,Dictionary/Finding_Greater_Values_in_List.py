# Write a Python Program to implement your own myreduce() function which works exactly like 
# Python's built-in function reduce()

# reduce(function, sequence)
# Finding the greatest of values from the given list

# Import statement for reduce()
from functools import reduce

lst=[28,27,35,45,98,1098,987]
max_func=lambda a,b: a if (a>b) else b # lambda function

greatest_Value = reduce(max_func,lst) # using reduce function, passing the function and lst to 
                                      # find the greater values
print("The Greater value using reduce function is:",greatest_Value)


# Finding the greater value with out reduce()
# Method 1: (Using Sort())
lst=[28,27,35,45,98,1098,987]
lst = sorted(lst)
print("-------------Method 1 using sort()-------------------")
print(lst)
print("The Greater Value is: ", lst[-1])

# Method 2: (Using max())
lst=[28,27,35,45,98,1098,987]
print("-------------Method 2 using max()-------------------")
print("The Greater Value is: ", max(lst))

# Method 3: (Using for() and appending technique)
lst=[28,27,35,45,98,1098,987]
lst1=[]
for i in lst:
    lst1.append(i)
print("-------------Method 3 using for loop and appending values-------------------")
print("The Greater Value is: ", max(lst1))

# Method 4: Greatest of Number using defining function
def greater_fn(lst):
    
    # Assuming the first number in the list is max
    max = lst[0]
    
    for i in lst: # Iterating the values in the list
        if i > max: # Comparing the itertaed value with the max value defined above
            max = i # If iterated value is greater than max value, then assigning the iterated value to max   
    return max  # returning the max value
    
lst=[28,27,35,45,98,1098,987]
print("-------------Method 4 using function()-------------------")
print("The Greater Value is:", greater_fn(lst))

# Method 5: Sorted and for loop
num =[8,27,35,45,98,1098,987]
greater=sorted(num)
sum=0
for i in greater:
    if i>sum:
        sum=i
print("-------------Method 5 using sorted and for loop-------------------")
print("The Greater Value is:",sum)
    




