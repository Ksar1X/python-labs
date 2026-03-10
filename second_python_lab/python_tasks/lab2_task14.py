def divide_three_even_numbers(a, b, c):
    if not (a % 2 == 0 and b % 2 == 0 and c % 2 == 0):
        return "Error: All three numbers must be even!"

    if b == 0 or c == 0:
        return "Error: The divisor cannot be zero!"

    result = a / b / c
    return result


print(divide_three_even_numbers(12, 4, 2))
print(divide_three_even_numbers(20, 2, 5))
print(divide_three_even_numbers(10, 3, 2))
print(divide_three_even_numbers(12, 0, 2))
