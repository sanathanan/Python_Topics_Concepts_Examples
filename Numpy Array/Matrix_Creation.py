# Matrix Creation

import numpy as np

# Creating Zero Matrix
a= np.zeros(5)
print(a)

a=np.zeros((2,4)) # If it is more than one row or column we need to give in tuples 
                  # i.e, placing the (2,4) inside () so ((2,4))
print(a)

# Creating Ones Matrix
a=np.ones(5)
print(a)

a=np.ones((5,1))
print(a)

# Creating a matrix multiple times
a=(np.ones((5,1,8))) # Creating 1X8 matrix 5 times.
print(a)

# Adding 5 to the one matrix
a=5+(np.ones((5,4)))
print(a)

# Finding the diagonal of the matrix
a=np.eye(4)
print(a)

# Constructing a Matrix
a=np.arange(16).reshape(-1,4)
print(a)
print(np.diag(a))
print(np.diag(np.diag(a)))
print(np.diag(a,k=-1)) # Printing the element below the diagonal element i.e, 4,9,14
print(np.diag(a,k=2)) # Printing the element above the diagonal element, i.e 2,7

# Priting the lower element in the matrix
a=np.tril([[1,2,3],[4,5,6],[7,8,9]], 0) # Above the diagonal element is printed with 0
print(a)

# Printing the upper element in the matrix
a=np.triu([[1,2,3],[4,5,6],[7,8,9]], 0) # Above the diagonal element is printed and lower the diagonal 
                                        # element is printed with 0
print(a)
