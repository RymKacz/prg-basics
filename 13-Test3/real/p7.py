def f(files):
    return sorted(files, key=lambda x: x.split('.')[-1])
if __name__ == "__main__":
    files = ["a.txt","bb.pdf","ccc.py","dddd.mpeg4"]
    print(f(files))