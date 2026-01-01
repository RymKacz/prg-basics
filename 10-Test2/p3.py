def f(n):
    word = ''
    if n == 0:
        return word
    elif n ==1:
        word = '*'
        return word
    else:
        for i in range (0,n*2-1):
            if i%2 == 0:
                word += "*"
            else:
                word += "/"
    return word

if __name__ == "__main__":
    print(f(4))
    print(f(1))
    print(f(0))
    print(f(2))
    print(f(3))