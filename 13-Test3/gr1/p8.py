class C:
    def __init__(self,number):
        self.number = number
    def m1(self):
        return self.number
    def m2(self):
        self.number += 1
    def m3(self):
        self.number -= 1
    def m4(self,n):
        self.number += n
    def __str__(self):
        return str(self.number)
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