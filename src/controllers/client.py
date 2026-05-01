
from fastapi import APIRouter, Depends, status

from src.core.security import login_required
from src.schemas.client import ClientIn, ClientOut, ClientUpdate
from src.service.client import ClientService


router = APIRouter(
  prefix = "/client",
  tags = ["client"],
  dependencies = [Depends(login_required)]
)

client_service = ClientService()

@router.post(
  "/create",
  response_model = ClientOut,
  status_code = status.HTTP_201_CREATED,
  tags = ["client"]
)
async def create_client(client : ClientIn) -> int:
  return await client_service.create(client)

@router.get(
  "/{client_id}",
  response_model = ClientOut,
  tags = ["client"]
)
async def read_client(client_id : int) -> ClientOut | None:
  return await client_service.read_client(client_id)

@router.patch(
  "/{client_id}",
  response_model = ClientOut,
  tags = ["client"]
)
async def update_client(client_id : int, client : ClientUpdate) -> ClientOut | None:
  return await client_service.update_client(client_id, client)

@router.delete(
  "/{client_id}",
  tags = ["client"]
)
async def delete_client(client_id : int) -> ClientOut | None:
  return await client_service.delete_client(client_id)

@router.get(
  "/read-with-account/{client_id}",
  response_model = ClientOut,
  tags = ["client"]
)
async def read_client_with_account(client_id : int) -> ClientOut | None:
  return await client_service.read_client_with_account(client_id)