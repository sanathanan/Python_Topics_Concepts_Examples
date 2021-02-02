# Lambda Function Examples
# Lambda functioon is a anonymous function and it dont have any name
# Writing a function without the def keyword and function name. 
# instead of def keyword, need to specify the lambda fuction and passing the variable to compute the function

# Example 1: Using Lambda Function
num =[1,2,3,40]
result = list(map(lambda x: (((9/5)*x)+32), num))
print(result)

# Example 1a: Without using lambda function
def farenheit(num):
    return (float((9/5)*num) + 32)
     
num=[1,2,3,40]
l1=[]
for i in num:
    l1.append(farenheit(i))
print(l1)


# Note: map() function will be applied to lambda function. Because it will create the loops
# Example 2: Square of a given numbers in list using lambda Function
num=[1,2,3,4,5,6,7,8,9,10]
result = list(map(lambda x: x**2, num))
print(result)

# Example 2a: without lambda function
def square(num):
    return num*num
num=[1,2,3,4,5,6,7,8,9,10]
l1=[]
for i in num:
    l1.append(square(i))
print(l1)










