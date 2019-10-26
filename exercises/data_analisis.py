import csv

def prepare_data(wartosc):
    wartosc = wartosc.replace("$", "")
    wartosc = wartosc.replace(",", "")
    kwota = float(wartosc)

    if isinstance(kwota, float):
        return kwota

def analysis(lista):
    srednia = sum(lista)/len(lista)
    return srednia

def wyciagnij_srednia(csv_file):
    lista = []
    for row in csv_file:
        wartosc = row["balance"]
        kwota = prepare_data(wartosc)
        lista.append(kwota)

    wynik = analysis(lista)

    return round(wynik, 2)             #zaokrąglamy do dwóch miejsc po przecinku

    return(wynik)

def wypisz_wiersze(csv_file):
    for row in csv_file:
        print(row["balance"])

with open("../resources/data.csv") as plik:
    csv_file = csv.DictReader(plik)  # odczytanie pliku jako słownika "dictionary"

    print(wyciagnij_srednia(csv_file))
    # printujemy samą kolumnę balans z data.csv
