###
# Checks the correctness of username and password
#
import re

# read username and password from keyboard
username = input("Write your username: ")
password = input("Write your password: ")

# pattern (criteria) for username and password
username_pattern = "^[a-z]{6,}$"
password_pattern = "^[A-Za-z0-9_]{8,}$"

# check if username and password are ok
username_match = bool(re.match(username_pattern,username))
password_match = bool(re.match(password_pattern, password))

# print results
if username_match == True and password_match == True:
   print(f"nazwa {username} i haslo {password} poprawne")
elif username_match == True and password_match == False:
   print(f"nazwa {username} poprawna lecz haslo {password} niepoprawne")
elif username_match == False and password_match == True:
    print(f"nazwa {username} niepoprawna lecz haslo {password} poprawne")
else:
    print(f"nazwa {username} i haslo {password} niepoprawne")

