matrix = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

def diagonal(table):
    for i in range(len(table)):
        for j in range(len(table)):
            if i==j:
                table[i][j] = 1
            else:
                continue
    return table

result = diagonal(matrix)

for row in result:
    print(row)
