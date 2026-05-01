
from pydantic import BaseModel, Field
from src.schemas.orm import ORMBaseModel


class PhoneIn(BaseModel):
  ddi: str = Field(..., max_length = 3)
  ddd: str = Field(..., max_length = 3)
  number : str = Field(..., max_length = 9)
  individual_id: int
  
class PhoneOut(ORMBaseModel, PhoneIn):
  id: int