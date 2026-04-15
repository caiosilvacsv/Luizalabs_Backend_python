from typing import Annotated

from fastapi import Cookie, FastAPI, Header, Response, status
from datetime import datetime, UTC
from pydantic import BaseModel

#Exemplo de logging para o FastAPI e uvicorn
import logging

logger = logging.getLogger("uvicorn.info")
logger.setLevel(logging.INFO)


app = FastAPI()


#Exemplo inicial
@app.get('/')
def read_root():
  return {
      "message": "Hello World"
    }

#Exemplo com Path parameters
@app.get('/post/{framework}')
def read_post(framework: str):
  return {
      "posts": [
        {
          'title': f'Criando uma aplicação com {framework}',
          'date': datetime.now(UTC),
        },
        {
          'title': f'Internacionalizando um app com {framework}',
          'date': datetime.now(UTC),
        }
      ]
    } 
  
#Exemplo de banco de dados
fake_DB = [
    {
      "title": "Criando uma aplicação com FASTAPI",
      "date": "2026-04-10T13:17:01.575868+00:00",
      'author': "teste",
      "published": True
    },
    {
      "title": "Internacionalizando um app com Django",
      "date": "2026-04-10T13:17:01.575871+00:00",
      'author': "teste",
      "published": True
    },
    {
      "title": "Criando uma aplicação com Django",
      "date": "2026-04-10T13:17:01.575874+00:00",
      'author': "teste",
      "published": True
    },
    {
      "title": "Internacionalizando um app com FastAPI",
      "date": "2026-04-10T13:17:01.575877+00:00",
      'author': "teste",
      "published": False
    }
]


#Exemplo com Query parameters
@app.get('/posts/')
def read_posts( published: bool, limit: int, skip: int = 0 ):
  # Modo simples de ser feito, mas falho em escala.
  # Pois anteriormente limit era descrito como "limit: int = len(fake_DB) 
  return [post for post in fake_DB[skip: skip + limit] 
          if post['published'] is published]
  
  
#Exemplo com Pydantic
class Post(BaseModel):
  title:      str
  date:       datetime = datetime.now(UTC)
  author:     str
  published:  bool = False

#Exemplo de Request body
@app.post('/posts/',status_code = status.HTTP_201_CREATED)
def create_post(post: Post):
  fake_DB.append(post.model_dump())
  return post

#Exemplo de cookies
@app.get('/posts/cookie')
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
@app.get('/posts/headers')
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
  
  
class Foo(BaseModel):
  bar: str

#Exemplo com response model    
@app.get('/foobar', response_model = Foo)
def foobar() -> Foo:
  return {
      "bar": "foo",
      "message": "Hello World"
  }