def flatten_matrix(m):
    return [item for row in m for item in row]

if __name__ == "__main__":
    matrices = [
        [[2, 3], [1, 5]],
        [[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]],
        [[2, 1], [3, 5], [7, 4], [2, 6]]
    ]
    
    for m in matrices:
        print(f"2D Array: {m}\n1D Array: {flatten_matrix(m)}\n")
