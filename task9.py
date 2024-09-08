import statistics


def calculate_mean(numbers):
    """
    Calculate the mean (average) of a list of numbers.

    Args:
    numbers (list of float): The list of numbers.

    Returns:
    float: The mean of the numbers.
    """
    if not numbers:
        raise ValueError("The list is empty.")
    return sum(numbers) / len(numbers)


def calculate_median(numbers):
    """
    Calculate the median of a list of numbers.

    Args:
    numbers (list of float): The list of numbers.

    Returns:
    float: The median of the numbers.
    """
    if not numbers:
        raise ValueError("The list is empty.")
    return statistics.median(numbers)


def calculate_mode(numbers):
    """
    Calculate the mode of a list of numbers.

    Args:
    numbers (list of float): The list of numbers.

    Returns:
    float: The mode of the numbers.
    """
    if not numbers:
        raise ValueError("The list is empty.")
    try:
        return statistics.mode(numbers)
    except statistics.StatisticsError as e:
        raise ValueError("No unique mode found. Error: " + str(e))


def calculate_range(numbers):
    """
    Calculate the range (difference between max and min) of a list of numbers.

    Args:
    numbers (list of float): The list of numbers.

    Returns:
    float: The range of the numbers.
    """
    if not numbers:
        raise ValueError("The list is empty.")
    return max(numbers) - min(numbers)


def calculate_variance(numbers):
    """
    Calculate the variance of a list of numbers.

    Args:
    numbers (list of float): The list of numbers.

    Returns:
    float: The variance of the numbers.
    """
    if not numbers:
        raise ValueError("The list is empty.")
    return statistics.variance(numbers)


def calculate_std(numbers):
    """
    Calculate the standard deviation of a list of numbers.

    Args:
    numbers (list of float): The list of numbers.

    Returns:
    float: The standard deviation of the numbers.
    """
    if not numbers:
        raise ValueError("The list is empty.")
    return statistics.stdev(numbers)


# Example usage
def main():
    data = [10, 20, 30, 40, 50]

    print("Data:", data)
    print("Mean:", calculate_mean(data))
    print("Median:", calculate_median(data))
    print("Mode:", calculate_mode(data))
    print("Range:", calculate_range(data))
    print("Variance:", calculate_variance(data))
    print("Standard Deviation:", calculate_std(data))


if __name__ == "__main__":
    main()
