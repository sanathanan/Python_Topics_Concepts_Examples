# Filter Function Example - Using lambda function:
lst=[1,2,3,4,5,6,7,8,9,10]
even_function= (lambda x: x%2==0)
num =filter(even_function,lst)
print(list(num))

# Filter function Example - Using  Function
def even_function(lst):
    if lst %2 ==0:
        return True
    
lst=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(even_function,lst)))


# Filter working principle with the help of def func
def even_function(lst):
    lst1=[]
    for i in lst:
        if i%2 ==0:
            lst1.append(i)
    return lst1
    
lst=[1,2,3,4,5,6,7,8,9,10]
print(even_function(lst))

# Filter working principle with the help of list_comprehension
lst=[1,2,3,4,5,6,7,8,9,10]
even=[i for i in lst if i%2 ==0]
print(even)


# Filter working principle with the help of for loop
lst=[1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i%2 ==0:
        print(i, end=" ")
        

        
        