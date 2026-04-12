  
from datetime import UTC, datetime
from pydantic import BaseModel

#Exemplo com Pydantic
class PostIn(BaseModel):
  title: str
  author: str
  published_at: datetime
  published: bool = False