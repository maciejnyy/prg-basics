array1 = [ 1,4,6,8]

def greaterThan(x,array):
    counter = 0
    for i in array:
        if x > i:
            counter += 1
            continue
            
    return counter
    
print(greaterThan(7,array1))