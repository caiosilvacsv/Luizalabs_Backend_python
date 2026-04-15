from datetime import datetime
from pydantic import BaseModel

class PostOut(BaseModel):
  id:           int
  title:        str
  author:       str
  published_at: datetime | None = None
  published:    bool

  