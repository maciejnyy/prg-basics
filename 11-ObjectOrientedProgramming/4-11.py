class C:
    def __init__(self, sectors):
        self.sectors = sectors

    def m1(self, s, n):
        self.sectors[s] = n

    def m2(self, s):
        return sum(self.sectors.get(sector, 0) for sector in s)

if __name__ == "__main__":
    stadium = C({"A": 120, "D": 150, "G": 90, "K": 110})
    stadium.m1("G", 130)
    print(stadium.m2("GD"))
    print(stadium.m2("KEJ"))
