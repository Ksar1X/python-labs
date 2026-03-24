for i in range(1000):
    x = input("First number: ")
    y = input("Second number: ")

    if not (x.lstrip('-').isdigit() and y.lstrip('-').isdigit()):
        print("Please provide only whole numbers!")
        continue

    x = int(x)
    y = int(y)

    if x == 0 or y == 0:
        print("Programme completed.")
        break

    result = x * y
    print("The product is:", result)