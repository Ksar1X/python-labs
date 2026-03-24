## 3. Wyświetl zdanie "Jestem a b mam c lat studiuję d",
##  gdzie : a-imie, a-nazwisko, c-liczba, d-kierunek studiów są dowolne zmienne które podaje użytkownik (wczytywane z klawiatury)


name = str(input("Name: "))
surname = str(input("Surname: "))
age = int(input("Age: "))
fieldOfStudy = str(input("Field of study: "))
print(f'Jestem {name} {surname} mam {age} studiuje {fieldOfStudy}')