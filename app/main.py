from fastapi import FastAPI
from app.db.session import Base, engine
from app.routes import document, home, upload

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(document.router)
app.include_router(home.router)
app.include_router(upload.router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")


