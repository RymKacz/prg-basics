class C:
    def __init__(self,stadion):
        self.stadion = stadion
    def m1(self,s,n):
        self.s = s
        self.n = n
        self.stadion[s] = n
    def m2(self,s):
        count = 0
        for char in s:
            if char in self.stadion:
                count += self.stadion[char]
        return count
if __name__ == "__main__":
    stadium = C({"A":120,"D":150,"G":90,"K":110})
    stadium.m1("G",130)
    print(stadium.m2("GD"))
    print(stadium.m2("KEJ"))
