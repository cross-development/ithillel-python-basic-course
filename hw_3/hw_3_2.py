# Test data
test_data = [12, 3, 4, 10, 8]

# Transforming the initial list
result = [test_data[-1]] + test_data[:-1] if len(test_data) > 1 else test_data

# Output the initial list
print(f"Initial list: {test_data}")

# Output the result
print(f"Transformed list: {result}")
