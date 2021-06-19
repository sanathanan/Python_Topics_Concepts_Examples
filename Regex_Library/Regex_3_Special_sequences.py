import re

# \A -- Returns a match if the specified characters are at the beginning of the string
print("----------------\A-------------------------")
txt = "The rain in Spain"
x=re.findall("\AThe",txt)
print(x)
if x:
    print("There is a match")
else:
    print("There is No Match")

# \b -- Returns a character that is beginning or at the end of the word
        # (r in the beginning will ensure that the string will be treated as raw string)
print("----------------\b-------------------------")
txt = "The rain in Spain"
x=re.findall(r"\bra",txt) # checking the string that is present at the beginning of the word
print(x)

txt = "The rain in Spain"
x=re.findall(r"ain\b",txt) # checking the string that is present at the beginning of the word
print(x)


# \B --Returns a match where the specified characters are present. Not at the beginning or at end of the woord.
     # It just checks whether the the character is present or not.
    # the r in the beginning will ensure that the string is a raw string
print("----------------\B-------------------------")
txt = "The rain in Spain"
x=re.findall(r"\Bai",txt) # it is checking the specified string
print(x)

txt = "The rain in Spain"
x=re.findall(r"\BTh",txt) # It will not check if it is present in starting or end of the word
print(x)
if x:
    print("There is a match")
else:
    print("Not a Match")

# \d -- returns a string that contains digits from 0 to 9
print("----------------\d-------------------------")
txt = "The rain in Spain"
x=re.findall("\d",txt)
print(x)

txt = "The rain123 in Spain"
x=re.findall("\d",txt)
print(x)

# \D -- returns a string that does not contains any digits
print("----------------\D-------------------------")
txt = "The rain in Spain"
x=re.findall("\D",txt)
print(x)

txt = "The rain123 in Spain"
x=re.findall("\D",txt)  # Its not printing 123.
print(x)

# \s -- returns a match where the string contains a white space character
print("----------------\s-------------------------")
txt = "The rain in Spain"
x=re.findall("\s",txt)
print(x)

# \w - Returns a match where the string contains any word characters (a-z, A-Z, 0-9, _)
print("----------------\w-------------------------")
txt = "The rain in_ Spain123"
x=re.findall("\w",txt)  # it wil remove the white space and it will print all the characters
print(x)

# \W - Returns a match where the string doesnot contains any word characters (a-z, A-Z, 0-9, _)
print("----------------\W-------------------------")
txt = "The rain in_ Spain123!"
x=re.findall("\W",txt)  # it wil print the white space and it will print the varaible that is not part of characters
print(x)

# Z --Returns a match at the end of the string
print("----------------\Z-------------------------")
txt = "The rain in_ Spain123!"
x=re.findall("Spain123!\Z",txt)
print(x)