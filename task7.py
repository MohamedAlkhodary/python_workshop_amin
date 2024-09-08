def check_same_type(items):
    if not items:  # If the list is empty, return True
        return True

    first_type = type(items[0])  # Get the type of the first item
    for item in items:
        if type(item) != first_type:
            return False
    return True


# Example1
sample_list_1 = [1, 2, 3, 4 ,8, 52, 510, 100, 1414, 10]  # All integers same type
# Example2
sample_list_2 = [1, 'amin', 3.5]  # Mixed types

print(sample_list_1,check_same_type(sample_list_1))  # Output: True

print(sample_list_2,check_same_type(sample_list_2))  # Output: False
