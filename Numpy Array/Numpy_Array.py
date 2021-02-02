# Numpy Array 
# Need to import numpy using "import numpy"


import numpy as np

# Creating an array
a= np.array([1,2,3])
print(type(a))
print(a)

# Creating an array with string and integer
a=np.array(["abc",1,2,3,"bcd"])
print(a)

#Creating a complex in array
a=np.array([1,2,3],dtype=complex) # dtype is used to create the complex variable
print(a)

a= np.array([(1,2),(3,4)],dtype=[('a','<i2'),('b','<i8')]) # dtype is used to create the complex variable
print(a)

# Creating a 3 dimensional array
a=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(a)

# Creating an array from list
lst=[[1,2,3],[4,5,6],[7,8,9]]
a=np.array(lst)
print(a)

