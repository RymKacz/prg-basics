quiz_answers = "1a,2a,3c,4c,5b,6a,7d,8a,9b,10d,11a,12d"
def f(quiz_answers,student1,student2):

    table = quiz_answers.split(',')
    studenta = student1.split(',')
    studentb = student2.split(',')
    help = []
    help2 = []
    punkt1 = 0
    punkt2 = 0
    for key in studenta:
        if key in table:
            help += key
    for key in studentb:
        if key in table:
            help2 += key
    if len(help) >= len(help2):
        for key in help:
            if key in help2:
                punkt1 += 1
    else:
        for key in help2:
            if key in help:
                punkt1 +=1
        
    return int(punkt1/2)

if __name__ == "__main__":
    student1 = "9b,5b,2a,1a,5b,12a,11a"
    student2 = "12a,3c,2a,1a,7d,8a,9b,5b,4b"
    print(f(quiz_answers,student1,student2))