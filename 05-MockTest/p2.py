def different_digits(x,y,z):
    if x != y and y != z and x != z:
        return True
    else:
        return False
    
print(different_digits(3,3,4))