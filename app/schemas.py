from pydantic import BaseModel, EmailStr, Field
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
    usuario_id: int
    quantidade: int = Field(default=1, ge=1)
    

class Config:
    from_attributes = True
