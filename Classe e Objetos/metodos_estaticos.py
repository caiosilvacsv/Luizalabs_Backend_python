class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  @classmethod
  def criar_de_data_nascimento(cls, ano, mes, dia, nome):
    idade = 2026 - ano
    return cls(nome, idade)

  @staticmethod
  def e_maior_idade(idade):
    return idade >= 18

p = Pessoa.criar_de_data_nascimento(2000, 1, 1, "Teste")
print(p.nome, p.idade)

print(Pessoa.maioridade(18))
print(Pessoa.maioridade(8))