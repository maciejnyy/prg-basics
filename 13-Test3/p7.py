class C:
    def __init__(self, n):
        self.n = n

    def m1(self):
        return self.n
    def m2(self):
        self.n = self.n+1
    def m3(self):
        self.n = self.n-1
    def m4(self, m):
        self.n = self.n + m
    def __str__(self):
        str(self.n)
        return self.n
    
c = C(5)

print(c.m1()) 
c.m2()
print(c.m1()) 
c.m4(-8)
print(c.m1()) 
c.m3()
print(c.m1()) 
c.m4(10)
print(c.m1()) 
print(c.__str__()) 