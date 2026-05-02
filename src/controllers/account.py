
from decimal import Decimal
from typing import Annotated

from fastapi import APIRouter, Depends, status, Header, Body

from src.core.security import login_required, get_current_user
from src.schemas.account import AccountIn, AccountOut, AccountOutWithStatement
from src.service.account import AccountService
from src.service.transaction import TransactionService


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
  "/my-accounts",
  response_model = list[AccountOut],
  tags = ["account"]
)
async def read_all(  
  current_user: Annotated[dict, Depends(get_current_user)],
  limit : int,
  skip : int = 0
) -> list[AccountOut] | None:
  client_id = int(current_user["user_id"])
  return await account_service.read_all(client_id, limit, skip)  

@router.get(
  "/read",
  response_model = AccountOut,
  tags = ["account"]
)
async def read_account_by_id(
 account_id: Annotated[
    int, 
    Header(embed=True, description="ID da conta no corpo da requisição")
  ]
) -> AccountOut | None:
  return await account_service.read_account_by_id(account_id)

#FIXME : Nao esta funcionando a conta corrente
@router.get(
  "/current-account/{account_id}",
  response_model = AccountOut,
  tags = ["account", "fix"]
)
async def read_current_account_by_id(account_id : int) -> AccountOut | None:
  return await account_service.read_current_account_by_id(account_id)

@router.get(
  "/daily-limit/{account_id}",
  tags = ["account", "fix"]
)
async def daily_limit(account_id : int) -> Decimal:
  return await account_service.read_current_account_limit(account_id)

@router.patch(
  "/daily-limit/{account_id}",
  tags = ["account", "fix"]
)
async def update_daily_limit(account_id : int, daily_limit : Decimal) -> Decimal:
  return await account_service.update_current_account_limit(account_id, daily_limit)

@router.post(
  "/balance",
  tags = ["account"],
)
async def balance(
  account_id: Annotated[
    int, 
    Body(embed=True, description="ID da conta no corpo da requisição")
  ]
) -> Decimal:
  return await account_service.read_current_account_balance(account_id)

@router.get(
  "/account_statement", 
  response_model=AccountOutWithStatement,
  tags = ["account"],
  description = "Return a statement of the account"
  )
async def get_account_statement(
  account_id: Annotated[
    int, 
    Header(embed=True, description="ID da conta no corpo da requisição")
  ]
):
  return await t_service.read_account_with_statement(account_id)
