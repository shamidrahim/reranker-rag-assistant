📚 Reranker RAG Assistant

A Retrieval-Augmented Generation (RAG) system with cross-encoder reranking.
This project lets you upload documents, retrieve the most relevant chunks, rerank them using a cross-encoder, and query them with an LLM (OpenAI GPT-4o-mini).

It includes a FastAPI backend and a Streamlit frontend for easy interaction.

🚀 Features

Upload documents (.pdf, .txt, .csv, .xlsx, .docx).

Split documents into chunks using LangChain’s RecursiveCharacterTextSplitter.

Store and retrieve embeddings with FAISS.

Re-rank results with sentence-transformers cross-encoder (ms-marco-MiniLM-L-6-v2).

Query documents using OpenAI GPT-4o-mini.

Chat history preserved per session.

Web interface with Streamlit.

Backend powered by FastAPI.

🛠️ Installation

Clone this repository:

git clone https://github.com/your-username/reranker-rag-assistant.git
cd reranker-rag-assistant


Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows


Install dependencies:

pip install -r requirements.txt

🔑 Environment Variables

Create a var.env file in the project root with:

OPENAI_API_KEY=sk-your-real-key-here


⚠️ Do not commit your real API key. Instead, use var.env.example to show the required format.

▶️ Running the Project
Start FastAPI backend
uvicorn main:app --reload


Runs at http://127.0.0.1:8000

Start Streamlit frontend
streamlit run streamlit_app.py


Runs at http://localhost:8501

📂 Project Structure
RAG project/
│── __pycache__/             # Python cache files
│── venv/                    # Virtual environment
│── main.py                  # FastAPI backend
│── rag_assist.py            # RAG logic (loading, retrieval, reranking, LLM)
│── streamlit_app.py         # Streamlit frontend
│── requirements.txt         # Dependencies
│── var.env                  # Local environment variables (ignored in git)
│── var.env.example          # Example env file for collaborators
│── .gitignore               # Ignore venv, env files, cache

📜 License

This project is licensed under the MIT License
.

🙌 Acknowledgements

LangChain
 for text splitting & retrieval.

FAISS
 for vector similarity search.

Sentence-Transformers
 for reranking.

OpenAI
 for GPT models.