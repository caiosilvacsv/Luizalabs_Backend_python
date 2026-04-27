
from src.banco.exceptions.business import AccountNotFoundError, ClientNotCreatedError, ClientNotFoundError
from src.banco.schemas.client import ClientIn, ClientUpdate
from src.banco.models.client import clients
from src.banco.models.account import accounts
from src.banco.database.connection import database, sa

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
    
    if not client or client.rowcount == 0:
      raise ClientNotCreatedError()
    
    return client
  
  async def update_client(
    self, 
    client_id : int,
    client : ClientUpdate,
  ):
    
    update = clients.update().where(clients.c.id == client_id).values(
      name = client.name,
      status = client.status,
    )
    
    client = await database.execute(update)
    
    if not client or client.rowcount == 0:
      raise ClientNotFoundError()
    
    return client
  
  async def delete_client(self, client_id : int):
    delete = clients.update().where(clients.c.id == client_id).values(
      status = False,
      closed = sa.func.now(),
    )
    await database.execute(delete)
  
  async def read_client(self, client_id : int):
    read = clients.select().where(clients.c.id == client_id)
    return await database.fetch_one(read)
    
  async def read_client_with_account(
    self,
    client_id : int,
  ):
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