def binary_numer(value):
    for char in value:
        cyfra = int(char)
        if cyfra ==0 or cyfra == 1:
            continue
        else:
            return False
    return True
        
print(binary_numer("01010101l10"))