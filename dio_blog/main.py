from contextlib   import asynccontextmanager

from fastapi      import FastAPI

from controllers  import post
from database     import database, metadata, engine

# Gerencia os eventos de inicialização e encerramento da aplicação

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)
app.include_router(post.router)