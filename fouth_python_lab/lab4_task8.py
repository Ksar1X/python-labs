from headers import *

def numbers_generator(user_value):
    value = 4

    for _ in range(user_value):
        yield value
        value *= 4

print(list(numbers_generator(4)))

