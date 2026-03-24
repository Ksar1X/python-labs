from headers import *

def fun_cycle(n):
    seq = "INFORMATYKA"
    cycler = itertools.cycle(seq)

    for _ in range(n * len(seq)):
        print(next(cycler))

fun_cycle(2)