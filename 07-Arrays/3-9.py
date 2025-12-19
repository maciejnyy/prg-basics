array1, array2 = [True,False,True],   [True,False,True]

def compare(arr1,arr2):
    comparison = ""
    if len(arr1) == len(arr2):
         for i in range(len(arr1)):
            if arr1[i] == arr2[i]:
                comparison = "arrays the same"
            else:
                comparison = "diferent arrays"
                break
    else:
        comparison = "diferent arrays"
    return comparison

print(compare(array1,array2))