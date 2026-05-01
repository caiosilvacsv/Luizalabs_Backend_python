
from decimal import Decimal
from databases.interfaces import Record
from sqlalchemy import update
from src.exceptions.business import AccountNotCreatedError, AccountNotFoundError, NotUpdatedError
from src.models.current_account import current_accounts
from src.models.account import accounts
from src.schemas.account import AccountIn, AccountOut
from src.database.connection import database

class AccountService:
    
  async def create(
    self, 
    account: AccountIn
  )-> AccountOut | None:
    new_account = accounts.insert().values(
      agency = account.agency,
      account_number = account.account_number,
      account_digit = account.account_digit,
      client_id = account.client_id
    )
    
    account = await database.execute(new_account)

    if not account:
      raise AccountNotCreatedError()    
    
    return await database.fetch_one(accounts.select().where(accounts.c.id == account))

  async def read_all(
    self,
    client_id : int,
    limit : int,
    skip : int = 0,
  ) -> list[Record] | None:
    
    query = (
        accounts.select()
        .where(
            accounts.c.is_active == True,
            accounts.c.client_id == client_id,
        )
        .limit(limit)
        .offset(skip)
    )
    account = await database.fetch_all(query)
    
    if not account:
      raise AccountNotFoundError(client_id)
    
    return account
      
  async def read_account_by_id(
    self,
    account_id: int
    ) -> Record | None:
    query = accounts.select().where(accounts.c.id == account_id)
    return await database.fetch_one(query)

  async def read_current_account_by_id(
    self,
    account_id: int
    ) -> Record | None:
    query = (
      current_accounts
      .select().
      where(
        current_accounts.c.account_id == account_id,
      )
    )
    return await database.fetch_one(query)

  async def read_current_account_limit(
    self,
    account_id: int
    ) -> Record | None:
    query = (
      current_accounts
      .select(
        current_accounts.c.daily_limit
      ).
      where(
        current_accounts.c.account_id == account_id,
      )
    )
    return await database.fetch_one(query)
  
  async def update_current_account_limit(
    self,
    account_id: int,
    daily_limit: Decimal
    ) -> Record | None:
    query = update().where(current_accounts.c.account_id == account_id).values(daily_limit = daily_limit)
    updated =  await database.execute(query)
    
    if updated == 0:
      raise NotUpdatedError("Not updated account : ", account_id)
    
    update_account = await self.read_current_account_by_id(account_id)
    
    if not update_account:
      raise AccountNotFoundError(account_id)
    
    return await self.read_current_account_by_id(account_id)

  async def read_current_account_balance(
    self,
    account_id: int
    ) -> Record | None:
    query = accounts.select(accounts.c.balance).where(accounts.c.id == account_id)
    return await database.fetch_one(query)
