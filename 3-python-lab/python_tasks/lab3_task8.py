from functools import reduce
print("The product of multiplying numbers from 1 to 100:", reduce(lambda x,y:x*y,[i for i in range(1,100)]))