numbers = range(1, 100)
evenNumbers = filter(lambda x: x % 2 == 0, numbers)
print(", ".join(map(str, evenNumbers)))

