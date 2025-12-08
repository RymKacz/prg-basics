def f(student1,student2):
    table1 = student1.split(",")
    table2 = student2.split(",")
    suma1 = 0
    suma2 = 0
    for char1 in table1:
        if int(char1) > 2:
            suma1 +=1
    for char2 in table2:
        if int(char2) >2:
            suma2 +=1
    if suma1 > suma2:
        return 1
    elif suma1 < suma2:
        return 2
    else:
        return 0
if __name__ == "__main__":
    print(f("3,4,5","4,3"))
    print(f("3,2,5","5,5,2,5"))
    print(f("3,2,5,2,2","4,4"))
