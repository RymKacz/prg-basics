import re
def f(vname):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    if len(vname) > 0 and len(vname) <= 5:
        if re.match(pattern, vname):
            return True
        else:
            return False
    else:
        return False
print(f("aBC"))
print(f("_ab_c"))
print(f("abcdef"))
print(f("8abc"))
print(f("_aB8_"))