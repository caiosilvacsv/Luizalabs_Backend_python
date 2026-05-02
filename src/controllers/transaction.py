
from decimal import Decimal
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from src.core.security import login_required, get_current_user
from src.schemas.statement import StatementIn
from src.service.transaction import TransactionService
from src.service.account import AccountService

router = APIRouter(
  prefix = "/transaction",
  tags = ["transaction"],
  dependencies = [Depends(
   login_required 
  )]
)

t_service = TransactionService() 
account_service = AccountService()

@router.post("/create")
async def create_transaction(
  statement:StatementIn, 
  current_user: Annotated[dict, Depends(get_current_user)],
  source_account : int = None,
  destination_account : int = None
):
  client_id = int(current_user["user_id"])
  
  # Busca a conta para a qual a transação foi solicitada
  account = await account_service.read_account_by_id(statement.account_id)
  
  # Confere se a conta existe e se ela pertence à pessoa que está logada
  if not account or account["client_id"] != client_id:
    raise HTTPException(
      status_code=status.HTTP_403_FORBIDDEN,
      detail="Você não tem permissão para movimentar esta conta."
    )

  return await t_service.create_transaction(
    statement,
    source_account,
    destination_account
  )
  
@router.get("/daily-limit/{account_id}")
async def daily_limit(account_id : int) -> Decimal:
  return await t_service.daily_limit(account_id)
