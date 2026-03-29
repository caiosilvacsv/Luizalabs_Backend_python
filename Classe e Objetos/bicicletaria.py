"""_summary_
Desafio:
  João tem uma bicicletaria e gostaria de registrar as vendas de
  suas bicicletas. Crie um programa onde João informe: cor,
  modelo, ano e valor da bicicleta vendida. Uma bicicleta pode:
  buzinar, parar e correr. Adicione esses comportamentos!
"""


class Bicicleta:
  """_summary_
    Representa uma bicicleta.
    
    Atributos:
      cor: str
      modelo: str
      ano: int
      valor: float 
  """
  def __init__(self, cor, modelo, ano, valor):
    self.cor    = cor 
    self.modelo = modelo 
    self.ano    = ano 
    self.valor  = valor
    
  def buzinar(self):
    return "plim plim"

  def parar(self):
    return "Parando a bicicleta\nBicicleta parada"
  
  def correr(self):
    return "Vrummm..."
  
  # def __str__(self):
  #   return f"Cor: {self.cor}\nModelo: {self.modelo}\nAno: {self.ano}\nValor: {self.valor}"
  
  def __str__(self):
    return f"{self.__class__.__name__}:\n{'\n'.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"



b1 = Bicicleta("Roxa", "Monark", 2000, 1000)

# print(b1.buzinar())
# print(b1.correr())
# print(b1.parar())
# print()
# print(b1.cor)
# print(b1.modelo)
# print(b1.ano)
# print(b1.valor)
print(b1)

b2 = Bicicleta("Azul", "Caloi", 2010, 2000)

# Bicicleta.buzinar(b2) # b2.buzinar()

# print(b2.buzinar())
# print(b2.correr())
# print(b2.parar())
# print()
# print(b2.cor)
# print(b2.modelo)
# print(b2.ano)
# print(b2.valor)
print(b2)