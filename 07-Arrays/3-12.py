array = [3,2,5,8,1,9,8,3,7,7,13]
unique_array = []
for i in array:
    counter = 0
    for j in array:
        if i!=j:
            continue
        else:
            counter += 1
            if counter > 1:
                break
    if counter <= 1:
        unique_array.append(i)

print(unique_array)