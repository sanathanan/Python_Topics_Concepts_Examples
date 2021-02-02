# Greatest of values from the list

# Lambda function and reduce function to find the greatest of Values from the list
from functools import reduce

num =[10,20,100,40,50]
result=reduce(lambda x,y: max(x,y),num)
print(result)

# Lambda function and reduce function to find the greatest of Values from the list - Another way
from functools import reduce

num =[10,20,100,40,50]
greter_function = lambda x,y: x if x>y else y
result=reduce(greter_function,num)
print(result)




