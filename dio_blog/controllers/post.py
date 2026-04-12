from typing import Annotated

from fastapi import Cookie, Header, Response, status, APIRouter
from datetime import datetime, UTC

#Exemplo de logging para o FastAPI e uvicorn
import logging

from views.post import PostOut
from schemas.post import PostIn

logger = logging.getLogger("uvicorn.info")
logger.setLevel(logging.INFO)

#Fake DB
#Exemplo de banco de dados
fake_DB = [
    {
      "title": "Criando uma aplicação com FASTAPI",
      'author': "teste",
      "published_at": "2026-04-10T13:17:01.575868+00:00",
      "published": True
    },
    {
      "title": "Internacionalizando um app com Django",
      'author': "teste",
      "published_at": "2026-04-10T13:17:01.575871+00:00",
      "published": True
    },
    {
      "title": "Criando uma aplicação com Django",
      'author': "teste",
      "published_at": "2026-04-10T13:17:01.575874+00:00",
      "published": True
    },
    {
      "title": "Internacionalizando um app com FastAPI",
      'author': "teste",
      "published_at": "2026-04-10T13:17:01.575877+00:00",
      "published": False
    }
]


router = APIRouter(
    prefix = '/posts',
    tags= ['posts',],
    
  )


#Exemplo com Path parameters
@router.get('/{framework}', response_model = PostOut)
def read_post(framework: str):
  return {
      "posts": [
        {
          'title': f'Criando uma aplicação com {framework}',
          'published_at': datetime.now(UTC),
        },
        {
          'title': f'Internacionalizando um app com {framework}',
          'published_at': datetime.now(UTC),
        }
      ]
    }

#Exemplo com Query parameters
@router.get('/', response_model = list[PostOut])
def read_posts( published: bool, limit: int, skip: int = 0 ):
  # Modo simples de ser feito, mas falho em escala.
  # Pois anteriormente limit era descrito como "limit: int = len(fake_DB) 
  return [post for post in fake_DB[skip: skip + limit] 
          if post['published'] is published]

#Exemplo de Request body
@router.post('/',status_code = status.HTTP_201_CREATED, response_model = PostOut)
def create_post(post: PostIn):
  fake_DB.append(post.model_dump())
  return post

#Exemplo de cookies
@router.get('/cookie', response_model = list[PostOut])
def read_post(
    published: bool,
    limit: int,
    response: Response,
    skip: int = 0,
    ads_id: Annotated[str | None, Cookie()] = None
):
  response.set_cookie(key = "user", value= "luizalabs@gmail.com")
  logger.info(f"Cookie: {ads_id}")
  return [post for post in fake_DB[skip: skip + limit] 
          if post['published'] is published]
  
#Exemplo de headers
@router.get('/headers', response_model = list[PostOut])
def read_post(
    published: bool,
    limit: int,
    response: Response,
    skip: int = 0,
    ads_id: Annotated[str | None, Cookie()] = None,
    user_agent: Annotated[str | None, Header()] = None,
): 
  response.set_cookie(key = "user", value= "luizalabs@gmail.com")
  logger.info(f"Cookie: {ads_id}")
  logger.info(f"User-Agent: {user_agent}")
  return [post for post in fake_DB[skip: skip + limit] 
          if post['published'] is published]
  
 