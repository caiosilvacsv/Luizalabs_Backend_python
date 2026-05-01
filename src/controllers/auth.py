from fastapi import APIRouter

from src.core.security import sign_jwt
from src.schemas.auth import LoginIn, LoginOut


router = APIRouter(
  prefix = "/auth",
  tags = ["auth"]
)

@router.post("/login", response_model = LoginOut)
async def login(data : LoginIn) -> LoginOut:
  return sign_jwt(user_id = data.user_id)