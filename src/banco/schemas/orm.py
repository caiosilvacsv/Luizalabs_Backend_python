# Permite ler dados diretamente do banco (SQLAlchemy)
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class ORMBaseModel(BaseModel):
  """
    Todos os schemas de resposta que lerem dados do banco 
    devem herdar desta classe em vez do BaseModel padrão.
  """
  model_config = ConfigDict(
    # 1. Lê do SQLAlchemy (Obrigatório para ORM/Core)
    from_attributes=True,
    
    # 2. Transforma "account_id" no Python para "accountId" no JSON
    alias_generator=to_camel,
    populate_by_name=True, # Permite que você crie o objeto usando o nome em Python
    
    # 3. Limpa espaços extras no começo e no fim das strings
    str_strip_whitespace=True,
    
    # 4. (Opcional) Impede que o schema aceite propriedades que não existem nele
    extra='ignore'
  )
  