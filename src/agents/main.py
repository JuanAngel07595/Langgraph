from src.rag.retriever import retrieve_context

def agent(query: str, llm):
    context = retrieve_context(query)

    prompt = f"""
    Usa el siguiente contexto para responder:

    {context}

    Pregunta: {query}
    """

    return llm.invoke(prompt)