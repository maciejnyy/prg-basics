def bubblesort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

array1 = [1,5,3,9,2,10,4,-20]
array1_sorted = bubblesort(array1)

print(bubblesort(array1_sorted))