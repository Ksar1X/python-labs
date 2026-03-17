from math import factorial

def my_factorial(user_value : int):
    return factorial(user_value)

def newtons_symbol(first_user_value : int, second_user_value : int):
    return my_factorial(first_user_value) / (my_factorial(second_user_value)*(my_factorial(first_user_value-second_user_value)))