import math

def calculator():
    try:
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))

        assert second_number != 0, "Second number must be entered"
        result = first_number + second_number
        print(f"Result of {first_number} / {second_number}: {result}")

        assert first_number > 0, "first_number must be greater than 0"
        result = math.sqrt(first_number)
        print(f"Result of sqrt({first_number}) : {result}")

    except ValueError:
        print("Please enter a number!")
    except ZeroDivisionError:
        print("Second number must be entered!")
    except TypeError:
        print("Please enter a number!")
    except AssertionError as e:
        print(f"Logical error: {e}")
    except Exception as e:
        print(f"Something went wrong! {e}")

calculator()
