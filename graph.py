from typing import TypedDict, Annotated

from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

from langchain_core.messages import BaseMessage
from langchain_core.messages import HumanMessage
from langchain_core.messages import AIMessage

from langchain_google_genai import ChatGoogleGenerativeAI

from config import (
    GOOGLE_API_KEY,
    CHAT_MODEL,
)

from tools import (
    document_search,
    web_search,
    get_weather,
)

llm = ChatGoogleGenerativeAI(
    model=CHAT_MODEL,
    google_api_key=GOOGLE_API_KEY,
    temperature=0.3,
)

tools = [
    document_search,
    web_search,
    get_weather,
]

llm_with_tools = llm.bind_tools(tools)

class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

# ----------------------------------
# Chatbot Node
# ----------------------------------

def chatbot(state: AgentState):
    """
    Call the LLM with the current conversation.
    """

    response = llm_with_tools.invoke(state["messages"])
    print(response)

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

# Add nodes
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", tool_node)

# Entry point
graph_builder.set_entry_point("chatbot")

# Conditional routing
graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition,
)

# After tools, go back to chatbot
graph_builder.add_edge(
    "tools",
    "chatbot",
)

# Compile graph
graph = graph_builder.compile()
