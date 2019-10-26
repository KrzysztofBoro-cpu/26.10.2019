zmienna_1 = input("Podaj liczbę :")
zmienna_2 = input("Podaj liczbę :")

try:
    a = int(zmienna_1)
    b = int(zmienna_2)
    print(f"Suma liczb to {a+b}.")
except Exeption:
    print("Nie byłem w stanie zrzutować na inta")

print("Koniec")
