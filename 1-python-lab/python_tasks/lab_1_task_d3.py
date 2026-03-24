# 3. Przygotuj dla dziecka, które uczy się czytać zestaw sylab do nauki, ale zrób to inteligentnie tj.
# dziecko wpisuje na klawiaturze 1 spółgłoskę a Ty dodajesz do niej odpowiednie samogłoski i wyświetlasz całość na ekranie


vowels = ['a', 'e', 'i', 'o', 'u', 'y']
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "v", "w", "x", "z", "ch", "cz", "sz"]

letter = input("Your consonants: ").lower().strip()
if letter in consonants:
    for vowel in vowels:
        print(letter + vowel)