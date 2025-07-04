from pydantic import BaseModel


class DocumentCreate(BaseModel):
    filename: str
    content: str


class DocumentOut(DocumentCreate):
    id: int

    class Config:
        orm_mode = True



