✈️ FlightPal — AI Travel Assistant

FlightPal is an AI-powered travel assistant that combines Retrieval-Augmented Generation (RAG), Model Context Protocol (MCP), LangChain, and Claude Desktop to provide real-time flight information, weather updates, and airline policy assistance through natural language conversations.

Instead of searching across multiple airline websites and travel portals, users can simply ask FlightPal questions such as:

"Check flight AA100"
"What's the weather at Heathrow?"
"What baggage allowance does Emirates allow?"
"Search Air India cabin baggage rules"

FlightPal intelligently retrieves live information from APIs while also searching a local knowledge base of airline documents.

🚀 Features
✈️ Live Flight Status

Retrieve real-time flight information using AviationStack API.

Returns:

Flight Status
Airline
Departure Airport
Arrival Airport
Departure Gate
Arrival Gate
Flight Delays

Example

Check flight AA100
🌤 Live Weather

Retrieve current weather information for any city or airport.

Returns

Temperature
Wind Speed
Location
Country

Example

Weather in London
🌦 Flight + Weather

Combines two tools.

Input

AA100

Returns

Flight Status
Arrival Airport
Destination Weather
📚 Airline Knowledge Base (RAG)

FlightPal includes a Retrieval-Augmented Generation (RAG) pipeline that searches airline documentation stored locally.

Supported information includes

Cabin baggage rules
Checked baggage allowance
Dangerous goods
Visa requirements
Travel policies
Airline baggage fees
Special baggage
International travel information
🤖 Claude Desktop Integration

FlightPal is exposed as an MCP Server, allowing Claude Desktop to invoke custom Python tools directly.

Available MCP tools

weather
flight_status
flight_weather
baggage

Claude automatically selects the appropriate tool based on the user's request.

🏗 Project Architecture
                    Claude Desktop
                           │
                           │
                 Model Context Protocol
                           │
                           ▼
                FlightPal MCP Server
                           │
       ┌───────────────────┼────────────────────┐
       │                   │                    │
       ▼                   ▼                    ▼
 Flight API          Weather API         RAG Pipeline
                                               │
                                               ▼
                                       Chroma Vector DB
                                               │
                                               ▼
                                     Airline PDF Documents
📂 Project Structure
FlightPal-Claude/

│
├── data/
│      Airline PDF documents
│
├── database/
│      Chroma Vector Database
│
├── src/
│
│   ├── api/
│   │      Flight API
│   │      Weather API
│   │
│   ├── mcp/
│   │      MCP Server
│   │
│   ├── rag/
│   │      Document Loader
│   │      Vector Store
│   │      Build Database
│   │      RAG Pipeline
│   │
│   ├── tools/
│   │      weather_tool.py
│   │      flight_tool.py
│   │      flight_weather_tool.py
│   │      rag_tool.py
│   │
│   └── config.py
│
├── tests/
│
├── requirements.txt
│
└── README.md
🛠 Technologies Used
AI
Anthropic Claude Desktop
Model Context Protocol (MCP)
LangChain
Retrieval
ChromaDB
HuggingFace Embeddings
APIs
AviationStack API
Open-Meteo API
Programming Language
Python 3.10+
⚙️ Installation
Clone Repository
git clone https://github.com/<your-username>/FlightPal-Claude.git

cd FlightPal-Claude
Create Virtual Environment
python -m venv venv

Windows

venv\Scripts\activate

Linux / Mac

source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
🔑 Environment Variables

Create a .env file.

AVIATIONSTACK_API_KEY=YOUR_API_KEY
📄 Build the Knowledge Base

Load airline documents into ChromaDB.

python -m src.rag.build_db

Expected Output

Loaded:
AirIndia.pdf
Emirates.pdf
American.pdf

Database Created Successfully
🧪 Testing

Run

python -m tests.test_tools

This verifies

Weather Tool
Flight Tool
Flight Weather Tool
RAG Tool
🤖 Running the MCP Server

Normally you do not need to start the server manually.

Claude Desktop launches it automatically.

Manual start (optional)

python -m src.mcp.server
🔌 Claude Desktop Setup

Open

Claude Desktop

Settings

Developer

Edit Config

Add the following configuration.

{
  "mcpServers": {
    "flightpal": {
      "command": "C:\\projects\\FlightPal-Claude\\venv\\Scripts\\python.exe",
      "args": [
        "C:\\projects\\FlightPal-Claude\\src\\mcp\\server.py"
      ],
      "cwd": "C:\\projects\\FlightPal-Claude",
      "env": {
        "PYTHONPATH": "C:\\projects\\FlightPal-Claude"
      }
    }
  }
}

Restart Claude Desktop.

Verify

Developer Settings

FlightPal

Running

Claude automatically discovers the following tools

weather
flight_status
flight_weather
baggage
💬 Example Queries
Flight Status
Check flight AA100
Weather
What's the weather in London?
Flight + Weather
Check flight AA100 and tell me the arrival weather.
Airline Policies
What baggage allowance does Emirates allow?
Travel Information
Search Air India cabin baggage rules.
📚 Knowledge Base

Current documents include

Air India Travel Guide
Emirates Baggage Rules
American Airlines Baggage Policy
UAE Visa Requirements
Dangerous Goods Policy
Special Baggage
Checked Baggage Allowance
Travel to USA Guide

The RAG pipeline retrieves relevant document chunks and returns grounded responses with document sources.
Future Enhancements
Airport Information Tool
Visa Requirement Tool
Lounge Finder
Terminal Maps
Airport Security Wait Times
Airline Policy Search
Voice Assistant
Streamlit / Gradio Interface
Multi-Agent Travel Planner
Hotel and Taxi Integration
👨‍💻 Author

Kishore Ravada

GitHub: https://github.com/<kishore-ravada>

LinkedIn: https://linkedin.com/in/<>

📜 License

This project is licensed under the MIT License.