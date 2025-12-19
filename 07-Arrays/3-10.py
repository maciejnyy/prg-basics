array1 = [4,36,12,28,9,44,5,6,1,25]
array2 = [5,1,36]
array3 = []
no_reapeted = False
for i in array1:
    for j in array2:
        if i != j:
            no_reapeted = True
        else:
            no_reapeted = False
            break
    if no_reapeted == True:
        array3.append(i)
print(array3)

    