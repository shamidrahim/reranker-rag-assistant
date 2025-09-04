# 📚 Reranker RAG Assistant

A Retrieval-Augmented Generation (RAG) system with **cross-encoder reranking**.  
This project lets you upload documents, retrieve the most relevant chunks, rerank them using a cross-encoder, and query them with an LLM (**OpenAI GPT-4o-mini**).

It includes a **FastAPI backend** and a **Streamlit frontend** for easy interaction.

---

## 🚀 Features
- 📂 Upload documents (`.pdf`, `.txt`, `.csv`, `.xlsx`, `.docx`)
- ✂️ Split documents into chunks with **LangChain’s RecursiveCharacterTextSplitter**
- 🔍 Store & retrieve embeddings using **FAISS**
- ⚖️ Rerank search results using **sentence-transformers cross-encoder** (`ms-marco-MiniLM-L-6-v2`)
- 🤖 Query documents using **OpenAI GPT-4o-mini**
- 💬 Session-based chat history
- 🌐 Streamlit web interface
- ⚡ FastAPI backend

---

## 🛠️ Installation

Clone this repository:

```bash
git clone https://github.com/shamidrahim/reranker-rag-assistant.git
cd reranker-rag-assistant
Create a virtual environment and activate it:

bash
Copy code
# Mac/Linux
python -m venv venv
source venv/bin/activate
powershell
Copy code
# Windows (PowerShell)
python -m venv venv
venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
🔑 Environment Variables
Create a .env file (here called var.env) in the project root:

bash
Copy code
OPENAI_API_KEY=sk-your-real-key-here
⚠️ Do not commit your real API key.
Instead, use var.env.example to share the required format with collaborators.

▶️ Running the Project
Start the FastAPI backend:

bash
Copy code
uvicorn main:app --reload
The API will be available at:
👉 http://127.0.0.1:8000

Start the Streamlit frontend:

bash
Copy code
streamlit run streamlit_app.py
The app will run at:
👉 http://localhost:8501

📂 Project Structure
php
Copy code
reranker-rag-assistant/
│── __pycache__/           # Python cache files
│── venv/                  # Virtual environment
│── main.py                # FastAPI backend
│── rag_assist.py          # RAG logic (loading, retrieval, reranking, LLM)
│── streamlit_app.py       # Streamlit frontend
│── requirements.txt       # Dependencies
│── var.env                # Local environment variables (ignored in git)
│── var.env.example        # Example env file
│── .gitignore             # Ignore venv, env files, cache
📜 License
This project is licensed under the MIT License.

🙌 Acknowledgements
LangChain – text splitting & retrieval

FAISS – vector similarity search

Sentence-Transformers – cross-encoder reranking

OpenAI – GPT models
