def f(fnc, res):
    arr = []
    for i in res:
        if fnc(i):
            arr.append(i)
    max1 = max(arr)
    min1 = min(arr)

    return (max1 - min1)

res = [95,90,20,50,70]
fnc1 = lambda x: x>50
print(f(fnc1,res))