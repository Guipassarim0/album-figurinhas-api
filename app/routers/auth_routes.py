from fastapi import APIRouter, Depends, HTTPException
from app.models import Usuario
from app.dependencies import pegar_sessao
from app.main import bcrypt_context
from app.schemas import Usuario_Schema
from sqlalchemy.orm import Session

auth_router = APIRouter(prefix='/auth', tags=['Authentication'])

@auth_router.get('/')
async def home():
    
    return{'mensagem': 'voce esta logado'}

@auth_router.post('/criar_conta')
async def criar_conta(usuario_schema: Usuario_Schema, session: Session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==usuario_schema.email).first()
    if usuario:

        raise HTTPException(status_code=400, detail='Já existe um usuario com este email')
    else:
        senha_hash = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_hash, usuario_schema.ativo, usuario_schema.admin)
        session.add(novo_usuario)
        session.commit()
        return {'mensagem': f'usuario cadastrado com sucesso {usuario_schema.email}'}
    