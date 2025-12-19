def first_symbols(name):
    skrot = ""
    slowa = name.split()
    counter = 0
    for i in slowa:
        if i:
            skrot += i[0].upper()
        return skrot
        

print(first_symbols("Maciek ma wąsy"))

