from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from ingest import ingest_pdf
from qa import answer_question

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    content = await file.read()
    ingest_pdf(content, file.filename)
    return {"message": "PDF ingested successfully."}

@app.post("/qa/")
async def qa_endpoint(question: str = Form(...)):
    answer = answer_question(question)
    return {"answer": answer}
