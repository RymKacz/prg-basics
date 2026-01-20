import re
def f(dates):
    pattern = r'[0-9]{0,2} [a-zA-Z]{0,100} [0-9]{4}'
    result = re.findall(pattern,dates)
    return result
if __name__ == "__main__":
    dates = "17 July 1999;05/12/2024;April 7 2014,9 May 2007;;2001-12-07:,1 May 23"
    print(f(dates))