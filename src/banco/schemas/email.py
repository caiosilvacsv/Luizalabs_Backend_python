
from pydantic import BaseModel, Field
from src.banco.schemas.orm import ORMBaseModel


class EmailIn(BaseModel):
  email: str = Field(..., max_length = 150)
  individual_id: int

class EmailOut(ORMBaseModel):
  id: int
  email: str
  individual_id: int