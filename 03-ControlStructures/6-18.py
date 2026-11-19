x = int(input("x = "))
y = int(input("y = "))
if x > 0 and y > 0: q = "first quadrant"
elif x < 0 and y > 0: q = "second quadrant"
elif x < 0 and y < 0: q = "third quadrant"
elif x > 0 and y < 0: q = "fourth quadrant"
elif x == 0 and y == 0:
    print(f"Point P({x},{y}) is located in the position (0,0)")
    exit()
else:
    print(f"Point P({x},{y}) is on an axis")
    exit()
print(f"Point P({x},{y}) is in the {q} of the coordinate system")
