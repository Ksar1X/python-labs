from headers import *

def initial_amount(k, interest_rate, period):
    countOfPeriod = period // 3

    factors = [1 + interest_rate] * countOfPeriod
    values = list(itertools.accumulate(factors, operator.mul))

    return k * values[-1] if values else k

result = initial_amount(10000, 0.05, 9)

print(result)
