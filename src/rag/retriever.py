from rag.vectorstore import load_vectorestore

db = load_vectorestore()


def retrieve_context(query:str, k: int = 3):

    return db.similarity_search(query, k=k)