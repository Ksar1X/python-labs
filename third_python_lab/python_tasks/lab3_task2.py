nameAndSurname = input("Enter your name: ").split(" ")
print(nameAndSurname)
letters = lambda x:[list(i) for i in nameAndSurname]
print(letters(nameAndSurname))

