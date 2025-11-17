plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # read the character's code (use ord())
    # add one to the character's code
    # replace new character code with its
    # corresponding character (use chr())
    # add encrypted character to encrypted text
    encrypted_text += chr(ord(char) + 1)
    

print(plain_text)
print(encrypted_text)
