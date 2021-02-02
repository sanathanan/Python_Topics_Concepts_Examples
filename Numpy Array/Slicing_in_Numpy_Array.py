# Slicing
import numpy as np

#Printing 4,7,6,9 from the 3X3 Matrix
lst=[[1,2,3],[4,5,6],[7,8,9]]
a=np.array(lst)
print(a)
slicing=a[1:3,0:3:2]  # 1:3 is row and 0:3:2 is column with step 2
print(slicing)

#Printing 5,8,9,12 from the 4X4 Matrix
lst=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
a=np.array(lst)
print(a)
slicing=a[1:3,0:4:3]  # 1:3 is row and 0:4:3 is column with step 3
print(slicing)

#Printing 1,4,13,16 from the 4X4 Matrix
lst=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
a=np.array(lst)
print(a)
slicing=a[0:4:3,0:4:3]  # 0:4:3 is row with step 3 and 0:4:3 is column with step 3
print(slicing)

