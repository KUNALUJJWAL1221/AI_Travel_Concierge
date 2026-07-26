import requests

from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

from config import WEATHERSTACK_API_KEY
from rag import ask_question

# -----------------------------------
# Global Retriever
# -----------------------------------

retriever = None


def set_retriever(new_retriever):
    """Update the active retriever."""
    global retriever
    retriever = new_retriever


# -----------------------------------
# Document Search Tool
# -----------------------------------

@tool
def document_search(question: str) -> str:
    """
    Search the uploaded travel guide.
    Use this tool whenever the user asks
    questions about the uploaded document.
    """

    if retriever is None:
        return "No travel guide has been uploaded."

    return ask_question(
        retriever,
        question,
    )


# -----------------------------------
# DuckDuckGo Search Tool
# -----------------------------------

search = DuckDuckGoSearchRun()


@tool
def web_search(query: str) -> str:
    """
    Search the web for recent information.
    Use this when information is not available
    in the uploaded travel guide.
    """

    return search.invoke(query)


# -----------------------------------
# WeatherStack Tool
# -----------------------------------

@tool
def get_weather(city: str) -> str:
    """
    Get the current weather for a city.
    """

    url = "https://api.weatherstack.com/current"

    params = {
        "access_key": WEATHERSTACK_API_KEY,
        "query": city,
    }

    response = requests.get(
        url,
        params=params,
        timeout=20,
    )

    data = response.json()
    print(data)

    if "current" not in data:
        return "Weather information not found."

    current = data["current"]

    temp = current.get("temperature")

    if temp is None or temp < -100 or temp > 70:
        return "Weather service returned invalid temperature."

    return (
        f"Temperature: {current['temperature']}°C\n"
        f"Weather: {current['weather_descriptions'][0]}\n"
        f"Humidity: {current['humidity']}%\n"
        f"Wind Speed: {current['wind_speed']} km/h"
    )