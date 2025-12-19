
def differenceMaxMin(arrayb):
    max_number = max(arrayb)
    min_number = min(arrayb)
    difference = max_number - min_number
    return difference

def middleValue(arrayc):
    ordered_array = sorted(arrayc)
    a = len(ordered_array)
    median = 0
    b = 0
    if a % 2 != 0:
        b = a // 2
        median = ordered_array[b]
    else:
        b = a // 2
        median = (ordered_array[b] + ordered_array[b-1]) / 2
    print(ordered_array)
        
    return median

def two_element(arrayd):
    maximum = arrayd[0]
    minimum = arrayd[0]
    new_array = []

    for i in arrayd:
        if i > maximum:
            maximum = i
        elif i < minimum:
            minimum = i
    new_array.append(minimum)
    new_array.append(maximum)
    return new_array

def number_string(arraye):
    string = ""
    for i in range(len(arraye)):
        if arraye[i] == arraye[-1]:
            string += str(arraye[-1])
        else:
            string += str(arraye[i]) + "-"


    return string

def secondLargest(arraya):
    temp = arraya.copy()
    max1 = temp.index(max(temp))
    del temp[max1]
    max2 = max(temp)
    return max2
    

array1 = [7,3,8,5,2]
         
print("Numbers: ", array1)
print("Second largest number: ", secondLargest(array1))
print("Mediana: ", middleValue(array1))
print("Smallest and largers number: ", two_element(array1))
print("Number as a string: ", number_string(array1))