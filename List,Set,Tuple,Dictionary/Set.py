# Set:
# Sets are an unordered collection of unique elements which can be constructed using the set() function.

# We cant able to find the index of the value. Because, it will change randomly


# Example 1:
# Display only unique elements  - will not display the same number more than once. 
# It will not support duplicate values
s = {1,1,4,2,6,7,7,4}
print(s)

# Example 2:
lst=[1,1,2,4,5,6,6,7,7,8,8,9,9,0] # List with multiple repeat elements
t=set(lst) # Converting list tp set to get the unique elements
print(type(t))
print(t)

