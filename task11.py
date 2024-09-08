#task11 part 1
def print_number_triangle_11():

    for i in range(1, 8):  # 1 to 7 inclusive
        for j in range(1, i + 1):
            print(j, end='')
        print()  # Move to the next line after printing each row

print_number_triangle_11()

#task11 part 2

def print_number_triangle_12():
    for i in range(1, 8):  # 1 to 7 inclusive
        for j in range(i, 0, -1):
            print(j, end='')
        print()  # Move to the next line after printing each row
print("   ")
print_number_triangle_12()

#task11 part 3
def print_star_pattern(rows):

    for i in range(rows):
        # Calculate the number of leading spaces
        leading_spaces = ' ' * i
        # Calculate the number of asterisks
        stars = '* ' * (rows - i)
        # Print the row with leading spaces and asterisks
        print(leading_spaces + stars.strip())


# Number of rows
num_rows = 6
print("  ")
print_star_pattern(num_rows)