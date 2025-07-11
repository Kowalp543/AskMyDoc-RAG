from pydantic import BaseModel


class DocumentCreate(BaseModel):
    filename: str
    content: str
    path: str


class DocumentOut(DocumentCreate):
    id: int

    model_config = {
        "from_attributes": True
    }
