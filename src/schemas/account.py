#Schema para a criação de uma conta
from pydantic import AwareDatetime, BaseModel, Field, NaiveDatetime
from decimal import Decimal
from typing import List
from src.schemas.orm import ORMBaseModel
from src.schemas.statement import StatementOut


class AccountBase(BaseModel):
  agency : int 
  balance : Decimal = Field(default=Decimal('0.00'), max_digits = 10, decimal_places = 2)
  is_active : bool = True
  account_number : int
  account_digit : int
  
class AccountIn(AccountBase):
  client_id : int

class AccountUpdate(AccountBase):
  agency : int | None = None
  balance : Decimal | None = None

class AccountOut(ORMBaseModel, AccountBase):
  id : int
  client_id : int
  created_at : AwareDatetime | NaiveDatetime
  is_active : bool
  
class AccountOutWithStatement(AccountOut):
  statement : List[StatementOut] = []