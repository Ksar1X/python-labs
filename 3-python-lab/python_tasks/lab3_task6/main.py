from sil import *

while True:
    first_num = int(input("Enter first number: "))
    second_num = int(input("Enter second number: "))
    if first_num < second_num:
        print(f"{first_num} is less than {second_num}! Second number should be less than first number!")
        continue
    else:
        print(newtons_symbol(first_num, second_num))
        break

