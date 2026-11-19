def identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def print_matrix(matrix):
    for row in matrix:
        for item in row:
            print(item, end=" ")
        print()
    print()

if __name__ == "__main__":
    print("Matrix 3x3:")
    print_matrix(identity_matrix(3))
    print("Matrix 5x5:")
    print_matrix(identity_matrix(5))
    print("Matrix 8x8:")
    print_matrix(identity_matrix(8))
