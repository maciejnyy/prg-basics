arr = [7,9,2,4,5,6]

new_arr = []
for i in arr:
    if i%2 ==0:
        new_arr.append(i)

for i in arr:
    if i%2 !=0:
        new_arr.append(i)
        

print(new_arr)
