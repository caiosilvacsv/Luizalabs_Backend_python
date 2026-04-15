from fastapi      import HTTPException, status, APIRouter

from database     import database
from service.post import PostService
from models.post  import posts
from schemas.post import PostIn
from views.post   import PostOut


#Exemplo de logging para o FastAPI e uvicorn
import logging


logger = logging.getLogger("uvicorn.info")
logger.setLevel(logging.INFO)

router = APIRouter(
    prefix = '/posts',
    tags= ['posts',],
  )

service = PostService()

#CRUD - GET - Ler os posts
@router.get('/', response_model = list[PostOut])
async def read_posts( published: bool, limit: int, skip: int = 0 ):
  return await service.real_all(published, limit, skip)


#CRUD - POST - Criar um post
@router.post('/',status_code = status.HTTP_201_CREATED, response_model = PostOut)
async def create_post(post: PostIn):
  return {**post.model_dump(), "id": await service.create(post)}


#CRUD - GET - Ler um post pelo id
@router.get('/{id}', response_model = PostOut)
async def read_post(id: int):
  return await service.read(id)

#CRUD - PATCH - Atualizar um post pelo id
@router.patch('/{id}', response_model = PostOut)
async def update_post(id: int, post: PostIn):
  return await service.update(id, post)


#CRUD - DELETE - Deletar um post pelo id
@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT, response_model=None)
async def delete_post(id: int):
  await service.delete(id)