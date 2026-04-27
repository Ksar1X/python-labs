import os


def zmien_i_wyswietl_katalog(sciezka):
    try:
        os.chdir(sciezka)
        print(f"\n✅ Pomyślnie zmieniono katalog na: {os.getcwd()}")

        zawartosc = os.listdir()
        print("Zawartość katalogu:")
        if not zawartosc:
            print(" └── Katalog jest pusty.")
        else:
            for element in zawartosc:
                print(f" ├── {element}")

    except FileNotFoundError:
        print(f"❌ Błąd: Katalog '{sciezka}' nie istnieje.")
    except PermissionError:
        print(f"❌ Błąd: Brak uprawnień dostępu.")
    except NotADirectoryError:
        print(f"❌ Błąd: Ścieżka '{sciezka}' nie jest katalogiem.")
    except Exception as e:
        print(f"❌ Wystąpił błąd: {e}")


def uruchom_interfejs():
    print("--- Start programu ---")
    while True:
        odpowiedz = input("Czy mam zmienić katalog? (Wpisz 'yes'): ")

        if odpowiedz.strip().lower() == "yes":
            print("Super! Przechodzimy dalej...\n")
            nowa_sciezka = input("Podaj ścieżkę do nowego katalogu: ")
            zmien_i_wyswietl_katalog(nowa_sciezka)
            break
        else:
            print("Nie przyjmuję odmowy! Musisz wpisać 'yes' :)")

uruchom_interfejs()