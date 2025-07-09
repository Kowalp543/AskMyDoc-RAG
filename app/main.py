from fastapi import FastAPI
from app.db.session import Base, engine
from app.routes import document, home, upload, chat

from fastapi.staticfiles import StaticFiles


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(document.router)
app.include_router(home.router)
app.include_router(upload.router)
app.include_router(chat.router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
