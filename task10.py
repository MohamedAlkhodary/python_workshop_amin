# Constants
BASE_FARE = 4.00
RATE_PER_140_METERS = 0.25
METERS_PER_KILOMETER = 1000
DISTANCE_UNIT = 140


def calculate_taxi_fare(distance_km):
    """
    Calculate the total taxi fare based on the distance traveled.

    Args:
    distance_km (float): The distance traveled in kilometers.

    Returns:
    float: The total fare.
    """
    # Convert distance from kilometers to meters
    distance_m = distance_km * METERS_PER_KILOMETER

    # Calculate the number of 140-meter units traveled
    units_traveled = distance_m / DISTANCE_UNIT

    # Calculate the total fare
    total_fare = BASE_FARE + (units_traveled * RATE_PER_140_METERS)

    return total_fare


def main():
    # Example distances
    distances = [1.5, 3.2, 0.75, 2.0, 50.0]

    print("Taxi Fare Calculation:")
    for distance in distances:
        fare = calculate_taxi_fare(distance)
        print(f"Distance traveled: {distance} km - Total fare: ${fare:.2f}")


if __name__ == "__main__":
    main()
