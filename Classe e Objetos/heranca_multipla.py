class Animal:
  def __init__(self, numero_patas):
    self.numero_patas = numero_patas

  def __str__(self):
    return f"{self.__class__.__name__}: \n\t{', '.join([f'{chave}: {valor}' 
              for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
  def __init__(self, cor_pelo, **kw):
    self.cor_pelo = cor_pelo
    super().__init__(**kw)


class Ave(Animal):
  def __init__(self, cor_bico, **kw):
    self.cor_bico = cor_bico
    super().__init__(**kw)

class Cachorro(Mamifero):
  pass

class Gato(Mamifero):
  pass

class Leao(Mamifero):
  pass

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, numero_patas):
      #MRO - Method Resolution Order - Ordem de resolução
      #print(self.__class__.__mro__)
      #Onitorrinco -> Mamifero -> Ave -> Animal
      super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, 
                         numero_patas=numero_patas)

#Se passar os kwargs para o construtor da classe mãe, 
# ele irá ignorar os kwargs da classe filha
gato = Gato(cor_pelo="Preto", numero_patas = 4)
print(gato)

#Se passar os argumentos para o construtor da classe mãe, 
# ele irá ignorar os argumentos da classe filha
ornitorrinco = Ornitorrinco("Amarelo", "Marrom", 4)
print(ornitorrinco)