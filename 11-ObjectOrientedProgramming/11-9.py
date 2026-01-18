class C():
    def __init__(self,name,surname,age,year_worked):
        self.name = name
        self.surname = surname
        self.age = age
        self.year_worked = year_worked
    def display_info(self):
        if self.age > 18:
            print(f"{self.surname.upper()}{self.name[0].upper()}{self.year_worked}")
        else:
             print(f"{self.surname.lower()}{self.name[0].lower()}{self.year_worked}")
def main():
    C1 = C("Anna","May",17,7)
    C1.display_info()
    C2 = C("George","Brown",21,4)
    C2.display_info()
if __name__ == "__main__":
    main()