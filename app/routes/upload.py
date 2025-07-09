from fastapi import APIRouter, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

import shutil
import os

from app.db.session import SessionLocal
from app.schemas.document import DocumentCreate
from app.services.document import create_document


router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.get("/upload", response_class=HTMLResponse)
def upload_page(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})


@router.post("/upload")
async def handle_upload(request: Request, file: UploadFile = File(...)):
    file_location = f"{UPLOAD_FOLDER}/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

        db = SessionLocal()

        try:
            relative_path = f"{UPLOAD_FOLDER}/{file.filename}"
            doc = DocumentCreate(filename=file.filename, path=relative_path, content="")
            create_document(db, doc)
        finally:
            db.close()

    return RedirectResponse(f"/chat/{file.filename}", status_code=303)
