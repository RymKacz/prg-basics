class C:
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
    def __str__(self):
        if self.age >= 18:
            return f'{self.name[0].upper()}{self.name[1].upper()}-{self.surname[0].upper()}{self.surname[1].upper()}-{self.age}'
        else:
            return f'{self.name[0].lower()}{self.name[1].lower()}-{self.surname[0].lower()}{self.surname[1].lower()}-{self.age}'
if __name__ == "__main__":
    print(C("John","May",18))
    print(C("Anna","Brown",17))