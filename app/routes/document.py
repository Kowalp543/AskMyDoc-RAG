from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.document import DocumentCreate, DocumentOut
from app.services.document import create_document, list_documents
from app.db.session import SessionLocal


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/documents/", response_model=DocumentOut)
def create(doc: DocumentCreate, db: Session = Depends(get_db)):
    return create_document(db, doc)


@router.get("/documents/", response_model=list[DocumentOut])
def read_all(db: Session = Depends(get_db)):
    return list_documents(db)