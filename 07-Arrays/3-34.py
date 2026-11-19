arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

print("Before:")
for row in arr:
    print(row)

# Swap first and last row
arr[0], arr[-1] = arr[-1], arr[0]

print("\nAfter:")
for row in arr:
    print(row)
