# Shallow Copying  and Deep Copying

import numpy as np

# Shallow Copying  - Refering to the same memory location
lst=[1,2,3,4,5,6]
a=np.array(lst) # Creating an array from lst
print("Printing the value of a: ",a)
b=a # Copying the data from a to b
print("Copying the data from a to b: ",b)
b[0]=0 # Changing the value of b[0]
print("The value of b[0] changes from 1 to 0: ",b)
print("The value of a[0] also changes to the value of b[0]: ",a) # The value of a[0] also changes to the value of b[0]
print("Memory location of a: ",id(a))
print("Memory location of b: ",id(b))


# Deep Copying  - Refering to the different memory location
lst=[1,2,3,4,5,6]
a=np.array(lst) # Creating an array from lst
print("Printing the value of a: ",a)
b=a.copy() #Reference copying the value of a to b.
print("Reference Copy of the data from a to b: ",b) 
b[0]=0 # Changing the value of b[0]
print("The value of b[0] changes from 1 to 0: ",b)
print("The value of a[0] will not change from 1 to 0",a)
print("Memory location of a: ",id(a))
print("Memory location of b: ",id(b))

