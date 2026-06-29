from pydantic import BaseModel, EmailStr, Field, field_validator
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
    sigla: str = Field(pattern=r"^[a-zA-Z]{3}$")
    numero: int = Field(..., ge=1, le=20)
    observacao:  Optional[str] = None
    quantidade: int = Field(default=1, ge=1)
    
    #aceita a sigla em minusculo ou maiusculo mas apenas sera salvo em maiusculo
    @field_validator("sigla")
    @classmethod
    def transformar_em_maiusculo(cls, v: str) -> str:
        return v.upper()

class Config:
    from_attributes = True

class Login_Schema(BaseModel):
    email: EmailStr
    senha: str

class Config:
    from_attributes = True
