class Cachorro:
  def __init__(self, nome, cor, raca, idade, peso, acordado = True):
    self.nome       = nome
    self.cor        = cor
    self.raca       = raca
    self.idade      = idade
    self.peso       = peso
    self.acordado   = acordado
  
  def latir(self):
    print("Au au")
    
  def __del__ (self):
    print("Removendo a instância da classe")
    print(f"{self.nome} morreu")
    

def criando_cachorro():
  c = Cachorro("Rex", "preto", "vira lata", 2, 20)
  print(c.nome)
    
c = Cachorro("Rex", "preto", "vira lata", 2, 20)
c.latir()
#del c
