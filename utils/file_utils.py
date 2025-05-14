from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import tempfile
import os

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

def process_uploaded_files(files):
    all_docs = []
    for file in files:
        suffix = os.path.splitext(file.name)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_file:
            tmp_file.write(file.getvalue())
            tmp_path = tmp_file.name
        if suffix == ".pdf":
            loader = PyPDFLoader(tmp_path)
        elif suffix == ".txt":
            loader = TextLoader(tmp_path)
        else:
            continue
        docs = loader.load()
        split_docs = text_splitter.split_documents(docs)
        all_docs.extend(split_docs)
        os.remove(tmp_path)
    return all_docs