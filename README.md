# AI_Assistant_in_Constitution# AI Assistant for the Constitution of the Republic of Kazakhstan

This is an MVP implementation of an AI-powered assistant capable of answering questions related to the Constitution of Kazakhstan. It supports document upload, Q&A based on context, and stores query history in a vector database.

## Features
- ✅ Chat interface using **Streamlit**
- ✅ Integration with **Ollama** (supports `llama3`)
- ✅ Upload multiple **PDF/text** files
- ✅ Context-based Q&A from documents and constitution
- ✅ Stores interactions in **ChromaDB**
- ✅ Modular and scalable architecture

## Technologies Used
- **Streamlit** – Web UI
- **LangChain** – Retrieval-Augmented Generation (RAG)
- **ChromaDB** – Local vector database
- **Ollama** – Local LLM server
- **LLaMA3** – Language model
- **HuggingFace Embeddings**
- **PyPDFLoader / TextLoader**
- **RecursiveCharacterTextSplitter**

## How to Run

### Prerequisites
- Python 3.8+
- [Ollama](https://ollama.ai ) installed
- Git

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/constitution-ai-assistant.git 
   cd constitution-ai-assistant