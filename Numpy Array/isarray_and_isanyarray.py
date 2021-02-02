#isarray() and isanyarray()

import numpy as np

# "np.asarray()" # They have same memory location but the index of that value shares diffferent memory location
lst=[1,2,3,4,5,6]
a=np.array(lst) # Creating an array from lst
print("Printing the value of a: ",a)
b=np.asarray(a) # Copying the data from a to b
print("Copying the data from a to b: ",b)
b[0]=0 # Changing the value of b[0]
print("The value of b[0] changes from 1 to 0: ",b)
print("The value of a[0] also changes to the value of b[0]: ",a) # The value of a[0] also changes to the value of b[0]
print(id(a))
print(id(b))

# "np.asanyarray()" # They have same memory location but the index of that value shares diffferent memory location
lst=[1,2,3,4,5,6]
a=np.array(lst) # Creating an array from lst
print("Printing the value of a: ",a)
b=np.asanyarray(a) 
print("Reference Copy of the data from a to b: ",b) 
b[0]=0 # Changing the value of b[0]
print("The value of b[0] changes from 1 to 0: ",b)
print("The value of a[0] will not change from 1 to 0",a)
print(id(a))
print(id(b))
print(id(a[0]))
print(id(b[0]))