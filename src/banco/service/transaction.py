
from datetime import date
from decimal import Decimal
from databases.interfaces import Record
from sqlalchemy import select, func, cast, Date

from src.banco.models.current_account import current_accounts
from src.banco.models.account import accounts
from src.banco.models.statement import statements
from src.banco.database.connection import database
from src.banco.schemas.statement import StatementIn, TypeTransaction
from src.banco.exceptions.business import (
  InsufficientBalance, 
  AccountNotFoundError,
  DailyLimitExceeded
)

class TransactionService:
  
  @database.transaction()
  async def create_transaction(
    self,
    statement: StatementIn,
    source_account : int = None, 
    destination_account : int = None
  ) -> Record:
    balance : Decimal
    
    account = self.__find_account(statement.account_id)
    
    if statement.type_transaction == TypeTransaction.WITHDRAWAL : 
      balance = await self.__withdrawal(statement, account)
      
    if statement.type_transaction == TypeTransaction.DEPOSIT :
      balance = self.__deposit(statement, account)
    
    if statement.type_transaction == TypeTransaction.TRANSFER :
      return await self.__transfer(
        statement, 
        source_account, 
        destination_account
      )
      
    #Create new transaction
    transaction_id = await self.__register_transaction(statement)
    
    #update account balance
    await self.__update_account_balance(statement.account_id, balance)
    
    query = statements.select().where(statements.c.id == transaction_id)
    return await database.fetch_one(query)
    
  async def __withdrawal(self, statement:StatementIn, account) -> Decimal:
    if account['balance'] < statement.amount:
      raise InsufficientBalance(account['id'])
    
    limit_available: Decimal = await self.daily_limit(account['id'])
  
    if limit_available < statement.amount:
      raise DailyLimitExceeded(account['id'])
    
    return account["balance"] - statement.amount
    
  def __deposit(self, statement:StatementIn, account) -> Decimal:
    return account["balance"] + statement.amount

  @database.transaction()
  async def __transfer(
    self,
    statement:StatementIn, 
    source_account, 
    destination_account
  ) -> dict:
    # 1. Cria uma cópia do schema alterando apenas a operação para SAQUE (WITHDRAWAL)
    withdrawal_statement = statement.model_copy(
      update={
        "type_transaction": TypeTransaction.WITHDRAWAL,
        "account_id": source_account,
        "description": str(destination_account['id'])
      }
    )
    
    # 2. Usa a própria instância para acessar o método e aguarda (await) sua execução
    withdrawal_record = await self.create_transaction(withdrawal_statement)
    
    #3. Cria uma cópia do schema alterando apenas a operação para DEPOSITO (DEPOSIT)
    deposit_statement = statement.model_copy(
      update={
        "type_transaction": TypeTransaction.DEPOSIT,
        "account_id": destination_account,
        "description": str(source_account['id'])
      }
    )
    
    # 4. Usa a própria instância para acessar o método e aguarda (await) sua execução
    deposit_record = await self.create_transaction(deposit_statement)
    return {
      "withdrawal": withdrawal_record,
      "deposit": deposit_record
    }

  async def daily_limit(self, account_id : int) -> Decimal:
    """
    Calcula o limite de saque diário restante para uma conta.
    1. Busca o limite diário total configurado para a conta.
    2. Busca a soma de todos os saques ('WITHDRAWAL') feitos hoje.
    3. Retorna a diferença.
    """
    # Primeiro, verifica se a conta corrente existe e pega o limite total
    limit_query = current_accounts.select().where(current_accounts.c.account_id == account_id)
    limit_record = await database.fetch_one(limit_query)

    if not limit_record:
      # Se não houver uma conta corrente associada, não há limite para calcular.
      raise AccountNotFoundError(account_id)
    
    total_limit = limit_record['daily_limit']

    # Segundo, calcula o total de saques realizados hoje
    today = date.today()
    withdrawals_query = (
        select(func.sum(statements.c.amount).label("total_withdrawn"))
        .where(
            statements.c.account_id == account_id,
            statements.c.type_transaction == 'WITHDRAWAL',
            cast(statements.c.created_at, Date) == today,
        )
    )
    
    withdrawals_record = await database.fetch_one(withdrawals_query)
    
    total_withdrawn = withdrawals_record['total_withdrawn'] or Decimal('0.00')

    # Terceiro, calcula e retorna o limite restante
    return total_limit - total_withdrawn

  async def read_account_with_statement(self, account_id: int) -> dict:
    # 1. Busca os detalhes da conta
    account = self.__find_account(account_id)
        
    # 2. Busca todas as transações (extrato) dessa conta
    statement_query = statements.select().where(statements.c.account_id == account_id)
    statement_records = await database.fetch_all(statement_query)
    
    # 3. Transforma o registro da conta em um dicionário mutável
    result = dict(account)
    
    # 4. Adiciona a lista de transações na chave "statement", 
    # exatamente como definido no schema AccountOutWithStatement
    result["statement"] = [dict(stmt) for stmt in statement_records]
    
    return result

  async def __register_transaction(
    self, 
    statement: StatementIn
  ) -> int : 
    command = statements.insert().values(
      amout = statement.amount,
      type_transaction = statement.type_transaction,
      description = statement.description,
      account_id = statement.account_id
    )
    return await database.execute(command)

  async def __update_account_balance(
    self, 
    account_id : int,
    balance : Decimal
  ):
    command = accounts.update().where(accounts.c.id == account_id).values(balance = balance)
    return await database.execute(command)
  
  async def __find_account(self, account_id : int) -> Record | None:
    account_query = (
      accounts.select()
      .where(
        accounts.c.id == account_id,
      )
    )
    account = await database.fetch_one(account_query)

    if not account:
      raise AccountNotFoundError(statements.account_id )
    return account
    