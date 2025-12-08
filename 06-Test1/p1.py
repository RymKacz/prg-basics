def f(x,y):
    reszta = x % y
    heksi = hex(reszta)
    return heksi
if __name__=="__main__":
    print(f(118,20))
    print(f(210,100))