def f(binary_number):
    new = ""
    for char in binary_number:
        if (char == "1" or char == "0"):
            new += char
        else:
            new += "X"
    if(new == binary_number):
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(f("101101"))
    print(f("1311a10100"))