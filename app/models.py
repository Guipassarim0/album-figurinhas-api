from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False )
    email = Column(String, nullable=False)
    senha = Column(String, nullable=False)
    ativo = Column(Boolean)
    admin = Column(Boolean, default=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome 
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin


class Figurinha(Base):
    __tablename__ = "figurinhas"
    # ID de autoincremento automatico
    id = Column(Integer, primary_key=True, index=True)

    # Siglas das seleções com limite de 3 caracteres
    sigla = Column(String(3), nullable=False)

    #Número da figurinha da seleção (de 0 a 20)
    numero = Column(Integer, nullable=False)

    #Quantidade de figurinhas coladas/repetidas (Assume valor padrão de 1)
    quantidade = Column(Integer, nullable=False, default=1)

    #Data e hora de quando a figurinha foi registrada
    created_at = Column(DateTime, server_default=func.now())

    #Foreignkey para identificar o usuario
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)

    def __init__(self, sigla, numero, usuario_id, quantidade=1, created_at=None):
        self.sigla = sigla
        self.numero = numero
        self.usuario_id = usuario_id
        self.quantidade = quantidade
        self.created_at = created_at
    
