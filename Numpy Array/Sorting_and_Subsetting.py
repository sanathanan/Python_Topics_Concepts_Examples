# Sorting

import numpy as np
from numpy import random as rd

# Sorting the numbers
a= rd.randint(1,100,30) # Creating a 30 elements between the numbers 1 to 100
b=np.sort(a) # Sorting the element of a using sort()
print(b)

# Creating a matrix from the sorted numbers
c=b.reshape(6,5) #  creating a 6X5 matrix from 30 elements
print(c)



print(c.argmax(axis=1)) # Index of the maximum element in a column

print(c.argmax(axis=0)) # Index of the maximum element in a row

print(c.max()) # Maximum element in a matrix
print(c.min()) # Minimum element in a matrix

# Subsetting

a=rd.randint(1,50,30).reshape(6,5)
print(a)

print(a>25) # Print True or False for the numbers present in the matrix greater than 25
print(a[a>25]) # Print the numbers present in the matrix greater than 25.
               # This is called Subsetting