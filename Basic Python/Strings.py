#You can use double or single quotes:

print("Hello")
print('Hello')

a = "Hello"
print(a)

# You can use three double quotes:

a = """This is just a string 
that is inside a triple quote"""
print(a)

# with single quotes three single quotes:

a = '''This is just a string 
that is inside a triple single quote'''
print(a)

# Strings are Arrays
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

# However, Python does not have a character data type, a single character is simply a string with a length of 1.

# Square brackets can be used to access elements of the string.

# Get the character at position 1 (remember that the first character has the position 0):

b = "Hello, World!"
print(b[1])

# Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop.

# Example
# Loop through the letters in the word "BAngladesh":

for x in "BAngladesh":
  print(x)

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.

# Example
# Check if "free" is present in the following text:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# Use it in an if statement:

# Example
# Print only if "free" is present:  
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# Check if NOT
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

# Example
# Check if "expensive" is NOT present in the following text:
str = "The best things in life are free!"
print("expensive" not in str)

# Use it in an if statement:

# Example
# print only if "expensive" is NOT present:
txte = "The best things in life are free!"
if "expensive" not in txte:
  print("No, 'expensive' is NOT present.")









