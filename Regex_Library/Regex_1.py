"""
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.

Need to import Regex using "import re"
"""

# Example 1:
# Search the string to see if it starts with "The" and ends with "Spain":
import re
txt="The world is not Spain"
x=re.search("^The.*Spain$", txt)
print(x)


