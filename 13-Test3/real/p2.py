def f(expression):
    stos = []
    elementy = expression.split()
    for element in elementy:
        if element == "+":
            b = stos.pop()
            a = stos.pop()
            stos.append(a + b)
        elif element == "-":
            b = stos.pop()
            a = stos.pop()
            stos.append(a - b)
        else:
            stos.append(int(element))
    return stos[0]
if __name__ == "__main__":
    print(f("2 3 4 5 + - +"))
    print(f("11 7 + 15 - 14 +"))