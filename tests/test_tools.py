from src.tools.weather_tool import weather_tool
from src.tools.flight_tool import flight_tool
from src.tools.flight_weather_tool import flight_weather_tool
from src.tools.rag_tool import rag_tool

print("="*50)
print(weather_tool("London"))

print("="*50)
print(flight_tool("AA100"))

print("="*50)
print(flight_weather_tool("AA100"))

print("="*50)
print(rag_tool("What baggage allowance do I get?"))