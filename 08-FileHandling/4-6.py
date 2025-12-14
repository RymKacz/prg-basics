filename = input("Enter the filename: ")
try:
    with open(filename, 'r') as file:
        content = file.read()
        contentlines = content.splitlines()
        counterlines = 0
        countercharakters = 0
        counterwords = 0
        for line in contentlines:
            counterlines += 1
            countercharakters += len(line)
            counterwords += len(line.split())
        print(f"Lines: {counterlines}")
        print(f"Characters: {countercharakters}")
        print(f"Words: {counterwords}")

except FileNotFoundError:
    print("The specified file was not found.")