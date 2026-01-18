def f(files):
    # Sortujemy listę, używając części po kropce jako klucza
    return sorted(files, key=lambda x: x.split('.')[-1])

# Test z zadania:
files = ["a.txt", "bb.pdf", "ccc.py", "dddd.mpeg4"]
wynik = f(files)
print(wynik) 
# Wynik: ['dddd.mpeg4', 'bb.pdf', 'ccc.py', 'a.txt']