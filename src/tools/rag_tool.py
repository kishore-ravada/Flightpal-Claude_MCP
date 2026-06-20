from src.rag.rag_pipeline import ask_flightpal


def rag_tool(question):

    result = ask_flightpal(question)

    if not result["context"]:
        return "No relevant information found."

    return f"""
Sources:
{", ".join(result["sources"])}

Context:
{result["context"]}
"""