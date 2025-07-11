from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.db.session import Base, engine
from app.routes import document, home, upload, chat
from app.settings import get_settings


settings = get_settings()

app = FastAPI(title=settings.app_name, debug=settings.debug)

Base.metadata.create_all(bind=engine)

app.include_router(document.router)
app.include_router(home.router)
app.include_router(upload.router)
app.include_router(chat.router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
