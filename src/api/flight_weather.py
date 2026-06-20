from .flight_api import get_flight_status
from .weather_api import get_weather


def get_flight_weather(flight_number):

    flight = get_flight_status(flight_number)

    if isinstance(flight, str):
        return flight

    weather = get_weather(
        flight["arrival_airport"]
    )

    return {
        "flight": flight["flight"],
        "airline": flight["airline"],
        "status": flight["status"],
        "arrival_airport": flight["arrival_airport"],
        "arrival_gate": flight["arrival_gate"],
        "arrival_delay": flight["arrival_delay"],
        "weather": weather
    }