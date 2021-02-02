# Reduce Function
# we need to add library - "From functools import reduce"
# The reduce() will calculate the first two values and the output of first two will be 
# calculated with third value and it follows - Until it give the final single output

from functools import reduce

# Finding the Greatest value from the list
lst=[28,27,56,78,101,100,89]
greater = lambda a,b: a if(a>b) else b
greatest_Value = reduce(greater,lst)  # Reduce Function will take function_name and Iterable values
print("The Greater Value is", greatest_Value)



# Finding the Greatest value from the user input
num=int(input("Enter the number of numbers you need to enter: "))
lst=[]

for i in range(0,num):
    values=int(input("Enter the values: "))
    lst.append(values)
print("The input value is: ", lst)
greater = lambda a,b: a if(a>b) else b
greatest_Value = reduce(greater,lst)  # Reduce Function will take function_name and Iterable values
print("The Greater Value is", greatest_Value)
    
    


    
