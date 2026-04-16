from fastapi import status
from httpx import AsyncClient
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

async def test_delete_post_sucess(client: AsyncClient, access_token: str):
  #Given | O que eu quero
  headers = {"Authorization": f"Bearer {access_token}"}
  post_id = 1

  #When | O que eu faço
  response = await client.delete(f"/posts/{post_id}", headers = headers)

  #Then | O que eu espero
  assert response.status_code == status.HTTP_204_NO_CONTENT
  
async def test_delete_post_not_authenticated_fail(client: AsyncClient):
  #Given | O que eu quero
  post_id = 1

  #When | O que eu faço
  response = await client.delete(f"/posts/{post_id}", headers = {})

  #Then | O que eu espero
  assert response.status_code == status.HTTP_401_UNAUTHORIZED
  
async def test_delete_post_not_found_fail(client: AsyncClient, access_token: str):
  #Given | O que eu quero
  headers = {"Authorization": f"Bearer {access_token}"}
  post_id = 66

  #When | O que eu faço
  response = await client.delete(f"/posts/{post_id}", headers = headers)

  #Then | O que eu espero
  assert response.status_code == status.HTTP_204_NO_CONTENT