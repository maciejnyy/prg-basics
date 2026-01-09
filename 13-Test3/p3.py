def f(d):
    total = 0
    for key,value in d.items():
        total += value
    average = total / len(d)
    number = 0
    for key,value in d.items():
        if value > average:
            number += 1
    return number
print(f({"LO231":150,"BA787":20,"NZ15":30}))