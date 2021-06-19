# [] set of characters
import re
print("------------Example of []-----------------")
txt = "The rain in Spain"

x= re.findall("[a-m]", txt) # Finding the lower case alphabets between a and m
y=re.findall('[a-z]', txt) # Finding the lower case alphabets
z=re.findall('[A-Z]', txt) # Finding the upper case alphabets

print(x)
print(y)
print(z)


# \ -- Signals a special sequence. It is also used to escape special character
print("------------Example of \   -----------------")
txt = "That will be 652 dollars"
x = re.findall("\d", txt)  # \d returns the string contains 0-9
print(x)
y = re.findall("[0-9]", txt)  # The above pattern can be written like this also
print(y)

# . ---- Any Character except a new line character
print("------------Example of .   -----------------")
txt
txt = "hello world"
x = re.findall("he..o",txt) # Printing the letter starts with he and two charcters and end with o
print(x)
y=re.findall('he.*d',txt) # Printing the letter start with he and mulitple occurance of character and end with d
print(y)
z=re.search("^h.*d$",txt) # Printing the letter start with he and mulitple occurance of character and end with d using search()
print(z)


# ^ --- Starts with
print("------------Example of ^   -----------------")
txt
txt = "hello world"
x = re.findall("^hello",txt)
if x:
    print("The string matches")
else:
    print("Not Matches")

txt = "hello world"
x = re.findall("^h.*",txt)  # We are printing the string that starts with h followed by multiple occurance of charater
print(x)

# $ -- Ends with
print("------------Example of $   -----------------")
txt
txt = "hello world"
x = re.findall("world$",txt)
if x:
    print("The string matches with end word")
else:
    print("Not Matches")

txt = "hello world"
x = re.findall("^h.*d$",txt)
print(x)

# * -- Zero or more occurances
print("------------Example of *   -----------------")
txt
txt = "The rain in Spain falls mainly in the plain!"

x = re.findall("ai.*",txt)
print(x)

txt = "The rain in Spain falls mainly in the plain!"
x = re.findall("aix*",txt) # checking for the string contains ai followed by 0 or x characters.. * is for multiple occurance
print(x)

# + -- One or more occurances
print("------------Example of +   -----------------")
txt
txt = "The rain in Spain falls mainly in the plain!"
x= re.findall("aix+", txt)
print(x)

# { } - Exactly specified number of occurances
print("------------Example of { }   -----------------")
txt
txt = "The rain in Spain falls mainly in the plain!"
x=re.findall("al{2}",txt)  # Printing the string that start with al followed by 2 no of characters
print(x)

# | -- Either or
print("------------Example of |   -----------------")
txt
txt = "The rain in Spain falls mainly in the plain!"
x=re.findall("Spain|stays",txt)
print(x)
if x:
    print("There is atleast 1 match")
else:
    print("No Match")