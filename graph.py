from typing import TypedDict, Annotated

from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

from langchain_core.messages import BaseMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

from config import (
    GOOGLE_API_KEY,
    CHAT_MODEL,
)

from tools import (
    document_search,
    web_search,
    get_weather,
    flight_search,
)


# ----------------------------------
# LLM
# ----------------------------------

llm = ChatGoogleGenerativeAI(
    model=CHAT_MODEL,
    google_api_key=GOOGLE_API_KEY,
    temperature=0.3,
)


# ----------------------------------
# Tools
# ----------------------------------

tools = [
    document_search,
    web_search,
    get_weather,
    flight_search,
]


llm_with_tools = llm.bind_tools(tools)


# ----------------------------------
# Agent State
# ----------------------------------

class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


# ----------------------------------
# System Prompt
# ----------------------------------

SYSTEM_PROMPT = """
You are an AI Travel Concierge.

You have access to four tools:

1. document_search
    - ALWAYS use this tool if the user asks about destinations,
      attractions, itineraries, hotels, restaurants, culture,
      transportation, travel tips, or anything that might exist in the
      uploaded travel guide.

2. web_search
    - Use ONLY when the user asks about information that changes over time,
      such as news, visa rules, exchange rates, current events, flight prices,
      or information that is not available in the uploaded guide.

3. get_weather
    - ALWAYS use this tool whenever the user asks about weather,
      temperature, rainfall, climate, or forecast.

4. flight_search
    - ALWAYS use this tool when the user asks about flights,
      airfare, flight prices, available flights, or flying between
      two cities or airports.
    - Use IATA airport codes for departure_id and arrival_id.
    - Use YYYY-MM-DD format for outbound_date.

Rules:

- Never invent information about the uploaded travel guide.
- If document_search cannot find the answer,
  politely say that the guide doesn't contain that information.
- Prefer document_search over your own knowledge whenever a travel guide
  could contain the answer.
- Use flight_search for live flight information instead of guessing
  flight schedules or prices.
- Keep answers clear and well formatted using Markdown.
"""

# ----------------------------------
# Chatbot Node
# ----------------------------------

def chatbot(state: AgentState):
    """
    Call Gemini with the current conversation.
    """

    messages = [
        SystemMessage(content=SYSTEM_PROMPT)
    ] + state["messages"]

    response = llm_with_tools.invoke(messages)

    return {
        "messages": [response]
    }


# ----------------------------------
# Tool Node
# ----------------------------------

tool_node = ToolNode(tools)


# ----------------------------------
# Build Graph
# ----------------------------------

graph_builder = StateGraph(AgentState)


# Nodes
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", tool_node)


# Entry point
graph_builder.set_entry_point("chatbot")


# Decide whether to use a tool
graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition,
)


# After tool execution, return to Gemini
graph_builder.add_edge(
    "tools",
    "chatbot",
)


# ----------------------------------
# Compile Graph
# ----------------------------------

graph = graph_builder.compile()
