from langchain_community.vectorstores import Chroma
from rag.embeddings import getembeddings



def create_vectorstore(chunks):
    embeddings = getembeddings()

    db = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )
    return db



def load_vectorestore():
    embeddings = getembeddings()

    return Chroma(
        persist_directory="./chroma_db",
        embedding_function=embeddings
    )

