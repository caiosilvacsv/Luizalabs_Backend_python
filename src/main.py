
from contextlib import asynccontextmanager
import asyncpg
from fastapi    import FastAPI, Request, status
from fastapi.responses import JSONResponse

from src.database.connection import database, engine
from src.exceptions.base import BankExceptionBase
from src.controllers import transaction 
from src.controllers import account, auth, client
print("imports")

@asynccontextmanager
async def lifespan(app: FastAPI):
  print("connect database")
  await database.connect()
  yield
  print("disconnect database")
  await database.disconnect()


print("init app")
app = FastAPI(
  lifespan=lifespan
)

print("rotas")

app.include_router(account.router)
print("rota 01")
app.include_router(auth.router)
print("rota 02")
app.include_router(client.router)
print("rota 03")
app.include_router(transaction.router)
print("rota 04")

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
  
@app.exception_handler(asyncpg.exceptions.UniqueViolationError)
async def unique_violation_handler(
  request: Request, 
  exception: asyncpg.exceptions.UniqueViolationError
):
  return JSONResponse(
    status_code = status.HTTP_409_CONFLICT,
    content = {
      "error" : exception.__class__.__name__,
      "detail": "Ja existe um registro com o mesmo valor.",
      "error_db" : str(exception),
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
