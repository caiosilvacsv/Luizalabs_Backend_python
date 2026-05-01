
from decimal import Decimal

from fastapi import APIRouter, Depends
from src.core.security import login_required
from src.schemas.statement import StatementIn
from src.service.transaction import TransactionService

router = APIRouter(
  prefix = "/transaction",
  tags = ["transaction"],
  dependencies = [Depends(
   login_required 
  )]
)

t_service = TransactionService() 

@router.post("/create")
async def create_transaction(
  statement:StatementIn, 
  source_account : int = None,
  destination_account : int = None
):
  return await t_service.create_transaction(
    statement,
    source_account,
    destination_account
  )
  
@router.get("/daily-limit/{account_id}")
async def daily_limit(account_id : int) -> Decimal:
  return await t_service.daily_limit(account_id)
