from datetime import datetime, timedelta, timezone
from typing import Annotated
import jwt
from uuid import uuid4
from pydantic import BaseModel
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPBearer
from src.banco.core.config import settings

SECRET = settings.SECRET
ALGORITHM = settings.ALGORITHM

# Modelo de dados que representa as informações contidas dentro do Token (Claims)
class AccessToken(BaseModel):
  iss: str
  sub: int
  aud: str
  exp: float
  iat: float
  nbf: float
  jti: str

# Modelo de resposta do Token JWT
class JWTToken(BaseModel):
  access_token: AccessToken
  
# Função responsável por gerar (assinar) o token JWT
def sign_jwt(user_id: int) -> JWTToken:
  # Pegamos a data atual em UTC para emitir o token e definir quando começa a ser válido
  now = datetime.now(timezone.utc)
  # Definimos a expiração para 30 minutos no futuro
  expires = now + timedelta(minutes = 30)
  
  payload = {
    "iss" : "banco.com",
    "sub" : str(user_id),
    "aud" : "desafio_banco",
    "exp" : expires, # validade final
    "iat" : now,     # emitido em
    "nbf" : now,     # não usar antes de
    "jti" : uuid4().hex     
  } 
  
  token = jwt.encode(payload, SECRET, algorithm = ALGORITHM)
  return {
    "access_token": token
  }
  
# Função assíncrona responsável por decodificar e validar o token JWT
async def decode_jwt (token:str) -> JWTToken | None: 
  try:
    decoded_token = jwt.decode(token, SECRET, audience="desafio_banco",algorithms = [ALGORITHM])
    _token = JWTToken.model_validate({"access_token": decoded_token})
    # Valida manualmente a data de expiração (comparando o float do JWT com o timestamp local)
    return _token if _token.access_token.exp >= datetime.now(timezone.utc).timestamp() else None
  except Exception:
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
    # Tenta extrair o token do cabeçalho de autorização da requisição
    authorization = request.headers.get("Authorization", "")
    scheme, _, credentials = authorization.partition(" ")
    
    if credentials:
      # Verifica se o tipo de autenticação é Bearer
      if not scheme == "Bearer":
        raise HTTPException(
          status_code = status.HTTP_401_UNAUTHORIZED,
          detail = "Invalid authenticated scheme",
        )
      
      # Realiza a decodificação do Token
      payload = await decode_jwt(credentials)
      
      if not payload: 
        raise HTTPException(
          status_code = status.HTTP_401_UNAUTHORIZED,
          detail = "Invalid or expired token",
        )
      return payload
    
    else:
      # Retorna erro caso o token seja omitido
      raise HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Invalid authorization code",
      )
  
# Dependência para injeção do usuário atual baseado no token enviado
async def get_current_user(
  token: Annotated[ JWTToken, Depends(JWTBearer())]
) -> dict[str, int]:
  return {"user_id": token.access_token.sub}

# Dependência que verifica e obriga o usuário a estar validado para acessar um endpoint
def login_required(current_user : Annotated[dict[str, int], Depends(get_current_user)]):
  if not current_user:
    raise HTTPException(
      status_code= status.HTTP_403_FORBIDDEN,
      detail= "Access denied",
    )