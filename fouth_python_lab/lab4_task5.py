from headers import *

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
bools = [True, False]

list1 = list(itertools.product(numbers, letters, bools))

print(list1)
