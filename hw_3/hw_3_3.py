# Initial list
lst = [1, 2, 3, 4, 5, 6]

# Find the middle of the list
length = len(lst)
# Add 1 to make the first list larger in case of an odd number of elements
middle = (length + 1) // 2

# Divide the list into two parts
first_half = lst[:middle]
second_half = lst[middle:]

# Form the result
result = [first_half, second_half]

# Output the result
print(f"Result: {result}")
