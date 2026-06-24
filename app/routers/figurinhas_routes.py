from fastapi import APIRouter

figurinhas_router = APIRouter(prefix='/figurinhas', tags=['Figurinha'])

@figurinhas_router.get('/')
async def figurinhas():
    return {'mensagem': 'lista de figurinhas'}
