import re
def f(dates):
    pattern = r"[1-9][0-9][0-9][0-9]-[0-1][0-9]-[0-3][0-9]"
    x = re.findall(pattern, dates)
    return x
print(f("2021-1-3;05/12/2024:1998-12-11,9 maj 2007;;2001-12-07,,15-09-2011"))