def f(arr):
    for i in arr:
        for j in arr:
            if i == j:
                continue
            elif i != j:
                return j
            
print(f([7,4,7,7,7,7,7,7]))