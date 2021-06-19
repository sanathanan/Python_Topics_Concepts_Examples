# A set is a set of characters inside a pair of square brackets with a special meaning
import re

#[arn]-- returns a match if one of the specified chatacter are present
print("---------[arn]--------------------------")
txt = "The rain in Spain"
x=re.findall("[ra]",txt)
print(x)

#[a-n]  --Returna a lowercase character, alphabetically between a to n
print("---------[a-n]--------------------------")
txt = "The rain in Spain"
x=re.findall("[a-i]",txt)  # Printing the characters between a to i
print(x)

#[^arn] --Returns a match for any character Exvcept a,r and n
print("---------[^arn]--------------------------")
txt = "The rain in Spain"
x=re.findall("[^ra]",txt)  # we are not printing the character r and a
print(x)

#[0123] --Returns a match if any of the specified digits are present or not
print("---------[0123]--------------------------")
txt = "The rain in Spain 1 23 34"
x=re.findall("[1234]",txt)
print(x)

# [0-9]  -- Returns a match for any digit between 0 to 9
print("---------[0-9]--------------------------")
txt = "The rain in Spain234 12334"
x=re.findall("[0-9]",txt)
print(x)

# [0-5][0-9] -- Returns a match for any 2 digit number from 00 to 59
print("---------[0-5][0-9]--------------------------")
txt = "8 time before 11.45 am"
x=re.findall("[0-5][0-9]",txt)
print(x)

# [a-zA-Z] -- Returns a match for any character between a to z in lowercase and upper case
print("---------[a-zA-Z]--------------------------")
txt = "8 time before 11.45 am"
x=re.findall("[a-z A-Z]",txt)
print(x)

# [+] -- In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
print("---------[+]--------------------------")
txt = "8 time before 11.45 am"
x=re.findall("[+]",txt)
print(x)

txt = "8 time before+ 11.45 am"
x=re.findall("[+]",txt)
print(x)