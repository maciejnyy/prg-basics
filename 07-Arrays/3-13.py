def occurs(number, array):
    result = False
    for i in array:
        if number == i:
            result = True
    if result == True:
        return f"number {number} appears in the array"
    else:
        return f"number {number} doesn't appears in the array"

print(occurs(-1, [15,38,7,23,14]))