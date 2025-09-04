import streamlit as st
import requests

# FastAPI backend URL (adjust if deploying remotely)
FASTAPI_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="RAG Assistant", layout="centered")

st.title("📚 RAG Assistant")
st.write("Upload a document, ask questions, and get answers from the RAG system.")

# --- File Upload ---
st.header("Upload Document")
uploaded_file = st.file_uploader("Choose a file", type=["pdf", "txt", "csv", "xlsx", "docx"])

if uploaded_file is not None:
    if st.button("Process Document"):
        files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
        response = requests.post(f"{FASTAPI_URL}/upload", files=files)
        if response.status_code == 200:
            st.success(response.json()["message"])
        else:
            st.error(response.json()["error"])

# --- Chat Section ---
st.header("Ask a Question")
query = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if query.strip():
        data = {"query": query}
        response = requests.post(f"{FASTAPI_URL}/chat", data=data)
        if response.status_code == 200:
            answer = response.json()["answer"]
            st.markdown(f"**Q:** {query}")
            st.markdown(f"**A:** {answer}")
        else:
            st.error(response.json()["error"])
    else:
        st.warning("Please enter a question before submitting.")

# --- Reset Section ---
st.header("Reset Session")
if st.button("Reset Conversation"):
    response = requests.post(f"{FASTAPI_URL}/reset")
    if response.status_code == 200:
        st.success(response.json()["message"])
    else:
        st.error("Failed to reset session.")