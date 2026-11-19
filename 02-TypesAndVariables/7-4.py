###
# A tree may be cut down if its diameter is at least 50 cm.
# Based on the circumference: diameter = circumference / pi
# Test: Tree 1: 160, Tree 2: 90, Tree 3: 230, Tree 4: 120
# Result: trees 1 and 3 can be cut down.
#
PI = 3.14159
circumference = float(input('Enter tree circumference in cm: '))
diameter = circumference / PI
can_be_cut = diameter >= 50
print(f'Tree can be cut down: {can_be_cut}')
