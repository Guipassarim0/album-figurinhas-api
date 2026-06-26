from pydantic import BaseModel, EmailStr
from typing import Optional

class Usuario_Schema(BaseModel):
    nome : str
    email: EmailStr
    senha: str 
    ativo: Optional[bool] = True
    admin: Optional[bool] = False

class Config:
    from_attributes = True


class Figurinha_Schema(BaseModel):
    sigla: str
    numero: int
    observacao:  Optional[str] = None
    id_usuario: int
    quantidade: int
    

class Config:
    from_attributes = True
