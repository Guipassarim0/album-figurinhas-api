from fastapi import FastAPI
from app.database import engine, Base
from app import models
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('ACCES_TOKEN_EXPIRE_MINUTES'))

Base.metadata.create_all(bind=engine)

app = FastAPI()


oauth2_schema = OAuth2PasswordBearer(tokenUrl="/auth/login_form")
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

from app.routers.figurinhas_routes import figurinhas_router
from app.routers.auth_routes import auth_router

app.include_router(auth_router)
app.include_router(figurinhas_router)


