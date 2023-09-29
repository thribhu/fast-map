import os
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import requests

load_dotenv()
app = FastAPI()

GOOGLE_API_KEY = os.getenv("GOOGLE_MAP_KEY")

@app.get("/directions/")
async def get_directions(origin: str, destination: str):
    # Google Maps Directions API endpoint
    endpoint = "https://maps.googleapis.com/maps/api/directions/json"

    params = {
        "origin": origin,
        "destination": destination,
        "key": GOOGLE_API_KEY
    }

    response = requests.get(endpoint, params=params).json()

    if response['status'] != 'OK':
        raise HTTPException(status_code=400, detail=f"Error: {response['status']}")

    route = response['routes'][0]
    leg = route['legs'][0]
    distance = leg['distance']['text']
    duration = leg['duration']['text']

    directions = {
        "origin": origin,
        "destination": destination,
        "distance": distance,
        "duration": duration,
    }

    return directions
