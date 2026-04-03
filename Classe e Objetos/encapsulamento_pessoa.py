class Pessoa: 
  def __init__(self, nome, ano_nascimento):
    self.nome = nome
    self._ano_nascimento = ano_nascimento
    
  @property
  def idade(self):
    import datetime
    ano_atual = datetime.date.today().year
    return ano_atual - self._ano_nascimento
  
pessoa = Pessoa("Teste", 2000)
print(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}")