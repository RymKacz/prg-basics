with open("files.txt", "r") as file:
    content = file.read()
    lines = content.splitlines()
    for line in lines:
        if ".html" in line:
            print(line)