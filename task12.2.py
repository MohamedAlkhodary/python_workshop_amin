#challange 2
import math
import os
import random
import re
import sys
def evaluate_integer(n):

    if n % 2 != 0:
        # n is odd
        print("Weird")
    elif 2 <= n <= 5:
        # n is even and in the range [2, 5]
        print("Not Weird")
    elif 6 <= n <= 20:
        # n is even and in the range [6, 20]
        print("Weird")
    elif n > 20:
        # n is even and greater than 20
        print("Not Weird")
    else:
        # This else is technically not necessary for this problem as all cases are covered
        print("Unspecified condition")

n = int(input("enter a number: "))
evaluate_integer(n)
