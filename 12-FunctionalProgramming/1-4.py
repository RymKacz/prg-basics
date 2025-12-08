f = lambda ms: ms * 3.6
if __name__ == "__main__":
    speed_ms = 10  # Example speed in meters per second
    speed_kmh = f(speed_ms)
    print(f"{speed_ms} m/s is equal to {speed_kmh} km/h")