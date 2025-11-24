def f(n1,n2,n3):
    if(n1 != n2):
        if(n2 != n3):
            if(n1 != n3):
                return True
            else:
                return False
        elif(n1 != n3):
            if(n2 != n3):
                return True
            else:
                return False
    elif(n2 != n3):
        if(n2 != n1):
            if(n1 != n3):
                return True
            else:
                return False
        elif(n1 != n3):
            if(n2 != n3):
                return True
            else:
                return False
    elif(n3 != n1):
        if(n3!=n2):
            if(n2 != n1):
                return True
            else:
                return False
        elif(n2!=n1):
            if(n3!=n2):
                return True
            else:
                return False

if __name__=="__main__":
    print(f(4,8,5))
    print(f(2,9,2))