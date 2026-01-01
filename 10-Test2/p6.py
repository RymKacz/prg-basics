import re
def f(addr):
    if re.match("^[a-z,A-Z]{0,1}",addr):
        if re.match(".[1-9]{1,9999}",addr) or re.match("..[1-9]{1,9999}",addr):
            return True
        else:
            return False
    else:
        return False
if __name__ == "__main__":
    print(f("Aa12"))
    print(f("bcd555"))
    print(f("a4"))
    print(f('bC123'))