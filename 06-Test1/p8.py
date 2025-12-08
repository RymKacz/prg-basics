def f(hours,minutes,seconds):
    if(hours*60 == minutes and hours*3600 == seconds and minutes * 60 == seconds):
        return True
    else:
        return False
if __name__ == "__main__":
    print(f(1,60,3600))
    print(f(2,120,7200))
    print(f(4,220,14400))
    print(f(3,180,10600))