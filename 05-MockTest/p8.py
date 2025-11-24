def f(palindrom):
    test = palindrom[::-1]
    if(test == palindrom):
        return True
    else:
        return False
if __name__=="__main__":
    print(f("radar"))
    print(f("12-11-21"))
    print(f("book"))