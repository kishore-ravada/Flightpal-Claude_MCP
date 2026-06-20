import requests

from .geocoding_api import get_coordinates


def get_weather(location):

    coords = get_coordinates(location)

    if coords is None:
        return "Location not found"

    latitude = coords["latitude"]
    longitude = coords["longitude"]

    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        f"&current=temperature_2m,wind_speed_10m"
    )

    headers = {
        "User-Agent": "FlightPal/1.0"
    }

    try:

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

    except requests.RequestException as e:

        return f"Weather API Error: {e}"

    data = response.json()

    current = data.get("current")

    if current is None:
        return "Weather unavailable"

    return {
        "location": coords["name"],
        "country": coords["country"],
        "temperature": current.get("temperature_2m"),
        "wind_speed": current.get("wind_speed_10m")
    }