def common_elements() -> set:
    # Create a list of numbers that are multiples of 3
    multiples_of_three = set(x for x in range(100) if x % 3 == 0)

    # Create a list of numbers that are multiples of 5
    multiples_of_five = set(x for x in range(100) if x % 5 == 0)

    # Find the intersection of sets
    common = multiples_of_three.intersection(multiples_of_five)

    return common


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}, 'Test1'

print('ОК')
