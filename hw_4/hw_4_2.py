# Initial list with test data
test_data = [0, 1, 7, 2, 4, 8]

# Check if the list is not empty
if test_data:
    # Calculate the sum of elements with even indices
    even_index_sum = sum([test_data[idx] for idx in range(0, len(test_data), 2)])
    # Multiply by the last element of the list
    result = even_index_sum * test_data[-1]
else:
    # Here we just assign 0 since there is nothing to calculate
    result = 0

# Output the result
print(result)
