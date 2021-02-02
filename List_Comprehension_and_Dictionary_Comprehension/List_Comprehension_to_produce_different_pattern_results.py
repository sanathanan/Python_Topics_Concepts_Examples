"""
Implement List comprehensions to produce the following lists. 
# Write List comprehensions to produce the following Lists
['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz'] 
['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz'] 
[[2], [3], [4], [3], [4], [5], [4], [5], [6]]
[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

"""
# Program 1:
# Output: ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
lst ="ACADGILD"
lst_comp=[i for i in lst]
print(lst_comp)

# Program 2:
# Output: ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz'] 
lst =["x","y","Z"]
lst_comp=[i*num for i in lst for num in range(1,5)]
print(lst_comp)

# Program 3:
# Output: ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
lst =["x","y","Z"]
lst_comp=[num*i for num in range(1,5) for i in lst]
print(lst_comp)

# Program 4:
# Output: [[2], [3], [4], [3], [4], [5], [4], [5], [6]]
lst =[2,3,4]
lst_comp=[[i+num] for i in lst for num in range(0,3)]
print(lst_comp)

# Program 5:
# Output: [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
lst =[2,3,4,5]
lst_comp=[[i+num for num in range(0,4)] for i in lst]
print(lst_comp)

# program 6:
# Output: [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
lst=[1,2,3]
lst_comp=[(j,i) for i in lst for j in lst]
print(lst_comp)