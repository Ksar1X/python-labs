numbers = []

for i in range(1, 1001):
    s = str(i)
    allEven = True

    for digit in s:
        if int(digit) % 2 != 0:
            allEven = False
            break

    if allEven:
        numbers.append(s)

print(",".join(numbers))