def f(number,even):
    n_number = str(number)
    wynik_p = 0
    wynik_n = 0
    for char in n_number:
        if(char == "1" or char =="3" or char=="5" or char == "7" or char == "9"):
            wynik_n += int(char)
        else:
            wynik_p += int(char)
    if (even == True):
        return wynik_p
    else:
        return wynik_n

if __name__ == "__main__":
    print(f(3124,True))
    print(f(3124,False))
    print(f(20576,False))
    print(f(20576,True))
    print(f(13115,True))