import re


txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)


# .span()
print("---------.span()---------------")
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

# .string()
print("---------.string()---------------")
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)  # It returns the search string
print(x.string)

# .spain()
print("---------.spain()---------------")
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)  # It will search for the word start with S and it will print the whole word
print(x.group())