def f(h0,r,h):
    temp = h0
    count = 0
    for i in range(0,h0*1000):
        if temp >= h:
            temp *= r
            count += 1
    return count
if __name__ == "__main__":
    print(f(10,0.8,5))
    print(f(10,0.95,5))
    print(f(12,0.7,2))