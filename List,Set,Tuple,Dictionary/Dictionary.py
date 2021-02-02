# Dictionary
# Dictionary helps to do mapping. It contains "Key" and "Value" pairs.

# Example 1:
# Creating the dictionary
t={}  #  Creating the empty dictionary
print(type(t)) # Type of Dictionary
t["name1"]="Sanath" # Adding data to the dictionary
t["name2"]= "Thangaraj"
print(t) # Output of the data in the dictionary

# Example 2: Dictionary data elements
d={"num":123, "key1":[1,2,3], "Vegetables":["Carrot","Onion","Tomato","Cucumber"]}
print("-----Printing the data in num-------------")
print(d["num"])
print("-----Printing the data in key1 of index 1-------------")
print(d["key1"][1])
print("-----Printing the data in vegetabkes of index 2-------------")
print(d["Vegetables"][2])
print("-----Printing the data in vegetabkes of index 1 and converting to Upper case-------------")
print(d["Vegetables"][1].upper())
print("-----changing the data of key1 of the index o element -------------")
d["key1"][0]=1234
print(d["key1"])
print("-------Printing only the keys in the dictionary")
print(list(d.keys()))
print("-----------Printing only the values in the dictionary")
print(list(d.values()))


# Example 3: # Nesting with Dictionaries
d={"key1":{"key2":{"key3": [1,2,3,4,5,6,7,7]}}}
print(" -------------Nesting with Dictionaries ---------------")
print(d["key1"]["key2"]["key3"])

