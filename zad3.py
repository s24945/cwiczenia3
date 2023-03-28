import getpass
import random

print("GRA W PAPIER, KAMIEN, NOZYCE")
print("Są dwa tryby:")
print("1. Gracz vs komputer")
print("2. Gracz vs gracz")
tryb = input("Jaki tryb wybierasz?(1/2) ")
counter1 = 0
counter2 = 0
rundy = int(input("Ile rund chcesz grac? "))
gra = 0
if tryb == "1":
    nazwaGracza = input("Podaj nazwę gracza: ")

    while gra <= rundy:
        print("\n-----------------\n1.Papier\n2.Kamień\n3.Nozyce")
        wyborGracz = int(input("Wybierz swoj ruch: (1/2/3)"))
        wyborKomp = random.randint(1, 3)

        if wyborGracz == 1 and wyborKomp == 1:
            print("\n", nazwaGracza, ":papier vs Komp :papier\nREMIS!")
        elif wyborGracz == 1 and wyborKomp == 2:
            print("\n", nazwaGracza, ":papier vs Komp :kamien\nPUNKT DLA ", nazwaGracza, "!")
            counter1 += 1
        elif wyborGracz == 1 and wyborKomp == 3:
            print("\n", nazwaGracza, ":papier vs Komp :nozyce\nPUNKT DLA KOMPUTER!")
            counter2 += 1

        elif wyborGracz == 2 and wyborKomp == 1:
            print("\n", nazwaGracza, ":kamien vs Komp :papier\nPUNKT DLA KOMPUTER!")
            counter2 += 1
        elif wyborGracz == 2 and wyborKomp == 2:
            print("\n", nazwaGracza, ":kamien vs Komp :kamien\nREMIS!")
        elif wyborGracz == 2 and wyborKomp == 3:
            print("\n", nazwaGracza, ":kamien vs Komp :nozyce\nPUNKT DLA ", nazwaGracza, "!")
            counter1 += 1

        elif wyborGracz == 3 and wyborKomp == 1:
            print("\n", nazwaGracza, ":nozyce vs Komp :papier\nPUNKT DLA ", nazwaGracza, "!")
            counter1 += 1
        elif wyborGracz == 3 and wyborKomp == 2:
            print("\n", nazwaGracza, ":nozyce vs Komp :kamien\nPUNKT DLA KOMPUTER!")
            counter2 += 1
        elif wyborGracz == 3 and wyborKomp == 3:
            print("\n", nazwaGracza, ":nozyce vs Komp :nozyce\nREMIS!")

        gra += 1

    if counter1 > counter2:
        print("-----------------")
        print("WYGRYWA: ", nazwaGracza)
        print("Wyniki: ", nazwaGracza, counter1, ":", counter2, "Komputer")
    elif counter1 < counter2:
        print("-----------------")
        print("WYGRYWA: KOMPUTER")
        print("Wyniki: ", nazwaGracza, counter1, ":", counter2, "Komputer")


if tryb == "2":
    nazwa1 = input("Podaj nazwe gracza nr1: ")
    nazwa2 = input("Podaj nazwe gracza nr2: ")

    while gra <= rundy:
        print("\n-----------------\n1.Papier\n2.Kamień\n3.Nozyce")
        wyborGracz1 = int(getpass.getpass(nazwa1 + " wybierz swoj ruch: (1/2/3)"))
        wyborGracz2 = int(getpass.getpass(nazwa2 + " wybierz swoj ruch: (1/2/3)"))

        if wyborGracz1 == 1 and wyborGracz2 == 1:
            print("\n", nazwa1, ":papier vs", nazwa2, ":papier\nREMIS!")
        elif wyborGracz1 == 1 and wyborGracz2 == 2:
            print("\n", nazwa1, ":papier vs", nazwa2, ":kamien\nPUNKT DLA ", nazwa1, "!")
            counter1 += 1
        elif wyborGracz1 == 1 and wyborGracz2 == 3:
            print("\n", nazwa1, ":papier vs", nazwa2, ":nozyce\nPUNKT DLA ", nazwa2, "!")
            counter2 += 1

        elif wyborGracz1 == 2 and wyborGracz2 == 1:
            print("\n", nazwa1, ":kamien vs", nazwa2, ":papier\nPUNKT DLA", nazwa2, "!")
            counter2 += 1
        elif wyborGracz1 == 2 and wyborGracz2 == 2:
            print("\n", nazwa1, ":kamien vs", nazwa2, ":kamien\nREMIS!")
        elif wyborGracz1 == 2 and wyborGracz2 == 3:
            print("\n", nazwa1, ":kamien vs", nazwa2, ":nozyce\nPUNKT DLA ", nazwa1, "!")
            counter1 += 1

        elif wyborGracz1 == 3 and wyborGracz2 == 1:
            print("\n", nazwa1, ":nozyce vs", nazwa2, ":papier\nPUNKT DLA ", nazwa1, "!")
            counter1 += 1
        elif wyborGracz1 == 3 and wyborGracz2 == 2:
            print("\n", nazwa1, ":nozyce vs", nazwa2, ":kamien\nPUNKT DLA ", nazwa2, "!")
            counter2 += 1
        elif wyborGracz1 == 3 and wyborGracz2 == 3:
            print("\n", nazwa1, ":nozyce vs", nazwa2, ":nozyce\nREMIS!")

        gra += 1

    if counter1 > counter2:
        print("-----------------")
        print("WYGRYWA: ", nazwa1)
        print("Wyniki: ", nazwa1, counter1, ":", counter2, nazwa2)
    elif counter1 < counter2:
        print("-----------------")
        print("WYGRYWA: ", nazwa2)
        print("Wyniki: ", nazwa1, counter1, ":", counter2, nazwa2)
