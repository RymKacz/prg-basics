def f(files):
    # Wyciągamy cyfry z nazwy i zamieniamy na liczbę, aby według niej sortować
    return sorted(files, key=lambda x: int(''.join(c for c in x if c.isdigit())))

# Test z zadania:
files = ["copy179", "copy15", "copy3", "copy123", "copy9"]
print(f(files))
# Wynik: ['copy3', 'copy9', 'copy15', 'copy123', 'copy179']