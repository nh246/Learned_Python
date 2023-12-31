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


'''Slicing
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string. '''

g = "Hello, World!"
print(g[2:5]) 

'''Slice From the Start
By leaving out the start index, the range will start at the first character:

Example
Get the characters from the start to position 5 (not included):'''

h= "Hello, World!"
print(h[:5])

j = "Hello, World!"
print(j[2:])

'''Negative Indexing
Use negative indexes to start the slice from the end of the string:
Example
Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):'''

lb = "Hello, World!"
print(lb[-5:-2])



'''Upper Case
The upper() method returns the string in upper case:'''

an = "Hello, World!"
print(an.upper())

'''The lower() method returns the string in lower case:'''


low = "Hello, World!"
print(low.lower())

'''Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

Example
The strip() method removes any whitespace from the beginning or the end:'''


str = " Hello, World! "
print(str.strip())

'''The replace() method replaces a string with another string:'''


rep = "Hello, World!"
print(rep.replace("H", "J"))

'''The split() method splits the string into substrings if it finds instances of the separator:'''


spl = "Hello, World!"
print(spl.split(","))




'''But we can combine strings and numbers by using the format() method!

The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are: '''

'''Use the format() method to insert numbers into strings:
'''


age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

'''The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

Example
'''

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

'''You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:'''


quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

'''Escape Character
To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
you use double quotes inside a string that is surrounded by double quotes:'''


'''To fix this problem, use the escape character \":

Example
The escape character allows you to use double quotes when you normally would not be allowed:'''


txt = "We are the so-called \"Vikings\" from the north."

















































































