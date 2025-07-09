from app.models.document import Document
from app.schemas.document import DocumentCreate
from sqlalchemy.orm import Session


def create_document(db: Session, doc: DocumentCreate):
    db_doc = Document(**doc.dict())
    db.add(db_doc)
    db.commit()
    db.refresh(db_doc)
    return db_doc


def list_documents(db: Session):
    return db.query(Document).all()
