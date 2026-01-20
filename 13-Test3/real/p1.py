def f(d):
    countminus = 0
    countplus = 0
    for char in d:
        if char == "+":
            countplus += 1
        elif char == "-":
            countminus += 1
    return countplus - countminus
if __name__ == "__main__":
    print(f(""))
    print(f("+-+"))
    print(f("+-+++-+---"))
    print(f("+-+++++-"))