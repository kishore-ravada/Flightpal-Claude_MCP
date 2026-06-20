from .vector_store import get_retriever

_retriever = None


def get_db():
    global _retriever

    if _retriever is None:
        _retriever = get_retriever()

    return _retriever


def ask_flightpal(question):

    retriever = get_db()

    docs = retriever.invoke(question)

    if not docs:
        return {
            "context": "",
            "sources": []
        }

    context = "\n\n".join(doc.page_content for doc in docs)

    sources = list({
        doc.metadata.get("source", "Unknown")
        for doc in docs
    })

    return {
        "context": context,
        "sources": sources
    }