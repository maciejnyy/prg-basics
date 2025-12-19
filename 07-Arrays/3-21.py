def isSubset(arr1,arr2):
    logic = False
    for i in arr1:
        for j in range(len(arr2)):
            if i == arr2[j]:
                logic = True
                del arr2[j]
                break
            else:
                logic = False
                continue
        if logic == False:
            return "nie nalezy do podzbioru"
    if logic == True:
        return "nalezy do podzbioru"
    
print(isSubset([1,0,0,2],[0,0,2,1,0]))
        