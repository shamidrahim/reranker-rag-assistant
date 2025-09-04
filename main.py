from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
import shutil
import os
from rag_assist import RAGAssist

# Initialize FastAPI app
app = FastAPI()
rag = RAGAssist(env_path="var.env")


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """Upload and process a document"""
    try:
        allowed = {".pdf", ".txt", ".csv", ".xlsx", ".docx"}
        ext = os.path.splitext(file.filename)[1].lower()

        if ext not in allowed:
            return JSONResponse(
                status_code=415,  # 415 = Unsupported Media Type
                content={"error": "Unsupported file type"}
            )

        temp_file = f"temp_{file.filename}"
        with open(temp_file, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        rag.load_process_doc(temp_file)

        os.remove(temp_file)

        return JSONResponse(content={"message": "Document processed successfully."})
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})


@app.post("/chat")
async def chat(query: str = Form(...)):
    """Ask a question to the RAG system"""
    try:
        answer = rag.ask(query)
        return JSONResponse(content={"question": query, "answer": answer})
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})


@app.post("/reset")
async def reset():
    """Reset session and conversation history"""
    rag.reset()
    return JSONResponse(content={"message": "Session reset successfully."})

