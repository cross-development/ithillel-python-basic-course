import random

# Generate a list of random numbers with a random length from 3 to 10
original_list = [random.randint(0, 100) for _ in range(random.randint(3, 10))]

# Create a new list from the first, third, and second elements from the end
new_list = [original_list[0], original_list[2], original_list[-2]]

# Output the original and new list
print("Original list: ", original_list)
print("New list: ", new_list)
