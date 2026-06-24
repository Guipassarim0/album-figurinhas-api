from fastapi import FastAPI
from app.database import engine, Base
from app import models

Base.metadata.create_all(bind=engine)

app = FastAPI()

from app.routers.figurinhas_routes import figurinhas_router
from app.routers.auth_routes import auth_router

app.include_router(figurinhas_router)
app.include_router(auth_router)

