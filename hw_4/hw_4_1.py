# Initial list with test data
test_data = [1, 0, 13, 0, 0, 0, 5]

# Pick all non-zero elements + the required number of zeros
result = [x for x in test_data if x != 0] + [0] * test_data.count(0)

# Output the result
print(result)
