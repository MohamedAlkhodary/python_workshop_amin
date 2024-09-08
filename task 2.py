import random
from collections import Counter

def generate_random_list(size, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

def find_duplicates(numbers):
    # Count occurrences of each number
    counts = Counter(numbers)
    # Extract duplicates (numbers that appear more than once)
    duplicates = [num for num, count in counts.items() if count > 1]
    return duplicates

# Generate a random list of 30 numbers between 1 and 100
random_list = generate_random_list(30, 1, 100)
print("Random List:", random_list)

# Find and print duplicates
duplicates = find_duplicates(random_list)
print("Duplicate Numbers:", duplicates)