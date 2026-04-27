
from decimal import Decimal

from fastapi import APIRouter, Depends, status

from src.banco.core.security import login_required
from src.banco.schemas.account import AccountIn, AccountOut, AccountOutWithStatement
from src.banco.service.account import AccountService
from src.banco.service.transaction import TransactionService


router = APIRouter(
  prefix = "/account",
  tags = ["account"],
  dependencies = [Depends(
   login_required 
  )]
)

account_service = AccountService()
t_service = TransactionService()

@router.post(
  "/create-account",
  response_model = AccountOut,
  status_code = status.HTTP_201_CREATED,
  tags = ["account"]
)
async def create_account(account: AccountIn) -> int:
  return await account_service.create(account)

@router.get(
  "/{client_id}",
  response_model = list[AccountOut],
  tags = ["account"]
)
async def read_all(  
  client_id : int,
  limit : int,
  skip : int = 0
) -> list[AccountOut] | None:
  return await account_service.read_all(client_id, limit, skip)

@router.get(
  "/{account_id}",
  response_model = AccountOut,
  tags = ["account"]
)
async def read_account_by_id(account_id : int) -> AccountOut | None:
  return await account_service.read_account_by_id(account_id)

@router.get(
  "/current-account/{account_id}",
  response_model = AccountOut,
  tags = ["account"]
)
async def read_current_account_by_id(account_id : int) -> AccountOut | None:
  return await account_service.read_current_account_by_id(account_id)

@router.get(
  "/daily-limit/{account_id}",
  tags = ["account"]
)
async def daily_limit(account_id : int) -> Decimal:
  return await account_service.read_current_account_limit(account_id)

@router.patch(
  "/daily-limit/{account_id}",
  tags = ["account"]
)
async def update_daily_limit(account_id : int, daily_limit : Decimal) -> Decimal:
  return await account_service.update_current_account_limit(account_id, daily_limit)

@router.get(
  "/balance/{account_id}",
  tags = ["account"],
)
async def balance(account_id : int) -> Decimal:
  return await account_service.read_current_account_balance(account_id)

@router.get("/{account_id}/statement", response_model=AccountOutWithStatement)
async def get_account_statement(account_id: int):
    # Chama a função do seu service que busca a conta e as transações
    account_data = await t_service.read_account_with_statement(account_id)
    return account_data
  