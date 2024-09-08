def reverse_list(fruits):
    reversed_list = []
    for i in range(len(fruits) - 1, -1, -1):
        reversed_list.append(fruits[i])
    return reversed_list
fruit_list = ["banana", "orange", "mango", "lemon"]
reversed_fruits = reverse_list(fruit_list)
print("Original List:", fruit_list)
print("Reversed List:", reversed_fruits)
