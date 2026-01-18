class contact():
    def __init__(self):
        self.dict = dict()
    
    def info(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
    
    def add_to_dictionary(self):
        self.dict.update({self.name: f"Email: {self.email}, Phone: {self.phone}"})
    
    def display_info(self):
        print(self.dict)
def main():
    c = contact()
    c.info("John Brown", "brown@onet.pl","555234000")
    c.add_to_dictionary()
    c.info("Anna May", "am@o2.pl","232000199")
    c.add_to_dictionary()
    c.display_info()
if __name__ == "__main__":
    main()