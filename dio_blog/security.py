import logging
import time
import jwt

from uuid     import uuid4
from fastapi  import Depends, HTTPException, status, Request
from typing   import Annotated
from pydantic import BaseModel

from fastapi.security import HTTPBearer

logger = logging.getLogger("uvicorn.info")
logger.setLevel(logging.INFO)

SECRET = "4f7866158064bebbaca5d77c32ebb9ce0d8a7b60a06d03c9b2967551f2ac1d4f"
ALGORITHM = "HS256"

# Exemplo de token
class AccessToken(BaseModel):
  iss: str
  sub: int
  aud: str
  exp: float
  iat: float
  nbf: float
  jti: str

class JWTToken(BaseModel):
  access_token: AccessToken

def sing_jwt(user_id: int) -> JWTToken:
  now = time.time()
  payload = {
    "iss" : "curso-fastapi.com.br",
    "sub" : str(user_id),
    "aud" : "curso-fastapi",
    "exp" : now + (60 * 30), # duração de 30 minutos
    "iat" : now,
    "nbf" : now,
    "jti" : uuid4().hex     
  } 
  
  token = jwt.encode(payload, SECRET, algorithm = ALGORITHM)
  return {"access_token": token}

#decodifica o token
async def decote_jwt(token: str) -> JWTToken | None:
  try: 
    decoded_token = jwt.decode(token, SECRET, audience = "curso-fastapi", algorithms = [ALGORITHM])
    _token = JWTToken.model_validate({"access_token": decoded_token})
    return _token if _token.access_token.exp >= time.time() else None
  except Exception as e:
    logger.error(e)
    return None
  
  

#JWTBearer - Tratativa do HTTPBearer | Boas praticas na tratativa dos erros
class JWTBearer(HTTPBearer):
  """JWTBearer

  Args:
      HTTPBearer (_type_): Tratativa do HTTPBearer
  """
  def __init__(self, auto_error: bool = True):
    super(JWTBearer, self).__init__(auto_error = auto_error)
  
  #Boas praticas na tratativa do token 
  async def __call__(self, request: Request) -> JWTToken:
    """__call__

    Args:
        request (_type_): request http

    Raises:
        HTTPException: autenticação invalida
        HTTPException: token expirado
        HTTPException: codigo de autenticação invalido

    Returns:
        _type_: payload
    """
    authorization = request.headers.get("Authorization", "")
    scheme, _, credentials = authorization.partition(" ")
    if credentials:
      if not scheme == "Bearer":
        raise HTTPException(
          status_code = status.HTTP_401_UNAUTHORIZED,
          detail = "Invalid authenticated scheme",
        )
      payload = await decote_jwt(credentials)
      
      if not payload: 
        raise HTTPException(
          status_code = status.HTTP_401_UNAUTHORIZED,
          detail = "Invalid or expired token",
        )
      return payload
    
    else:
      raise HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Invalid authorization code",
      )
  

async def get_current_user(token: Annotated[ JWTToken, Depends(JWTBearer())]) -> dict[str, int]:
  return {"user_id": token.access_token.sub}

def login_required(current_user: Annotated[dict[str, int], Depends(get_current_user)]):
  if not current_user:
    raise HTTPException(status_code = status.HTTP_403_FORBIDDEN ,detail="Access denied")