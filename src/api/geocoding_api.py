import requests


def get_coordinates(location):

    url = (
        f"https://geocoding-api.open-meteo.com/v1/search"
        f"?name={location}"
        f"&count=1"
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

    except requests.RequestException:

        return None

    data = response.json()

    results = data.get("results")

    if not results:
        return None

    place = results[0]

    return {
        "name": place.get("name"),
        "country": place.get("country", ""),
        "latitude": place.get("latitude"),
        "longitude": place.get("longitude")
    }