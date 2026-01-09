def f(uid):
    flag = True
    for i in uid:
        counter = 0
        for j in uid:
            if i == j:
                counter +=1
                if counter >1:
                    flag = False
                    return flag
            else:
                continue
    return flag

print(f(["abc123","ann","abc123","a10"]))