# Iterators:
# Iterator can be created using "iter" keyword
# we can forloop and next() to iterate the values inside the lst/collection.
# Itertor is much more efficient

# Example 1: This is called Iterable.
# We are iterating the data inside the collection using for loop
lst=[1,2,3,4]
for i in lst:
    print(i)
    
# Example 2: # We are creating the iterator and iterating using for loop
lst=[1,2,3,4]
iterable = iter(lst) # creating iterator with the help of "iter" keyword
print(type(iterable)) # Printing the type of iterable
for i in iterable:
    print(i)
    
    
# Example 3: # We are creating the iterator and iterating using next()
lst=[1,2,3,4]
iterable = iter(lst) # creating iterator with the help of "iter" keyword
print(next(iterable)) # next() used to iterate the elements in the list by one by one. Once it finishing
# iterating all the values in the list, then it will throw an error message "StopIteration".
print(next(iterable))
print(next(iterable))
print(next(iterable))
try:
    next(iterable)
except StopIteration:
    print("No more elements in the list")



