with open("email.txt", "r") as file:
        email = file.read()
        email_line = email.splitlines()
def email_sender(): 
    for line in email_line:
        if "From:" in line:
            print(line)
def email_recipeint():
    for line in email_line:
        if "To:" in line:
            print(line)
def email_subject():
    for line in email_line:
        if "Subject:" in line:
            print(line)
def email_body():
    for line in email_line:
        if "Content-Type:" in line:
            for i in range(email_line.index(line)+2, len(email_line)):
                print(email_line[i])
            
email_sender()
email_recipeint()
email_subject()
email_body()