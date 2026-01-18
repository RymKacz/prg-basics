def f(d):
    countplus = 0
    countminus = 0
    for i in d:
        if i == '+':
            countplus += 1
        elif i == '-':
            countminus += 1
    return countplus - countminus

print(f(""))
print(f("+-+"))
print(f("+-+++-+---"))
print(f("+-+++++-"))