from src.api.flight_api import get_flight_status


def flight_tool(flight_number):

    return get_flight_status(flight_number)