from headers import *


numbers = [random.randrange(1, 10000) for i in range(10000)]
resultNumbers = list(filter(lambda x: x % 2 == 0 and x < 3, numbers))

print(resultNumbers)