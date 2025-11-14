###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math

def triangle_area(a,b,c):
    s = (a+b+c) / 2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area

a = int(input('Enter a side: '))
b = int(input('Enter b side: '))
c = int(input('Enter c side: '))

pole = triangle_area(a,b,c)
print(f'The area of ​​a triangle with sides {a},{b},{c} is {pole}')
