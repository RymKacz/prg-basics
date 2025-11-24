def f(amount_to_pay):
    wynik = 0
    wynik2=0
    for i in range (5,amount_to_pay,5):
        wynik += 1
    amount_to_pay = amount_to_pay - wynik*5
    for i in range (2,amount_to_pay,2):
        wynik2 +=1
    amount_to_pay = amount_to_pay - amount_to_pay*2
    return wynik+wynik2+1
if __name__ == "__main__":
    print(f(23))
    print(f(8))