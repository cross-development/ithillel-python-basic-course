def add_one(some_list: list[int]) -> list[int]:
    # Convert a list of digits to a single number and add 1 to the number
    number = int(''.join(map(str, some_list))) + 1

    # Convert the number back to a list of digits
    return [int(digit) for digit in str(number)]


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'

print("ОК")
