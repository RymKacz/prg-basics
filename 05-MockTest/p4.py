def f(card_name):
    new = ""
    i=0
    for char in card_name:
        if(i >1 and i<12):
            new += "*"
        else:
            new+=char
        i+=1
    return new
if __name__=="__main__":
    print(f("5290312400019022"))