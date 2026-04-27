
from decimal import Decimal
from enum import Enum
from pydantic import AwareDatetime, BaseModel, Field, NaiveDatetime
from src.banco.schemas.orm import ORMBaseModel

class TypeTransaction(str, Enum):
  DEPOSIT = 'DEPOSIT'
  WITHDRAWAL = 'WITHDRAWAL'
  TRANSFER = 'TRANSFER'

class StatementBase(BaseModel):
  description: str = Field(..., max_length = 150)
  amount: Decimal = Field(..., max_digits = 10, decimal_places = 2)
  type_transaction: TypeTransaction
  
class StatementIn(StatementBase):
  #Necessario saber o id da conta
  account_id: int
  
  class Config:
    use_enum_values = True

class StatementOut(ORMBaseModel, StatementBase):
  id: int
  created_at: AwareDatetime | NaiveDatetime
  account_id: int
  
class Transfer(BaseModel):
  withdrawal: StatementOut
  deposit: StatementOut