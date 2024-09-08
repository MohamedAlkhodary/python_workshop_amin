#challange 4
def main():
    # Read two integers from standard input
    a = int(input("enter a number"))
    b = int(input("enter a number"))

    # Perform integer division and float division
    int_division = a // b
    float_division = a / b

    # Print the results
    print(int_division)
    print(float_division)


# Call the main function
if __name__ == "__main__":
    main()