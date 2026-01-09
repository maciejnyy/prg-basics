class C:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.quadrant = 0

    def m1(self):
        if self.x > 0 and self.y > 0:
            self.quadrant = 1
        elif self.x < 0 and self.y > 0:
            self.quadrant = 2
        elif self.x < 0 and self.y < 0:
            self.quadrant = 3
        elif self.x > 0 and self.y < 0:
            self.quadrant = 4
        else:
            self.quadrant = 0
        return self.quadrant

    def m2(self, a, b):
        other = C(a, b)
        return self.m1() == other.m1()
    
    def m3(self, a, b):
        self.a = a
        self.b = b
        import math
        distance = math.sqrt(float((self.a-self.x)**2+(self.b-self.y)**2))
        if distance > 5:
            return True
        else:
            return False


p = C(2, 3)
print(p.m1())        # Output: 1
print(p.m2(7, 4)) 
print(p.m3(8, 5)) 