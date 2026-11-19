arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

print("Before:")
for row in arr:
    print(row)

# Swap first and last column
for i in range(len(arr)):
    arr[i][0], arr[i][-1] = arr[i][-1], arr[i][0]

print("\nAfter:")
for row in arr:
    print(row)
