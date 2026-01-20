def f(fnc,res):
    zadanie = list(filter(fnc,res))
    return max(zadanie) * min(zadanie)
if __name__ == "__main__":
    res = [95,90,2,50,70]
    fnc1 = lambda x: x> 50
    print(f(fnc1,res))
    fnc2 = lambda x: x>30 and x < 90
    print(f(fnc2,res))