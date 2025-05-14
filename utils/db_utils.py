from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
import os

CHROMA_PATH = "data/chroma_db"

def get_retriever(docs=None):
    embedding_function = HuggingFaceEmbeddings()
    if docs:
        db = Chroma.from_documents(
            documents=docs,
            embedding=embedding_function,
            persist_directory=CHROMA_PATH
        )
    else:
        db = Chroma(
            persist_directory=CHROMA_PATH,
            embedding_function=embedding_function
        )
    return db.as_retriever(search_kwargs={"k": 5})