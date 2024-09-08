#challange 5

def main():
    # Read an integer from standard input
    n = int(input("enter a number"))

    # Print the square of all non-negative integers less than n
    for i in range(n):
        print(i ** 2)


# Call the main function
if __name__ == "__main__":
    main()