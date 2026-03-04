# 1. Wykonaj mini ankietę tj. poproś użytkownika o następujące informacje: imie, nazwisko, wiek, zadaj mu pytania: "Czy zdrowo się odżywiasz?",
# , "Czy lubisz sport?" i dodatkowo 3 inne własne. Po uzyskaniu wszystkich odpowiedzi wyświetl ich podsumowanie.

name = str(input("Name: "))
surname = str(input("Surname: "))
age = int(input("Age: "))

firstQuestion = input("Do you eat healthy food?: ")
secondQuestion = input("Do you like sport?: ")

thirdQuestion = input("Какой ваш любимый цвет? ")
fourthQuestion = input("Какое ваше хобби? ")
fifthQuestion = input("В каком городе вы живете? ")

print(f"Пользователь: {name} {surname}, Возраст: {age}")
print(f"Отношение к еде: {firstQuestion}")
print(f"Отношение к спорту: {secondQuestion}")
print(f"Любимый цвет: {thirdQuestion}")
print(f"Хобби: {fourthQuestion}")
print(f"Место проживания: {fifthQuestion}")