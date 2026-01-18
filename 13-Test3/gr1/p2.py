def f(expression):
    stos = []
    elementy = expression.split() # Dzieli tekst na pojedyncze liczby i znaki

    for element in elementy:
        if element == "+":
            b = stos.pop() # Wyjmij ostatnią liczbę
            a = stos.pop() # Wyjmij przedostatnią liczbę
            stos.append(a + b)
        elif element == "-":
            b = stos.pop()
            a = stos.pop()
            stos.append(a - b)
        else:
            # Jeśli to nie operator, to znaczy, że to liczba
            stos.append(int(element))
            
    return stos[0]

# Testy z zadania:
print(f("2 3 4 5 + - +"))        # Wynik: -4
print(f("11 7 + 15 - 14 +"))     # Wynik: 17