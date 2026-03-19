#Metodos úteis para String
def MetodosUteis():
  nome = "tesTe aÍ"

  print(nome.upper())
  print(nome.lower())
  print(nome.title())

  texto = "   Olá Mundo     "

  print(texto)
  print(texto.strip())
  print(texto.lstrip())
  print(texto.rstrip())

  center = "teste"

  print(center.center(10))
  print(center.center(20, "-"))
  print("-".join(center.center((20-(len(center)*2)), "-")))

def Interpolacao():
  nome = "Teste"
  idade = 22
  saldo = 123.21
  profissao = "Desenvolvedor"
  linguagem = "Python"

  data = { "name": nome, "age": idade}

  print("Nome: %s Idade: %d" % (nome, idade))

  print("Nome: {} Idade: {}". format(nome, idade))
  print("Nome: {1} Idade: {0}". format(idade, nome))
  print("Nome: {1}, {1}, {1}, {1} Idade: {0}". format(idade, nome))
  print("Nome: {nome} Idade: {idade}". format(nome = nome, idade = idade))
  print("Nome: {name} Idade: {age}". format(age = idade, name = nome))
  print("Nome: {name} Idade: {age}". format(**data))

  print(f"Nome: {nome} Idade : {idade} Saldo : {saldo:1.2f}")


def Fatiamento():
  frase = "Estou testestando tudo"

  print(frase[0])
  print(frase[-2])
  print(frase[:9])
  print(frase[10:])
  print(frase[10:16])
  print(frase[10:16:2])
  print(frase[:])
  print(frase[::-1])

def Multilinha():
  nome = "teste"

  mensagem = f'''
     Olá, meu nome é {nome},
    Eu estou aprendendo python.
        E essa mensagem há diferentes recuos;
  '''

  print(mensagem)

  print(
    """
    ''''''''''''MENU'''''''''''''
    [1] - Sacar 
    [2] - Depositar
    [3] - Extrato
    '''''''''''''''''''''''''''''
    """
  )
Multilinha()


