from fastapi import status
from httpx import AsyncClient


async def test_create_post_sucess(client : AsyncClient, access_token : str):
  #Given | O que eu quero
  headers = {"Authorization": f"Bearer {access_token}"}
  data = {
    "title": "post 1", 
    "content": "content 1", 
    "published_at": "2026-04-16T07:56:00Z",
    "published": True
  }
  
  #When | O que eu faço
  response = await client.post("/posts/", json = data, headers = headers)

  #Then | O que eu espero
  assert response.status_code == status.HTTP_201_CREATED
  assert response.json()["id"] is not None
  
async def test_create_post_invalid_payload_fail(client : AsyncClient, access_token : str):
  #Given | O que eu quero
  headers = {"Authorization": f"Bearer {access_token}"}
  data = { 
    "content": "content 1", 
    "published_at": "2026-04-16T07:56:00Z",
    "published": True
  }
  
  #When | O que eu faço
  response = await client.post("/posts/", json = data, headers = headers)

  #Then | O que eu espero
  assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT
  assert response.json()["detail"][0]["loc"] == ["body", "title"] 
  
async def test_create_post_invalid_title_fail(client : AsyncClient, access_token : str):
  #Given | O que eu quero
  headers = {"Authorization": f"Bearer {access_token}"}
  data = { 
    "title": "post 1",
    "content": "content 1", 
    "published_at": "2026-04-16T07:56:00Z",
    "published": True
  }
  await client.post("/posts/", json = data, headers = headers)
  
  #When | O que eu faço
  response = await client.post("/posts/", json = data, headers = headers)

  #Then | O que eu espero
  assert response.status_code == status.HTTP_400_BAD_REQUEST
  assert response.json()["detail"] == "Post already exists"
  
async def test_create_post_not_authenticated_fail(client : AsyncClient):
  #Given | O que eu quero
  data = { 
    "title": "authenticated",
    "content": "content 1", 
    "published_at": "2026-04-16T07:56:00Z",
    "published": True
  }
  
  #When | O que eu faço
  response = await client.post("/posts/", json = data, headers = {})
  
  #Then | O que eu espero
  assert response.status_code == status.HTTP_401_UNAUTHORIZED
