class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_fare(self):
        print(f"Distance: {self.distance} km")
        print(f"Fare: €{self.fare:.2f}")

def main():
    # Create a TaxiRide instance with a rate of €2 per km
    taxi_ride = TaxiRide(rate_per_km=2)
    taxi_ride2 = TaxiRide(rate_per_km=3.5)
    # Calculate fare for a distance of 10 km
    taxi_ride.calculate_fare(distance=10)
    taxi_ride2.calculate_fare(distance=12)
    # Print the fare details
    taxi_ride.print_fare()
    taxi_ride2.print_fare()


if __name__ == "__main__":
    main()
