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

## Project Structure

```
AI_Trip_Planner/
├── agent/
│   ├── __init__.py
│   └── agentic_workflow.py       # Agentic workflow logic
├── config/
│   ├── __init__.py
│   └── config.yml                # App configuration
├── notebooks/
│   └── experiments.ipynb         # Experimentation & prototyping
├── prompt_library/
│   ├── __init__.py
│   └── prompt.py                 # Prompt templates
├── tools/
│   ├── __init__.py
│   ├── weather.py                # Real-time weather tool
│   ├── place_search.py           # Place search & attractions tool
│   ├── currency_converter.py     # Currency conversion tool
│   ├── calculator.py             # Cost calculation tool
│   └── arithmetic_operation.py  # Arithmetic operations tool
├── utils/
│   ├── __init__.py
│   ├── model_loader.py           # LLM model loader
│   ├── config_loader.py          # Config loader
│   ├── weather.py                # Weather helper
│   ├── currency_converter.py     # Currency converter helper
│   ├── place_info.py             # Place info helper
│   ├── calculator.py             # Calculator helper
│   └── save_to_document.py      # Saves summarised trip report
├── app.py                        # Application entry point
├── main.py                       # Main runner
├── .env                          # Environment variables (secrets)
├── .env.name                     # Env variable template
├── pyproject.toml                # Project dependencies
└── requirements.txt              # Python dependencies
```

## Setup

1. Clone the repository
```bash
git clone <repo_url>
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

5. Run the application
```bash
python app.py
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
