
from contextlib import asynccontextmanager
from fastapi    import FastAPI, Request, status
from fastapi.responses import JSONResponse

from src.banco.database.connection import database
from src.banco.exceptions.base import BankExceptionBase
from src.banco.controllers import account, auth, client, transaction 

@asynccontextmanager
async def lifespan(app: FastAPI):
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