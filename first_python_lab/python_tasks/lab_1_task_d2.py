# 2. Twoim zadaniem jest przygotowanie uniwersalnego i profesjonalnego życiorysu, złożonego z 5-ciu zdań, które wyświetlisz na ekranie
# Użytkownik wpisuje tylko swoje imie, nazwisko, wiek, zawód, miejsce urodzenia, zainteresowania i ... życiorys jest gotowy.

name = str(input("Name: "))
surname = str(input("Surname: "))
age = int(input("Age: "))
profession = str(input("Profession: "))
placeOfBirth = str(input("Place of birth: "))
hobbies = str(input("Hobbies: "))

s1 = f"My name is {name} {surname}, and I am a dedicated professional in my field."
s2 = f"At {age} years old, I have developed a strong foundation of skills and experience."
s3 = f"Originally born in {placeOfBirth}, my journey has been shaped by diverse environments."
s4 = f"I currently serve as a {profession}, focusing on delivering high-quality results."
s5 = f"Beyond my professional career, I am deeply passionate about {hobbies}."

print(f"{s1} {s2} {s3} {s4} {s5}")