import string

# Receive input from the user
user_input = input("Enter two letters separated by a hyphen (e.g., a-c): ")

# Split the input string into two parts
start, end = user_input.split('-')

# Get a list of all letters (uppercase and lowercase)
all_letters = string.ascii_letters

# Find the indices of the starting and ending letters
start_index = all_letters.index(start)
end_index = all_letters.index(end)

# Select all characters between these indices inclusive
result = all_letters[start_index:end_index + 1]

# Output the result
print(result)
