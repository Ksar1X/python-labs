## 5. Sprawdź czy suma dowolnych dwóch liczb podanych przez użytkownika jest liczbą parzystą czy nieparzystą wyświetl właściwy komunikat
##   użyj operatora modulo % który zwraca resztę z dzielenia  np. 5%2   czyli 2 reszta 0

if (int(input("First number: ")) + int(input("Second number: "))) % 2 == 0:
    print("Yes")
else:
    print("No")