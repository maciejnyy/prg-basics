def f(subjects):
    best = ""
    best_srednia = 0
    for i,value in subjects.items():
        suma = 0
        srednia = 0
        ilosc_ocen = 0
        for j in value:
            suma += j
            ilosc_ocen += 1
        srednia = suma / ilosc_ocen
        if srednia > best_srednia:
            best_srednia = srednia
            best = i
    return best

print(f({"math":[3,4,4,6,6,6,6],"geo":[5,4,4,4,6,6,6,6],"comp":[5,4,6]}))