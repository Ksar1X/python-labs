import pickle

def find_numbers(x=1, y=1):

    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError('x must be an integer')

    if x > y:
        x, y = y, x

    result = [num for num in range(x, y + 1) if num % 7 == 0 and num % 5 != 0]
    return result

def save_to_pickle(data, filename = "result.pkl"):
    try:
        with open(filename, "wb") as file:
            pickle.dump(data, file)
    except IOError as e:
        print(f"Error saving file: {e}")

def main():
    try:
        x = int(input("Enter x number: "))
        y = int(input("Enter y number: "))

        numbers = find_numbers(x, y)

        print(", ".join(map(str, numbers)))

        save_to_pickle(numbers)

    except ValueError as ve:
        print(f"Input error {ve}")
    except Exception as e:
        print(f"Type error {e}")

if __name__ == "__main__":
    main()



