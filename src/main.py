from contextlib   import asynccontextmanager

from fastapi      import FastAPI

from src.controllers  import post, auth
from src.database     import database, engine
from src.models.post  import metadata

# Gerencia os eventos de inicialização e encerramento da aplicação

@asynccontextmanager
async def lifespan(app: FastAPI):
    metadata.create_all(engine)
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)
app.include_router(post.router)
app.include_router(auth.router)