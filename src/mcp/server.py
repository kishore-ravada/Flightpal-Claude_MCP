from mcp.server.fastmcp import FastMCP

from src.tools.weather_tool import weather_tool
from src.tools.flight_tool import flight_tool
from src.tools.flight_weather_tool import flight_weather_tool
from src.tools.rag_tool import rag_tool

mcp = FastMCP("FlightPal")


@mcp.tool(
    description="Get current weather for any city or airport."
)
def weather(location: str):
    return weather_tool(location)


@mcp.tool(
    description="Get live status of a flight using the flight number."
)
def flight_status(flight_number: str):
    return flight_tool(flight_number)


@mcp.tool(
    description="Get arrival airport weather for a flight."
)
def flight_weather(flight_number: str):
    return flight_weather_tool(flight_number)


@mcp.tool(
    description="""
Search airline baggage rules, airport guides,
visa requirements and travel policies stored
inside the FlightPal knowledge base.
"""
)
def baggage(question: str):
    return rag_tool(question)


if __name__ == "__main__":
    mcp.run()