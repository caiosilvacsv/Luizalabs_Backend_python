from database import database
from databases.interfaces import Record
from fastapi import HTTPException, status
from models.post import posts
from schemas.post import PostIn, PostUpdateIn

class PostService:
  # Busca todos os posts
  async def real_all(
    self, 
    published : bool,
    limit : int,
    skip : int = 0
  ) -> list[Record]:
    """Busca todos os post existentes

    Args:
        published (bool): Se está publicado
        limit (int): Limite de posts por pagina
        skip (int, optional): Quantidade de posts a serem pulados. Defaults to 0.

    Returns:
        list[Record]: Post
    """
    query = posts.select().where(posts.c.published == published).limit(limit).offset(skip)
    return await database.fetch_all(query)
  
  # Cria um novo post
  async def create(
    self,
    post : PostIn
  ) -> int:
    """Cria um post

    Args:
        post (PostIn): Post

    raises:
        HTTPException: Post already exists
        HTTPException: Error internal server
    
    Returns:
        int: _id do post criado
    """
    try:
      command = posts.insert(). values(
        title = post.title,
        content = post.content,
        published_at = post.published_at,
        published = post.published,
      )
      
      return await database.execute(command)
    except Exception as e:
      # Verifica se o erro é de restrição de unicidade do SQLite
      if "UNIQUE constraint failed" in str(e):
        raise HTTPException(
          status_code = status.HTTP_400_BAD_REQUEST,
          detail = "Post already exists",
        )
      # Caso seja outro erro, lança o erro original
      raise HTTPException(
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail = "Error internal server",
      )
  # Busca um post pelo id
  async def read(
    self,
    id: int 
  ) -> Record:
    """Busca um post pelo id

    Args:
        id (int): _id do post

    Raises:
        HTTPException: Post not found - 404

    Returns:
        Record: Post
    """
        
    
    return await self.__get_by_id(id)
  
  # Atualiza um post
  async def update(
    self, 
    id: int,
    post: PostUpdateIn
  ) -> Record:
    """Updade de um post

    Args:
        id (int): _id do post 
        post (PostUpdateIn): Post

    Raises:
        HTTPException: post não encontrado - 404

    Returns:
        Record: Post
    """
    total = await self.count(id)
    if not total:
      raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Post not found",
      )
    try:  
      data = post.model_dump(exclude_unset = True)
      command = posts.update().where(posts.c.id == id).values(**data)
      await database.execute(command)
    
      return await self.__get_by_id(id)
    except Exception as e:
      # Verifica se o erro é de restrição de unicidade do SQLite
      if "UNIQUE constraint failed" in str(e):
        raise HTTPException(
          status_code = status.HTTP_400_BAD_REQUEST,
          detail = "Post already exists",
        )
      # Caso seja outro erro, lança o erro original
      raise HTTPException(
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail = "Error internal server",
      )
  
  # Deleta um post
  async def delete(
    self, 
    id: int
  ) -> None:
    """ Deleta um post

    Args:
        id (int): _id do post
    """
    command = posts.delete().where(posts.c.id == id)
    await database.execute(command)
  
  # Busca um post pelo id e verifica se ele existe
  async def __get_by_id(
    self,
    id: int
  ) -> Record:
    """Busca um post pelo id

    Args:
        id (int): _id do post

    Raises:
        HTTPException: Post not found 404

    Returns:
        Record: Post
    """
    query = posts.select().where(posts.c.id == id)
    post = await database.fetch_one(query)
    if not post:
      raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Post not found",
        )
    return post
  
  # Conta quantos posts existem com o certo id
  async def count(
    self, 
    id: int
  ) -> int:
    """ Numero de posts existentes

    Args:
        id (int): id do post que está buscando

    Returns:
        int: Numero total de posts encontrados com o certo id 
    """
    query = "SELECT COUNT(id) AS total FROM posts WHERE id = :id"
    result = await database.fetch_one(query, {"id": id})
    return result.total
