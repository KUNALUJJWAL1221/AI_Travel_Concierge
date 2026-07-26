from langchain_core.messages import HumanMessage

from graph import graph


def ask_agent(question: str) -> str:
    """
    Send a user question to the LangGraph agent
    and return the final response.
    """

    result = graph.invoke(
        {
            "messages": [
                HumanMessage(content=question)
            ]
        }
    )

    final_message = result["messages"][-1]

    # Gemini sometimes returns a list instead of a string
    if isinstance(final_message.content, list):

        text = ""

        for item in final_message.content:
            if item.get("type") == "text":
                text += item.get("text", "")

        return text

    return final_message.content