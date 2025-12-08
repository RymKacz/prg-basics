def f(wysokosc_startowa,wspolczynnik_odbicia,wysokosc_docelowa):
    wynik = 0
    while wysokosc_startowa > wysokosc_docelowa:
        wysokosc_startowa *= wspolczynnik_odbicia
        wynik +=1
    return wynik
if __name__ == "__main__":
    print(f(12,0.9,10))
    print(f(10,0.6,1))
    print(f(25,0.85,7))