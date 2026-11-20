arr = [
    [-38, 19], 
    [5, 40], 
    [-7, 11], 
    [29, 16]
]

min_val = float('inf')
max_val = float('-inf')
min_pos = (0, 0)
max_pos = (0, 0)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] < min_val:
            min_val = arr[i][j]
            min_pos = (i, j)
        if arr[i][j] > max_val:
            max_val = arr[i][j]
            max_pos = (i, j)

print(f"Smallest value: {min_val} in row {min_pos[0]} col {min_pos[1]}")
print(f"Largest value: {max_val} in row {max_pos[0]} col {max_pos[1]}")
