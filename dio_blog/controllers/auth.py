
from fastapi      import APIRouter
from schemas.auth import LoginIn
from views.auth   import LoginOut
from security     import sing_jwt 

router = APIRouter(
    prefix = "/auth",
    tags= ['auth',],
  )

@router.post("/login", response_model = LoginOut)
async def login(data: LoginIn):
  return sing_jwt(user_id = data.user_id)

