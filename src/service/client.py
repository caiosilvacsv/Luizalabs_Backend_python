
from src.exceptions.business import AccountNotFoundError, ClientNotCreatedError, ClientNotFoundError, NotUpdatedError
from src.schemas.client import ClientIn, ClientOut, ClientUpdate
from src.models.client import clients
from src.models.account import accounts
from src.database.connection import database, sa

class ClientService:
  
  async def create(
    self,
    client : ClientIn,
  ):
    new_cliente = clients.insert().values(
      name = client.name,
      status = client.status,
    )
    
    client = await database.execute(new_cliente)
    
    if not client:
      raise ClientNotCreatedError()
      
    return await database.fetch_one(clients.select().where(clients.c.id == client))
  
  async def update_client(
    self, 
    client_id : int,
    client : ClientUpdate,
  ) -> ClientOut | None:
    client_data = client.model_dump(exclude_unset=True)

    # Verifica se o campo 'closed' foi enviado e é um booleano
    if client_data.get("closed") is True:
      client_data["closed"] = sa.func.now()
    elif client_data.get("closed") is False:
      # Se for explicitamente false, remove a data de fechamento
      client_data["closed"] = None
    
    update = clients.update().where(clients.c.id == client_id).values(**client_data)
    
    cliente = await database.execute(update)
    
    if cliente == 0:
      raise NotUpdatedError("Not updated client : ", client_id)
    
    updated_client = await self.read_client(client_id)
    
    if not updated_client:
      raise ClientNotFoundError(client_id)
      
    return updated_client
  
  async def delete_client(self, client_id : int) -> ClientOut:
    delete = clients.update().where(clients.c.id == client_id).values(
      status = False,
      closed = sa.func.now(),
    )
    await database.execute(delete)
  
  async def read_client(self, client_id : int) -> ClientOut | None:
    read = clients.select().where(clients.c.id == client_id)
    client = await database.fetch_one(read)
    
    # 1. Garante que o cliente existe para não gerar um TypeError
    if not client:
      raise ClientNotFoundError(client_id)
      
    # 2. Converte para dicionário para tratar possíveis valores Nulos no banco
    result = dict(client)
    if result.get("status") is None:
      result["status"] = True
      
    if result["status"] == False:
      raise ClientNotFoundError(client_id)  
      
    return result
    
  async def read_client_with_account(
    self,
    client_id : int,
  ) -> ClientOut | None:
    client_query = (
      clients.select()
      .where(clients.c.id == client_id)
      .where(clients.c.status == True
      )
    )
    
    client = await database.fetch_one(client_query)
    
    if not client:
      raise ClientNotFoundError(client_id)
    
    account_query = (
      accounts.select()
      .where(accounts.c.client_id == client_id)
      .where(accounts.c.is_active == True)
    )
    
    account = await database.fetch_all(account_query)
    
    if not account:
      raise AccountNotFoundError(client_id)
    
    result = dict(client)
    
    result["accounts"] = [dict(acc) for acc in account]
    
    return result