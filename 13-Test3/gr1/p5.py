class C:
    def __init__(self,stadium):
        self.stadium = stadium
        pass
    def m1(self,s,n):
        self.s = s
        self.n = n
        self.stadium.update({s:n})
    def m2(self,s):
        self.s = s
        count = 0
        for letter in s:
            if letter in self.stadium:
                count += self.stadium[letter]
        return count

stadium = C({"A":120,"D":150,"G":90,"K":110})
stadium.m1("G",130)
print(stadium.m2("GD"))
print(stadium.m2("KEJ"))