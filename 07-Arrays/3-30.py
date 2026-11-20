arr = [[0 for _ in range(5)] for _ in range(5)]

for i in range(5):
    for j in range(5):
        arr[i][j] = (i + 1) * (j + 1)

for row in arr:
    for item in row:
        print(f"{item:2d}", end=" ")
    print()
