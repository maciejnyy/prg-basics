###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # read the character's code (use ord())
    crypted_letter_number = ord(char)
    # add one to the character's code
    crypted_letter_number = crypted_letter_number + 1
    # replace new character code with its
    # corresponding character (use chr())
    crypted_letter = chr(crypted_letter_number)
    # add encrypted character to encrypted text
    encrypted_text = encrypted_text + crypted_letter

print(plain_text)
print(encrypted_text)