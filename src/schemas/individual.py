
from datetime import date
from typing import List

from pydantic import AwareDatetime, BaseModel, Field, NaiveDatetime
from src.schemas.orm import ORMBaseModel
from src.schemas.address import AddressOut
from src.schemas.phone import PhoneOut
from src.schemas.email import EmailOut


class IndividualBase(BaseModel):
  cpf : str = Field(..., max_length = 11)
  date_of_birth : date

class IndividualIn(IndividualBase):
  client_id : int
  
class IndividualOut(ORMBaseModel, IndividualBase):
  id : int
  created_at : AwareDatetime | NaiveDatetime

class IndividualOutWithDetails(IndividualOut):
  addresses: List[AddressOut] = []
  phones: List[PhoneOut] = []
  emails: List[EmailOut] = []