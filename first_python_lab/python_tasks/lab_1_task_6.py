## 6. Utwórz prosty kalkulator dla 2 zmiennych podanych przez użytkownika, który obliczy: sumę, różnicę,
## iloczyn, iloraz, potęgę tych liczb, nie zapomnij o stosownych komentarzach informacyjnych dla użytkownika.

example = str(input()).split(" ")
if example[1] == "+":
    print("Suma:", int(example[0]) + int(example[2]))
elif example[1] == "-":
    print("Roznica:", int(example[0]) - int(example[2]))
else:
    print("Error!")