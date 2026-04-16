from fastapi import status
from httpx import AsyncClient

#Estrutura BDD - Behavior - Driven Development
async def test_login_sucess(client : AsyncClient):
  #Given | O que eu quero
  data = {"user_id": 1}

  #When | O que eu faço
  response = await client.post("/auth/login", json = data)

  #Then | O que eu espero
  assert response.status_code == status.HTTP_200_OK
  assert response.json()["access_token"] is not None