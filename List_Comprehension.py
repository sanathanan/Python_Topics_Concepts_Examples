# List Comprehension  - It is a single line of code, the output will be in the form of list

#Example 1: (Ordinary List)
lst = [1,2,3,4,5,6,7]
lst1=[]

for i in lst:
    lst1.append(i**2)
    
print(lst1)


#Example 1a: The above program is writen using list_comprehension
lst=[1,2,3,4,5,6,7]

lst1 = [i**2 for i in lst] # Wrritngit single line of code  
 
print(lst1) 


# Example 2: Sum of even numbers inside a collection using list_comprehension
lst=[1,2,3,4,5,6,7,8,9,10]

lst1=[i for i in lst if i%2==0] # Getting the list inside forloop and checking the even number condition
                                # using "if" and getting the value of i
lst1=sum(lst1)
print(lst1)


# Example 3: Sum of odd numbers inside a collection using list_comprehension
lst=[1,2,3,4,5,6,7,8,9,10]

lst1=[i for i in lst if i%2!=0] # Getting the list inside forloop and checking the even number condition
                                # using "if" and getting the value of i
lst1=sum(lst1)
print(lst1)
    

