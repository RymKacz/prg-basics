##
# Checks the correctness of username and password
#
import re

# read username and password from keyboard
username = input("Enter username: ")
password = input("Enter password: ")

# pattern (criteria) for username and password
# Username: 9-100 lowercase letters; Password: 8-100 alphanumeric or underscore
username_pattern = "[a-z]{6,100}$"
password_pattern = "[A-Za-z0-9_]{8,100}$"

# check if username and password are ok
username_match = re.match(username_pattern,username)
password_match = re.match(password_pattern,password)

# print results
if username_match and password_match:
   print("Username and password are correct")
else:
   print("Username or password are incorrect")