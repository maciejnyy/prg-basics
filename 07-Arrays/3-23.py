def is_subset(arr1, arr2):
    return all(x in arr2 for x in arr1)

if __name__ == "__main__":
    arr_a = [2, 4]
    arr_b = [1, 2, 3, 4, 5]
    print(f"Is {arr_a} a subset of {arr_b}? {is_subset(arr_a, arr_b)}")
