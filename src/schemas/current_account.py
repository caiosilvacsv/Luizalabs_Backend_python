
from decimal import Decimal
from pydantic import BaseModel, Field
from src.schemas.orm import ORMBaseModel


class CurrentAccountIn(BaseModel):
  daily_limit: Decimal = Field(..., max_digits = 10, decimal_places = 2)
  daily_withdrawal: int
  account_id: int
  
class CurrentAccountOut(ORMBaseModel):
  id: int
  daily_limit: Decimal
  daily_withdrawal: int
  account_id: int