
from datetime import datetime
from typing import List
from pydantic import AwareDatetime, BaseModel, Field, NaiveDatetime
from src.banco.schemas.orm import ORMBaseModel
from src.banco.schemas.account import AccountOut


class ClientBase(BaseModel):
  name: str = Field(..., max_length = 100)
  
class ClientIn(ClientBase):
  status: bool

class ClientUpdate(BaseModel):
  name: str | None = Field(None, max_length = 100)
  status: bool | None = None
  closed: datetime | None = None

class ClientOut(ORMBaseModel, ClientBase):
  id: int
  created_at: AwareDatetime | NaiveDatetime
  status: bool
  closed: datetime | None = None

class ClientOutWithAccounts(ClientOut):
  accounts: List[AccountOut] = []