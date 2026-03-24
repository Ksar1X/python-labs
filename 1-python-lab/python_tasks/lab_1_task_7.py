## 7. Dla dowolnego x sprawdź wynik działań (x > 1 and x < 13) oraz (x != 5 or x < 0)

number = int(input("X= "))
if (number > 1) and (number < 13):
    if (number != 5) or (number < 0):
        print("True")
else:
    print("False")