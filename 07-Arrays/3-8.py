array = [2,6,4,9,7]

def star(n):
    for i in range(n):
        print("*", end = "")            
    return ""

for i in array:
    print(f"{i}: ", end="")  # print number first, stay on same line
    star(i)                  # print stars
    print()    