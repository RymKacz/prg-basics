class number_clac():
    def __init__(self,number):
        self.number = number
    def max_number(self):
        self.max_number = max(self.number)
    def min_number(self):
        self.min_number = min(self.number)
    def mean_number(self):
        self.mean_number = sum(self.number)/len(self.number)
    def mediana_number(self):
        sorted_numbers = sorted(self.number)
        n = len(sorted_numbers)
        mid = n // 2
        if n % 2 == 0:
            self.mediana_number = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
        else:
            self.mediana_number = sorted_numbers[mid]
    def display_table(self):
        string = '' 
        for i in self.number:
            string += f"{i} "
        print(string)
    def display(self):
        self.max_number()
        self.min_number()
        self.mean_number()
        self.mediana_number()
        print(f"Max number: {self.max_number}")
        print(f"Min number: {self.min_number}")
        print(f"Mean number: {self.mean_number}")
        print(f"Mediana number: {self.mediana_number}")

def main():
    number = [12, 37, 6, 9, 17]
    number_table = number_clac(number)
    number_table.display_table()
    number_table.display()

if __name__ == "__main__":
    main()
