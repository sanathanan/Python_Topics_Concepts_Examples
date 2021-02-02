# Tuples
# Tuples are like list and they are immutable data. We cannot able to change the values 
# in the tuples.
# When we need the data or constants that need not be changed, the we can use Tuples()

# Exampl 1: Tuple syntax and type
t=(1,2,3)
print("----------Data Type ----------------------")
print(type(t))
print("--------Printing the Data in Tuple ---------------------------")
print(t)

# Example 2: 
t=("Hari","Abhi", "Anu")
print("--------Printing the Data in Tuple ---------------------------")
print(t)
print("--------Printing data of the index 0 element ---------------------------")
print(t[0])
# t[0] = "AAnu"   we cannot able to change the data in the tuple. It will throw an error
#t.append("AAnu") # We cannot able to add the new data to the existing data in the tuple
#print(t)

# Example 3:
t=("Hari","Abhi", "Anu")
result = [i for i in t] # Printing the data using list comprehension
result1= [i for i in t][: : -1] # reversing the data from last to first
result2= [i[: : -1] for i in t][: : -1] # reversing the data and character from last to first
print("--------Printing the data using list comprehension ---------------------------")
print(result)
print("--------Reversing the data from last to first ---------------------------")
print(result1)
print("--------Reversing the data and character from last to first ---------------------------")
print(result2)


# Example 4 : Count and Index Example
num=[1,2,3,4,7,5,6,66,7,7,7,7,7]
result = num.count(7)
print("-------Printing the count funtionality ------------")
print(result)
result1 = num.index(7) # It will diaplay the index value of first encountering number of 7
print("-------Printing the index funtionality ------------")
print(result1)