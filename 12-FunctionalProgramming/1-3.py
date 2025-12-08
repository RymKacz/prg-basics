def ms_to_kmh(ms):
    """Convert speed from meters per second to kilometers per hour."""
    return ms * 3.6
if __name__ == "__main__":
    speed_ms = 10  # Example speed in meters per second
    speed_kmh = ms_to_kmh(speed_ms)
    print(f"{speed_ms} m/s is equal to {speed_kmh} km/h")