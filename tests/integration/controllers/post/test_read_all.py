from fastapi import status
from httpx import AsyncClient
import pytest
import pytest_asyncio


@pytest_asyncio.fixture(autouse = True)
async def populate_posts(db):
  from schemas.post import PostIn
  from service.post import PostService
  
  service = PostService()
  await service.create(PostIn(
    title =     'Post 1', 
    content =   'Conteudo 1',
    published = True
  ))
  await service.create(PostIn(
    title =     'Post 2', 
    content =   'Conteudo 2',
    published = True
  ))
  await service.create(PostIn(
    title =     'Post 3', 
    content =   'Conteudo 3',
    published = False
  ))
  
@pytest.mark.parametrize("published, total", [("on", 2), ("off", 1)])
async def test_read_posts_by_status_sucess(
  client : AsyncClient,
  access_token : str,
  published : str,
  total : int
):
  #Given | O que eu quero
  params = {"published": published, "limit": 10}
  headers = {"Authorization": f"Bearer {access_token}"}

  #When | O que eu faço
  response = await client.get("/posts/", params = params, headers = headers)

  #Then | O que eu espero
  assert response.status_code == status.HTTP_200_OK
  assert len(response.json()) == total
  
async def test_read_posts_limit_sucess(
  client : AsyncClient,
  access_token : str,
):
  #Given | O que eu quero
  params = {"published": "on", "limit": 1}
  headers = {"Authorization": f"Bearer {access_token}"}

  #When | O que eu faço
  response = await client.get("/posts/", params = params, headers = headers)

  #Then | O que eu espero
  assert response.status_code == status.HTTP_200_OK
  assert len(response.json()) == 1

async def test_read_posts_not_authenticated_fail(
  client : AsyncClient,
):
  #Given | O que eu quero
  params = {"published": "on", "limit": 1}

  #When | O que eu faço
  response = await client.get("/posts/", params = params, headers = {})

  #Then | O que eu espero
  assert response.status_code == status.HTTP_401_UNAUTHORIZED
  
async def test_read_posts_empty_parameters_fail(
  client : AsyncClient,
  access_token : str,
):
  #Given | O que eu quero
  headers = {"Authorization": f"Bearer {access_token}"}

  #When | O que eu faço
  response = await client.get("/posts/", params = {}, headers = headers)

  #Then | O que eu espero
  assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT
  
