from fastapi import APIRouter, Depends, HTTPException   
from app.models import Figurinha
from app.dependencies import pegar_sessao 
from sqlalchemy.orm import Session
from app.schemas import Figurinha_Schema

figurinhas_router = APIRouter(prefix='/figurinhas', tags=['Figurinha'])

@figurinhas_router.get('/')
async def figurinhas():
    return {'mensagem': 'lista de figurinhas'}

@figurinhas_router.post('/criar_figurinha')
async def criar_figurinha(figurinha_schema: Figurinha_Schema, session: Session = Depends(pegar_sessao)):
    figurinha = session.query(Figurinha).filter(Figurinha.sigla==figurinha_schema.sigla, Figurinha.numero==figurinha_schema.numero).first()
    if figurinha:
        figurinha.quantidade += figurinha_schema.quantidade
        figurinha.observacao = figurinha_schema.observacao
        session.commit()
        return {'mensagem': f'Figurinha repetida cadastrada com sucesso {figurinha_schema.sigla}, {figurinha_schema.numero}, [+{figurinha_schema.quantidade}]'}
    else:
        nova_figurinha = Figurinha(figurinha_schema.sigla, figurinha_schema.numero,figurinha_schema.observacao, figurinha_schema.id_usuario, figurinha_schema.quantidade)
        session.add(nova_figurinha)
        session.commit()
        return {'mensagem': f'Figurinha nova cadastrada com sucesso {figurinha_schema.sigla}, {figurinha_schema.numero}, [+{figurinha_schema.quantidade}]'}