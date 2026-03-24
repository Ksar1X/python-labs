from headers import *

list1 = [i for i in range(1, 100)]
list2 = [random.randrange(1, 100) for i in range(100)]

result_list = list(map(operator.sub, list1, list2))

print(result_list)




