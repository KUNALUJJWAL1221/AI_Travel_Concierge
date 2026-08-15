import requests

from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

from config import WEATHERSTACK_API_KEY, SERPAPI_API_KEY
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

    try:

        response = requests.get(
            url,
            params=params,
            timeout=20,
        )

        data = response.json()

    except requests.exceptions.RequestException:

        return "Unable to connect to the weather service."

    if "current" not in data:
        return "Weather information not found."

    data = response.json()

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

# -----------------------------------
# SerpApi Google Flights Tool
# -----------------------------------

@tool
def flight_search(
    departure_id: str,
    arrival_id: str,
    outbound_date: str,
) -> str:
    """
    Search Google Flights for available flights.

    Use this tool when the user asks about:
    - flights
    - airfare
    - flight prices
    - available flights
    - flying between two airports or cities

    departure_id:
        IATA airport code for the departure airport.
        Example: DEL

    arrival_id:
        IATA airport code for the arrival airport.
        Example: GOI

    outbound_date:
        Departure date in YYYY-MM-DD format.
        Example: 2026-08-20
    """

    url = "https://serpapi.com/search.json"

    params = {
        "engine": "google_flights",
        "api_key": SERPAPI_API_KEY,
        "hl": "en",
        "gl": "in",
        "type": "2",
        "departure_id": departure_id.upper(),
        "arrival_id": arrival_id.upper(),
        "outbound_date": outbound_date,
        "currency": "INR",
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=20,
        )

        response.raise_for_status()
        data = response.json()

    except requests.exceptions.RequestException:
        return "Unable to connect to the flight search service."

    if "error" in data:
        return f"Flight search error: {data['error']}"

    best_flights = data.get("best_flights", [])

    if not best_flights:
        return (
            f"No flights were found from {departure_id.upper()} "
            f"to {arrival_id.upper()} on {outbound_date}."
        )

    results = []

    for flight_option in best_flights[:5]:

        flights = flight_option.get("flights", [])

        if not flights:
            continue

        first_flight = flights[0]

        departure = first_flight.get("departure_airport", {})
        arrival = first_flight.get("arrival_airport", {})

        airline = first_flight.get("airline", "Unknown airline")
        flight_number = first_flight.get(
            "flight_number",
            "Unknown flight"
        )

        departure_time = departure.get("time", "Unknown")
        arrival_time = arrival.get("time", "Unknown")

        duration = flight_option.get(
            "total_duration",
            first_flight.get("duration", "Unknown")
        )

        price = flight_option.get("price")

        if price is not None:
            price_text = f"₹{price:,}"
        else:
            price_text = "Price unavailable"

        results.append(
            f"- {airline} {flight_number}: "
            f"{departure_time} → {arrival_time}, "
            f"{duration} minutes, {price_text}"
        )

    if not results:
        return "Flight information was found, but no usable flight results were available."

    return (
        f"Flights from {departure_id.upper()} to {arrival_id.upper()} "
        f"on {outbound_date}:\n"
        + "\n".join(results)
    )

# -----------------------------------
# Basic Itinerary Generation Tool
# -----------------------------------

from langchain_google_genai import ChatGoogleGenerativeAI

from config import GOOGLE_API_KEY, CHAT_MODEL


itinerary_llm = ChatGoogleGenerativeAI(
    model=CHAT_MODEL,
    google_api_key=GOOGLE_API_KEY,
    temperature=0.4,
)


@tool
def generate_itinerary(
    destination: str,
    days: int,
) -> str:
    """
    Generate a basic day-by-day travel itinerary.

    IMPORTANT:
    Call this tool whenever the user asks for an itinerary,
    trip plan, travel plan, or day-by-day plan.

    Examples:
    - Create a 3-day itinerary for Goa.
    - Plan a 5-day trip to Kerala.
    - Make a 2-day itinerary for Jaipur.

    destination:
        The travel destination.

    days:
        Number of days for the trip.
    """

    if days < 1 or days > 14:
        return "Please choose a trip duration between 1 and 14 days."

    prompt = f"""
Create a practical {days}-day travel itinerary for {destination}.

Requirements:

- Organize the itinerary day by day.
- Include morning, afternoon, and evening activities.
- Include major attractions and experiences.
- Keep the plan realistic and not overcrowded.
- Include reasonable travel flow between nearby attractions.
- Include a short practical tip for each day.
- Use Markdown formatting.
- Do not invent specific hotel prices, flight prices, or exact opening
  hours.
- Keep the itinerary suitable for a general traveler.

Destination: {destination}
Trip duration: {days} days
"""

    try:

        response = itinerary_llm.invoke(prompt)

        return response.content

    except Exception:

        return "Unable to generate the itinerary right now."   
