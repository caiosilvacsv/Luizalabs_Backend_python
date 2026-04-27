
from pydantic import AwareDatetime, NaiveDatetime
from src.banco.schemas.orm import ORMBaseModel, BaseModel, Field


class AddressBase(BaseModel):
  postal_code: str = Field(..., max_length = 20)
  address_line_1: str = Field(..., max_length = 150)
  address_line_2: str = Field(..., max_length = 150)
  district: str = Field(..., max_length = 150)
  city: str = Field(..., max_length = 150)
  state: str = Field(..., max_length = 150)
  country: str = Field(..., max_length = 150)
  
class AddressIn(AddressBase):
  individual_id: int

class AddressOut(AddressBase, ORMBaseModel):
  id: int
  created_at: AwareDatetime | NaiveDatetime
  individual_id: int
 