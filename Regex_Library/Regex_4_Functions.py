import re

# findall()  -- Returns a list contains all matches
print("---------findall()-----------------")
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

# search() -- This function search for a match and returns the match object if there is a match
# If there is morethan one match, then only the first occurance of the match will be returned
print("---------search()-----------------")
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

# split() --It returns a list where the string has been split at each match
print("---------split()-----------------")
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

#sub() --It replace the matches with the text of our choice
print("---------sub()-----------------")
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)  # Replacing the space with 9
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2) # we are substituting the white space with 9 for 2 times
print(x)


