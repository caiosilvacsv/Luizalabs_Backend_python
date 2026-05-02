
from .base import BankExceptionBase, status

class AccountNotFoundError(BankExceptionBase):
  def __init__(
    self,
    account_id: int = None, 
    message : str = "Account not found",
    status_code : int = status.HTTP_404_NOT_FOUND,
  ):
    self.account_id = account_id
    super().__init__(message + f" {account_id or ''}", status_code)
    
class AccountNotCreatedError(BankExceptionBase):
  def __init__(
    self,
    message : str = "Account not created",
    status_code : int = status.HTTP_400_BAD_REQUEST,
  ):
    super().__init__(message, status_code)

class ClientNotCreatedError(BankExceptionBase):
  def __init__(
    self,
    message : str = "Client not created",
    status_code : int = status.HTTP_400_BAD_REQUEST,
  ):
    super().__init__(message, status_code)
      
class ClientNotFoundError(BankExceptionBase):
  def __init__(
    self,
    client_id: int, 
    message : str = "Client not found",
    status_code : status = status.HTTP_400_BAD_REQUEST,
  ):
    self.client_id = client_id
    super().__init__(message + f" {client_id}", status_code)
    
class NotUpdatedError(BankExceptionBase):
  def __init__(
    self,
    client_id: int, 
    message : str = "Not updated ",
    status_code : int = status.HTTP_404_NOT_FOUND,
  ):
    self.client_id = client_id
    super().__init__(message + f" {client_id}", status_code)
    
class InsufficientBalance(BankExceptionBase):
  def __init__(
    self,
    account_id: int, 
    message : str = "Insufficient balance",
    status_code : int = status.HTTP_422_UNPROCESSABLE_CONTENT,
  ):
    self.account_id = account_id
    super().__init__(message + f" {account_id}", status_code)

class DailyLimitExceeded(BankExceptionBase):
  def __init__(
    self,
    account_id: int, 
    message : str = "Daily limit exceeded",
    status_code : int = status.HTTP_422_UNPROCESSABLE_CONTENT,
  ):
    self.account_id = account_id
    super().__init__(message + f" {account_id}", status_code)
    
class AccountNumberExists(BankExceptionBase):
  def __init__(
    self, 
    message : str = "Account number already exists",
    status_code : int = status.HTTP_422_UNPROCESSABLE_CONTENT,
  ):
    super().__init__(message, status_code)