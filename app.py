import streamlit as st
from utils.file_utils import process_uploaded_files
from utils.db_utils import get_retriever
from utils.llm_utils import get_llm_chain

st.set_page_config(page_title="Kazakhstan Constitution AI")
st.title("Constitution AI Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Document uploader
uploaded_files = st.file_uploader("Upload PDF or Text Documents", type=["pdf", "txt"], accept_multiple_files=True)

if uploaded_files:
    with st.spinner("Processing documents..."):
        docs = process_uploaded_files(uploaded_files)
        retriever = get_retriever(docs)
        chain = get_llm_chain(retriever)
    st.success(f"{len(uploaded_files)} file(s) processed.")
else:
    chain = get_llm_chain()

# Chat input
user_input = st.chat_input("Ask something about the Constitution...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        response = chain.run(user_input)
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})