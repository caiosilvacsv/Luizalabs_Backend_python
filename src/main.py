
from contextlib import asynccontextmanager
from fastapi    import FastAPI, Request, status
from fastapi.responses import JSONResponse

from src.database.connection import database, engine
from src.exceptions.base import BankExceptionBase
from src.controllers import transaction 
from src.controllers import account, auth, client
from src.models import (
  client as clients,
  account as accounts,
  address,
  current_account,
  email,
  individual, 
  phone , 
  statement
)

@asynccontextmanager
async def lifespan(app: FastAPI):
  await create_tables()
  await database.connect()
  yield
  await database.disconnect()


app = FastAPI(
  lifespan=lifespan
)

app.include_router(account.router)
app.include_router(auth.router)
app.include_router(client.router)
app.include_router(transaction.router)

@app.exception_handler(BankExceptionBase)
async def bank_exception_handler(
  request: Request, 
  exception: BankExceptionBase
):
  return JSONResponse(
    status_code = exception.status_code,
    content = {
      "error" : exception.__class__.__name__,
      "detail": exception.message,
      "instance" : request.url.path
    } 
  )

@app.exception_handler(Exception)
async def global_exception_handler(
  request: Request, 
  exception: Exception
):
  return JSONResponse(
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
    content = {
      "error" : exception.__class__.__name__,
      "detail": "Um erro inesperado aconteceu no servidor.",
      "instance" : request.url.path
    } 
  )
  
async def create_tables():
  clients.metadata.create_all(engine)
  accounts.metadata.create_all(engine)
  address.metadata.create_all(engine)
  current_account.metadata.create_all(engine)
  email.metadata.create_all(engine)
  individual.metadata.create_all(engine)
  phone.metadata.create_all(engine)
  statement.metadata.create_all(engine)
  clients.clients.metadata.create_all(engine)