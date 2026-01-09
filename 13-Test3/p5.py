def f(numbers):
    import re
    pattern = "^[+-]?[a-dA-D1-7]+$"

    number = 0
    for i in numbers:
        if re.match(pattern, i):
            number += 1
    return number

print(f(["1234"]))