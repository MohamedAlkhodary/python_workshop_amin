import keyword


def is_valid_variable_name(name):
    """
    Check if the provided string is a valid Python variable name.

    Args:
    name (str): The string to check.

    Returns:
    bool: True if the string is a valid variable name, False otherwise.
    """
    if not isinstance(name, str):
        return False
    if not name.isidentifier():
        return False
    if name in keyword.kwlist:
        return False
    return True


# Example usage
print(is_valid_variable_name("my_variable"))  # True
print(is_valid_variable_name("2nd_variable"))  # False
print(is_valid_variable_name("import"))  # False
print(is_valid_variable_name("_valid_name"))  # True
