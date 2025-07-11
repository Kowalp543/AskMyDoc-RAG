from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from fastapi import Body
from sqlalchemy.orm import Session
import os

from app.rag.loader import load_and_split
from app.rag.vectorstore import store_embeddings
from app.rag.qa import create_qa_chain
from app.db.session import SessionLocal
from app.models.document import Document


router = APIRouter()
templates = Jinja2Templates(directory="app/templates")
UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/chat/{filename:path}", response_class=HTMLResponse)
async def chat_with_document(request: Request, filename: str, db: Session = Depends(get_db)):
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    try:
        document = db.query(Document).filter_by(filename=filename).first()

        if document and document.content:

            summary = document.content
        else:

            docs = load_and_split(file_path)

            vectordb = store_embeddings(docs)

            qa_chain = create_qa_chain(vectordb)

            summary_prompt = "Give a short summary of this document in 3 sentences."
            result = qa_chain.invoke(summary_prompt)

            summary = (
                result["result"]
                if isinstance(result, dict) and "result" in result
                else str(result)
            )

            if document:
                document.content = summary
                db.commit()
            else:
                new_doc = Document(filename=filename, path=file_path, content=summary)
                db.add(new_doc)
                db.commit()

    finally:
        db.close()

    return templates.TemplateResponse(
        "chat.html", {"request": request, "filename": filename, "summary": summary}
    )


@router.post("/chat/{filename:path}/ask")
async def ask_question(filename: str, body: dict = Body(...)):
    question = body.get("question")

    if not question:
        return JSONResponse({"error": "No question provided"}, status_code=400)

    file_path = os.path.join(UPLOAD_FOLDER, filename)
    docs = load_and_split(file_path)
    vectordb = store_embeddings(docs)
    qa_chain = create_qa_chain(vectordb)

    try:
        answer = qa_chain.invoke(question)
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

    return JSONResponse({"answer": answer["result"]})
