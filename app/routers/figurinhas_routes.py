from fastapi import APIRouter, Depends, HTTPException   
from app.models import Figurinha, Usuario
from app.dependencies import pegar_sessao, verificar_token
from sqlalchemy.orm import Session
from app.schemas import Figurinha_Schema



figurinhas_router = APIRouter(prefix='/figurinhas', tags=['Figurinha'])

@figurinhas_router.get('/')
async def figurinhas():
    return {'mensagem': 'lista de figurinhas'}

@figurinhas_router.post('/criar_figurinha')
async def criar_figurinha(figurinha_schema: Figurinha_Schema, usuario: Usuario = Depends(verificar_token), session: Session = Depends(pegar_sessao)):
    figurinha = session.query(Figurinha).filter(Figurinha.sigla==figurinha_schema.sigla, Figurinha.numero==figurinha_schema.numero, Figurinha.usuario_id==usuario.id).first()
    if figurinha:
        figurinha.quantidade += figurinha_schema.quantidade
        figurinha.observacao = figurinha_schema.observacao
        session.commit()
        return {'mensagem': f'Figurinha repetida cadastrada com sucesso {figurinha_schema.sigla}, {figurinha_schema.numero}, [+{figurinha_schema.quantidade}]'}
    else:
        nova_figurinha = Figurinha(sigla=figurinha_schema.sigla, numero=figurinha_schema.numero, quantidade=figurinha_schema.quantidade, observacao=figurinha_schema.observacao, usuario_id=usuario.id)
        session.add(nova_figurinha)
        session.commit()
        return {'mensagem': f'Figurinha nova cadastrada com sucesso {figurinha_schema.sigla}, {figurinha_schema.numero}, [+{figurinha_schema.quantidade}]'}
    
@figurinhas_router.get("/listar", response_model=list[str])
async def listar_figurinhas(usuario: Usuario = Depends(verificar_token), session: Session = Depends(pegar_sessao)):
    """
    Traz todas as figurinhas que pertencem ao ID do usuário que está logado
    """
    lista_formatada = []

    minhas_figurinhas = session.query(Figurinha).filter(Figurinha.usuario_id == usuario.id).all()
    if not minhas_figurinhas:
        raise HTTPException(status_code=404, detail="Figurinha Não Encontrada")

    for figurinha in minhas_figurinhas:
        texto = f"{figurinha.sigla} {figurinha.numero} -- {figurinha.quantidade}"
        lista_formatada.append(texto)

    return lista_formatada

@figurinhas_router.post("/remover_figurinha")
async def remover_figurinha(figurinha_schema:Figurinha_Schema, usuario = Depends(verificar_token), session: Session = Depends(pegar_sessao)):
    figurinha_removida = session.query(Figurinha).filter(Figurinha.sigla==figurinha_schema.sigla, Figurinha.numero==figurinha_schema.numero, Figurinha.usuario_id==usuario.id).first()
    if not figurinha_removida:
        raise HTTPException(status_code=404, detail="Figurinha Não Encontrada")
    elif figurinha_removida.quantidade > figurinha_schema.quantidade:
        # Não deletar uma linha, apenas diminuir a quantidade
        figurinha_removida.quantidade -= figurinha_schema.quantidade
        session.commit()
        return {"mensagem": f"Figurinha(s) removida [!] com SUCESSO: {figurinha_schema.sigla, figurinha_schema.numero} [-{figurinha_schema.quantidade}]"}
    else:
        # Se o numero a remover for maior ou igual que a quantidade, deletar a linha do banco de dados
        session.delete(figurinha_removida)
        session.commit()
        return {"mensagem": f"Figurinha Deletada [-] do Album: {figurinha_schema.sigla, figurinha_schema.numero}"}