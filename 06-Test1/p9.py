def f(size):
    sumaM = 0
    sumaS = 0
    sumaL = 0
    for char in size:
        if char == "M":
            sumaM +=1
        elif char == "S":
            sumaS+=1
        elif char == "L":
            sumaL +=1
    if(sumaM < sumaS and sumaM <= sumaL):
        return "M"
    elif(sumaS <= sumaM and sumaS <= sumaL):
        return "S"
    elif(sumaL < sumaM and sumaL < sumaS):
        return "L"
    elif(sumaL == sumaM):
        return "M"
    elif(sumaL == sumaS):
        return "S"
    elif(sumaM == sumaS):
        return "S"
if __name__ == "__main__":
    print(f("L,S,L,M,L,S,S,L"))
    print(f("M,L,L,L,M"))
    print(f("M,L,M,L,S,S,S"))

