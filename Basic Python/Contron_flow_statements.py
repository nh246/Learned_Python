# Example of if, elif, and else statements
# age = int(input("Enter your age: "))

# if age < 18:
#     print("You are a minor.")
# elif 18 <= age < 65:
#     print("You are an adult.")
# else:
#     print("You are a senior citizen.")

# for loop example

# foods = ["pizza", "burger", "pasta", "salad"]
# for food in foods:
#     print(f"I like {food}.")

#  while loop example

# Example of a while loop
# count = 0

# while count < 5:
#     print(f"Count is: {count}")
#     count += 1  # Increment the counter to avoid an infinite loop

# Example of break statement
# foods = ["pizza", "burger", "pasta", "salad"]

# for food in foods:
#     if food == "pasta":
#         print("Found pasta! Stopping the loop.")
#         break  # Exit the loop when "pasta" is found
#     print(f"I like {food}.")

#         # Example of continue statement
# for food in foods:
#     if food == "burger":
#         print("Skipping burger!")
#         continue  # Skip the rest of the code for this iteration
#     print(f"I like {food}.")

# Example of pass statement
foods = ["pizza", "burger", "pasta", "salad"]

for food in foods:
    if food == "pasta":
        # Placeholder for future code
        pass  # Do nothing for now
    else:
        print(f"I like {food}.")