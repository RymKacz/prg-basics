def readfromfile(filename):
    """Reads the content of a file and returns it as a string."""
    with open(filename) as file:
        content = file.read()  
    return content

filecontent = readfromfile("pets.txt")
filewords = filecontent.split()
total = 0
for word in filewords:
    total += 1
print(f"The file has {total} words.")