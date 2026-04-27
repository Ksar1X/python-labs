from math import *


def multiple_arguments(*args):
    if len(args) > 100:
        raise ValueError("Too many arguments")

    for x in args:
        if not isinstance(x, int):
            raise TypeError("Argument must be an integer")


    result = [pow(x,2) for x in args]
    return result

userInput = str(input("Enter comma-separated numbers: "))

try:
    numbers = [int(x.strip()) for x in userInput.split(",") if x.strip()]
    output = multiple_arguments(*numbers)
    print(*output)
except ValueError:
    print("Error: Please enter valid numbers.")

