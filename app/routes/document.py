from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse

from app.schemas.document import DocumentCreate, DocumentOut
from app.services.document import create_document, list_documents
from app.db.session import SessionLocal


router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/documents/", response_model=DocumentOut)
def create(doc: DocumentCreate, db: Session = Depends(get_db)):
    return create_document(db, doc)


@router.get("/documents/", response_class=HTMLResponse)
def documents_list(request: Request, db: Session = Depends(get_db)):

    documents_list = list_documents(db)
    documents_list_count = len(documents_list)

    return templates.TemplateResponse(
        "documents.html",
        {
            "request": request,
            "documents_list": documents_list,
            "documents_list_count": documents_list_count,
        },
    )
