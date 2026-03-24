from headers import *
numbers = itertools.count(99, 5)

for i, value in zip(range(50), numbers):
    print(value)