# Generators - It is really used inorder to create the iterator
# Generator uses "yield" keyword to create a generator. which is eventually creating the iterator
# The "yield" keyword store the local variable and returns the variable
# Generator helps us to write fast and compact code.


# Example 1: squaring the number without genertor function.
def square(n):
    for i in range(n):
        return i**2
    
result = square(3)
print("-----Printing without Genertor function-----------")
print(result)  # It's only returns the first value. Its not iterating.


# Example 2a: squaring the number with the help of genertor function.
def square(n):
    for i in range(n):
        yield i**2  # Generator uses yield keyword, which is creating the itertor
    
result = square(3)
print("------Printing the Generator object--------------")
print(result) # It is creating the genertor obkject which is iterable

# Example 2b:
def square(n):
    for i in range(n):
        yield i**2
    
result = square(3)
print("---------Printing the Generator object using for loop---------------")
for i in result: # we are iterting the generator object using for loop
    print(i)
    
# Example 2c: squaring the number with the help of genertor function.
def square(n):
    for i in range(n):
        yield i**2  # Generator uses yield keyword, which is creating the itertor
    
result = square(3)
print("---------Printing the Generator object using next()---------------")
print(next(result)) # we are iterting the generator object using next()
print(next(result))
print(next(result))
try:
    next(result)
except StopIteration:
    print("Iteration is completed")
    
# Example 3: Cube of numbers
def get_Cubes(n):
    for i in range(1,n+1):
        yield i**3
        
result = get_Cubes(10)
print("---------Printing the cube of a numbers using forloop---------------")
for i in result:
    print(i)



