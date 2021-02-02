# split() method returns a list of strings after breaking the given string by 
# the special separator

# Syntax: str.split(separator,Maxsplit)

# Example 1: splitting by spaces
text= "This is a Python Program"
txt = text.split(" ")
print(txt)

# Example 2: splitting by ","
text= "This,is,a,Python,Program"
txt = text.split(",")
print(txt)

# Example 3: splitting by ":"
text= "This:is:a:Python:Program"
txt = text.split(":")
print(txt)

# Example 4: splitting by "#"
text = "apple#banana#cherry#orange"
txt = text.split("#")
print(txt)


# Example 5a: splitting by "#"  (Maximum splitting up to 1)
text = "apple#banana#cherry#orange"
txt = text.split("#",1)
print(txt)

# Example 5b: splitting by "#" (Maximum splitting up to 2)
text = "apple#banana#cherry#orange"
txt = text.split("#",2)
print(txt)
