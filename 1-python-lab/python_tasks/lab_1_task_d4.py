# 4. Użytkownik podaje imie, sprawdź czy to imie to Janusz lub Grażyna


name = str(input("Name: "))
if (name == "Janusz") or (name == "Grazyna"):
    print("True")
else:
    print("False")