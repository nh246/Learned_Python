# Example of nested loops
# rows = 3
# columns = 4

# for i in range(1, rows + 1):  # Outer loop for rows
#     for j in range(1, columns + 1):  # Inner loop for columns
#         print(f"Row {i}, Column {j}", end="  ")
#     print()  # Move to the next line after each row

colors = ["red", "green", "blue"]
items = ["apple", "grape", "banana"]

for color in colors:
    for item in items:
        print(f"{color} {item}")