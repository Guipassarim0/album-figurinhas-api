from fastapi import FastAPI
from app.database import engine, Base
from app import models
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

Base.metadata.create_all(bind=engine)

app = FastAPI()

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

from app.routers.figurinhas_routes import figurinhas_router
from app.routers.auth_routes import auth_router

app.include_router(auth_router)
app.include_router(figurinhas_router)


