import os
from dotenv import load_dotenv
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    CSVLoader,
    UnstructuredExcelLoader,
    Docx2txtLoader,
)
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from sentence_transformers import CrossEncoder
from langchain.prompts import PromptTemplate


class RAGAssist:
    def __init__(self, env_path="var.env"):
        self.load_env_variables(env_path)
        self.cross_encoder = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
        self.llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
        self.embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
        self.retriever = None
        self.conversation_history = []

    def load_env_variables(self, env_path):
        load_dotenv(env_path)

    def rerank_documents(self, query, docs, top_k=3):
        pairs = [[query, doc.page_content] for doc in docs]
        scores = self.cross_encoder.predict(pairs)
        scored_docs = sorted(zip(docs, scores), key=lambda x: x[1], reverse=True)
        return [doc for doc, _ in scored_docs[:top_k]]

    def load_process_doc(self, file_path):
        if file_path.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
        elif file_path.endswith(".txt"):
            loader = TextLoader(file_path, encoding="utf-8")
        elif file_path.endswith(".csv"):
            loader = CSVLoader(file_path=file_path)
        elif file_path.endswith(".xlsx"):
            loader = UnstructuredExcelLoader(file_path, mode="elements")
        elif file_path.endswith(".docx"):
            loader = Docx2txtLoader(file_path)
        else:
            raise ValueError("Unsupported file type.")

        docs = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=2000, chunk_overlap=200, length_function=len
        )
        doc_split = text_splitter.split_documents(docs)
        vectorstore = FAISS.from_documents(doc_split, self.embedding_model)
        self.retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})

    def prompt(self):
        template = """
        You are a helpful assistant. Use the following context to answer the question.
        Context:
        {context}
        {history}
        Question:
        {question}
        Answer:"""
        return PromptTemplate(
            input_variables=["context", "history", "question"],
            template=template,
        )

    def ask(self, query: str):
        if not self.retriever:
            return "No document loaded. Please upload a document first."

        initial_docs = self.retriever.invoke(query)
        top_docs = self.rerank_documents(query, initial_docs)
        context_text = "\n\n".join([doc.page_content for doc in top_docs])

        history_str = ""
        for q, a in self.conversation_history:
            history_str += f"User: {q}\nAssistant: {a}\n"

        prompt = self.prompt()
        chain = prompt | self.llm

        result = chain.invoke(
            {
                "context": context_text,
                "history": history_str,
                "question": query,
            }
        )

        answer = result.content if hasattr(result, "content") else result
        self.conversation_history.append((query, answer))
        return answer

    def reset(self):
        self.retriever = None
        self.conversation_history = []