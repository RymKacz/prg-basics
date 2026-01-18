import random
class Thermometer():
    def __init__(self):
        pass
    def turn_on(self):
        self.turn_on = True
    def turn_off(self):
        self.turn_off = False
    def mesured_temperature(self,temperature):
        self.temperature = temperature
    def display_temperature(self):
        if self.temperature > 37.0:
            print(f"Tempreture: {self.temperature}C (fever)")
        else:
            print(f"Tempreture: {self.temperature}C")
def main():
    thermometer = Thermometer()
    thermometer.turn_on()
    temperature = round(random.uniform(34.0, 42.0),1)
    thermometer.mesured_temperature(temperature)
    thermometer.display_temperature()
    thermometer.turn_off()

if __name__ == "__main__":
    main()