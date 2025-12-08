def f(thing_to_wash,extra_winse,extra_spin):
    if(thing_to_wash == "J"):
        min = 40
        if extra_winse  == True:
            min += 15
            if extra_spin == True:
                min += 9
        else:
            if extra_spin == True:
                min += 9
    elif(thing_to_wash == "U"):
        min = 70
    elif(thing_to_wash == "S"):
        min = 20
    return min
if __name__ == "__main__":
    print(f("U",False,True))
    print(f("J",True,True))
    print(f("S",False,False))