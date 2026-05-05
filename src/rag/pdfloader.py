from langchain_community.document_loaders import PyPDFLoader
from rag.loader import split_text




def loaderpdf(path:str):

    loader = PyPDFLoader(path)
    documents = loader.load()








    full_text = "\n".join([doc.page_content for doc in documents])

    chunk = split_text(full_text)



    return chunk