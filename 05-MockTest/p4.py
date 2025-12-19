def card_number(number):
    szyfrowany = "" 
    i = 0
    for digit in number:
        if i == 0 or i == 1:
            szyfrowany += digit
        elif i >= 12:
            szyfrowany += digit
        else:
            digit = "*"
            szyfrowany += digit
        i += 1
    return szyfrowany

print (card_number("5290312400019022"))

