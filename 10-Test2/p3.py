def f(array2D):
    rows = len(array2D)
    cols = len(array2D[0])

    # inicjalizacja sum kolumn
    sumy_kolumn = [0] * cols

    # liczenie sum wierszy
    for i in range(rows):
        suma_wiersza = 0
        for j in range(cols):
            value = array2D[i][j]
            suma_wiersza += value
            sumy_kolumn[j] += value
            print(f'wiersz {i}, kolumna {j}: {value}', end='  ')
        print('| suma wiersza:', suma_wiersza)

    # wypisanie sum kolumn
    print('Suma kolumn:')
    for j in range(cols):
        print(f'kolumna {j}: {sumy_kolumn[j]}')

print(f([[3,7,2],[4,2,5],[9,2,1]]))
# tab = [[3,7,2],[4,2,5],[9,2,1]]
# print(tab[0])