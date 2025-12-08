class Phone():
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_on = False
        self.battery_level = 100
        self.current_app = None
    def power_on(self):
        self.is_on = True
    def power_off(self):
        self.is_on = False
    def open_app(self, app_name):
        if self.is_on:
            self.current_app = app_name
    def close_app(self):
        self.current_app = None
    def display_info(self):
        print(f"Phone Brand: {self.brand}")
        print(f"Phone Model: {self.model}")
        print(f"Price: ${self.price}")
        print(f"Battery Level: {self.battery_level}%")
        if self.is_on:
            print("The phone is ON.")
            if self.current_app:
                print(f"Current App: {self.current_app}")
            else:
                print("No app is currently open.")
        else:
            print("The phone is OFF.")
def main():
    my_phone = Phone("Apple", "iPhone 13", 999)
    my_phone.power_on()
    my_phone.open_app("Messages")
    my_phone.display_info()
    my_phone.close_app()
    my_phone.power_off()
if __name__ == "__main__":
    main()

    