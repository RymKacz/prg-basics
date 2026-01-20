import re
def f(vname):
    check = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    if len(vname) >0 and len(vname) <= 5:
        if re.match(check, vname):
            return True
        else:
            return False
    else:
        return False
if __name__ == "__main__":
    print(f("aBC"))
    print(f("_ab_c"))
    print(f("abcdef"))
    print(f("8abc"))
    print(f("_aB8_"))