# Map is a function that takes 2 arguments:
    # Function
    # Sequence (iterable)
    # map(funtion_name, sequence(iterbale))
    
# Example 1:Finding the temperature in Fahrenheit Without Map Function
def fahrenheit(i):
    return (float(9/5)*i + 32)

temp=[10,20,30,40]
l1=[]
for i in temp:
    l1.append(fahrenheit(i))
print(l1)


# Example 1: Finding the temperature in Fahrenheit with Map Function
def fahrenheit_fn(i):
    return (float(9/5)*i + 32)

temp=[10,20,30,40]

fahrenheit_fn = list(map(fahrenheit_fn,temp))
print(fahrenheit_fn)


