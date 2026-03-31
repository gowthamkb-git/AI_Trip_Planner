# AI Trip Planner

An Agentic AI application that helps users plan trips worldwide by providing real-time weather reports, place attractions, activities, hotel recommendations, cost estimation, currency conversion, and a summarised trip document.

## Features

- Real-time weather information for any destination
- Place search & attractions discovery
- Hotel recommendations
- Cost estimation & expense tracking
- Currency conversion (worldwide)
- Summarised trip report generation

## Tech Stack

- **LLM** - OpenAI / Groq
- **Framework** - LangChain / LangGraph
- **Search** - Tavily, Google Places, Foursquare
- **Weather** - OpenWeatherMap
- **Currency** - Exchange Rate API
- **Tracing** - LangSmith
- **Backend** - FastAPI
- **Frontend** - Streamlit

## Project Structure

```
AI_Trip_Planner/
├── agent/
│   ├── __init__.py
│   └── agentic_workflow.py       # Agentic workflow logic (LangGraph)
├── config/
│   ├── __init__.py
│   └── config.yaml               # App configuration (LLM providers)
├── notebook/
│   └── experiments.ipynb         # Experimentation & prototyping
├── prompt_library/
│   ├── __init__.py
│   └── prompt.py                 # Prompt templates
├── tools/
│   ├── __init__.py
│   ├── weather_info_tool.py      # Real-time weather tool
│   ├── place_search_tool.py      # Place search & attractions tool
│   ├── currency_conversion_tool.py  # Currency conversion tool
│   ├── expense_calculator_tool.py   # Cost calculation tool
│   └── arthamatic_op_tool.py    # Arithmetic operations tool
├── utils/
│   ├── __init__.py
│   ├── model_loader.py           # LLM model loader
│   ├── config_loader.py          # Config loader
│   ├── weather_info.py           # Weather helper
│   ├── currency_converter.py     # Currency converter helper
│   ├── place_info_search.py      # Place info helper
│   ├── expense_calculator.py     # Calculator helper
│   └── save_to_document.py      # Saves summarised trip report
├── logger/
│   ├── __init__.py
│   └── logging.py                # App-wide logging configuration
├── exception/
│   ├── __init__.py
│   └── exceptiohandling.py       # Custom exception handling
├── main.py                       # FastAPI backend entry point
├── streamlit_app.py              # Streamlit frontend entry point
├── .env                          # Environment variables (secrets)
├── .env.name                     # Env variable template
├── setup.py                      # Package setup & dependencies
├── pyproject.toml                # Project dependencies
└── requirements.txt              # Python dependencies
```

## Setup

1. Clone the repository
```bash
git clone https://github.com/gowthamkb-git/AI_Trip_Planner.git
cd AI_Trip_Planner
```

2. Create and activate virtual environment
```bash
uv venv
.venv\Scripts\activate.bat
```

3. Install dependencies
```bash
uv pip install -r requirements.txt
```

4. Configure environment variables
```bash
cp .env.name .env
# Fill in your API keys in .env
```

5. Run the FastAPI backend
```bash
uvicorn main:app --reload
```

6. Run the Streamlit frontend
```bash
streamlit run streamlit_app.py
```

## Environment Variables

| Variable | Description |
|---|---|
| `OPENAI_API_KEY` | OpenAI API key |
| `GROQ_API_KEY` | Groq API key |
| `GOOGLE_API_KEY` | Google API key |
| `LANGCHAIN_API_KEY` | LangSmith API key |
| `OPENWEATHER_API_KEY` | OpenWeatherMap API key |
| `GOOGLE_PLACES_API_KEY` | Google Places API key |
| `FOURSQUARE_API_KEY` | Foursquare API key |
| `TAVILY_API_KEY` | Tavily search API key |
| `EXCHANGE_RATE_API_KEY` | Exchange Rate API key |

## CI/CD

Deployment is handled via GitHub Actions. *(Coming soon)*
