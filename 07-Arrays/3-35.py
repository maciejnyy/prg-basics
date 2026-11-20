def transpose_matrix(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def print_matrix(matrix):
    for row in matrix:
        for item in row:
            print(item, end=" ")
        print()

if __name__ == "__main__":
    matrices = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]],
        [[5, 6, 7, 8]]
    ]
    
    for m in matrices:
        print("Original:")
        print_matrix(m)
        print("Transposed:")
        print_matrix(transpose_matrix(m))
        print("-" * 15)
