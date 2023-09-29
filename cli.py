import os
from dotenv import load_dotenv
import argparse
import requests

load_dotenv()
def get_travel_distance(origin, destination):
    GOOGLE_API_KEY = os.getenv("GOOGLE_MAP_KEY")
    endpoint = "https://maps.googleapis.com/maps/api/directions/json"

    params = {
        "origin": origin,
        "destination": destination,
        "key": GOOGLE_API_KEY
    }

    response = requests.get(endpoint, params=params).json()

    if response['status'] != 'OK':
        print(f"Error: {response['status']}")
        return None

    route = response['routes'][0]
    leg = route['legs'][0]
    distance = leg['distance']['text']

    return distance

def main():
    parser = argparse.ArgumentParser(description="Fetch travel distance between two locations")
    parser.add_argument("origin", type=str, help="Origin location")
    parser.add_argument("destination", type=str, help="Destination location")
    args = parser.parse_args()

    origin = args.origin
    destination = args.destination

    distance = get_travel_distance(origin, destination)

    if distance:
        print(f"The travel distance between {origin} and {destination} is approximately: {distance}")

if __name__ == "__main__":
    main()
