# function in python

# def greet():
#     print("Hello, user")

# greet()

# def greet(name = "User"):
#     print(f"Hello, {name} " )

# # greet("Nazmul Hossain")
# # greet(12)
# greet()

# Example of recursion: Calculating factorial of a number

# def factorial(n):
#     # Base case: if n is 0 or 1, return 1
#     if n == 0 or n == 1:
#         return 1
#     # Recursive case: n * factorial of (n-1)
#     else:
#         return n * factorial(n - 1)

# # Test the function
# number = 5
# print(f"The factorial of {number} is {factorial(number)}")

# Example of a lambda function: Doubling a number

# Lambda function to double a number
double = lambda x: x * 2

# Test the lambda function
number = 5
print(f"The double of {number} is {double(number)}")