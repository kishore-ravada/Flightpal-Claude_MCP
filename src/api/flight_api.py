import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("AVIATIONSTACK_API_KEY")


def get_flight_status(flight_number):

    url = (
        f"http://api.aviationstack.com/v1/flights"
        f"?access_key={API_KEY}"
        f"&flight_iata={flight_number}"
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

        return f"Flight API Error: {e}"

    data = response.json()

    print("\nAPI RESPONSE:")
    print(data)

    if "error" in data:
        return data["error"].get(
            "message",
            "Unknown API error"
        )

    flights = data.get("data", [])

    if not flights:
        return "Flight not found"

    flight = flights[0]

    return {
        "flight": flight_number,
        "status": flight.get("flight_status"),
        "airline": flight.get("airline", {}).get("name"),
        "departure_airport": flight.get("departure", {}).get("airport"),
        "arrival_airport": flight.get("arrival", {}).get("airport"),
        "departure_gate": flight.get("departure", {}).get("gate"),
        "arrival_gate": flight.get("arrival", {}).get("gate"),
        "arrival_delay": flight.get("arrival", {}).get("delay")
    }