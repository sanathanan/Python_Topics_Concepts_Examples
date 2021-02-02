# Random Number and Reshaping

from numpy import random as rd # Importing random from numpy

# Random Function

# Using rand function.
a=rd.rand(2,3) # Printing the 2 rows and 3 columns with the number from 0 to 1 
print(a)


# Using randn function.
a=rd.randn(2,3) # Printing the 2 rows and 3 columns with the number from 0 mean to Standard deviation 1
print(a)

# Using randint function
a= rd.randint(1,50,(4,4)) # Creating a 4X4 matrix with the numbers from 1 to 50
print(a)


a= rd.randint(1,5,20) # Creating a 20 elements in a row with numbers from 1 to 5
print(a)


# Reshaping

a=rd.randint(1,50,30)
print(a)
b=a.reshape(6,5) # Printing the 30 elements of a in 6X5 matrix
print(b)
c=a.reshape(2,3,5)# Printing the 30 elements of a in 2X5 matrix 2 times
print(c)