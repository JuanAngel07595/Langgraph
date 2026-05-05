from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_text(text: str):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap= 100
    )

    return splitter.split_text(text)


oe = split_text("Hola como estas, espero estes muy bien y tú, exccelente jaja gracias.")

print(oe)





