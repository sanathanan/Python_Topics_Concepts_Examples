#Arange and LinSpace

import numpy as np

#Arange()
a= np.arange(5,16,2) # Giving the starting,ending and step value
print(a)
a= np.arange(5,16,2.5)
print(a)

a=np.arange(50,-1,-5) # Is printing the numbers from 50 to -1 with step=-5
print(a)

# Lin Space
num = np.linspace(1,5,50) # Printing the Linear spaced numbers from 1 to 5 with 50 steps. 
                          # 50 is we need 50 steps between the number from 1 to 5
print(num)