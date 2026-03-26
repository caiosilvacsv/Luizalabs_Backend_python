def lista_exemplo():
  frutas = ["laranja", "maça", "uva"]
  frutas = []
  letras = list("python") # ['p', 'y', 't', 'h', 'o', 'n']
  numeros = list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  carro = ["Volkswagem", "golf", 38000, 2010, 120000, "Minas Gerais", True]

def indices():
  frutas = ["laranja", "maça", "uva"]
  frutas[0] # laranja
  frutas[2] # uva
  #indices negativos
  frutas[-1] #uva
  frutas[-3] #laranja

def aninhados():
  matriz = [
    [0,0,1],
    [0,2,0],
    [3,0,0]
  ]

  matriz[0]       #[0,0,1]
  matriz[0][2]    # 1
  matriz[0][-1]   #1
  matriz[-1][-3]  #3

def fatiamento():
  lista = ['p', 'y', 't', 'h', 'o', 'n']
  
  lista[2:]     # ['t', 'h', 'o', 'n']
  lista[:2]     # ['p', 'y']
  lista[1:3]    # ['y', 't']
  lista[0:3:2]  # ['p','t']
  lista[::]     # ['p', 'y', 't', 'h', 'o', 'n']
  lista[::-1]   # ['n', 'o', 'h', 't', 'y', 'p']


def interacao():
  carros = ["civic", "corolla", "cerato"]
  for carro in carros:
    print(carro)
  
  #enumerate
  for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

def filtro():
  numeros = [1, 30, 21, 2, 9, 65, 34]
  pares = [numero for numero in numeros if numero % 2 == 0]
  quadrado = [numero**2 for numero in numeros ]
  
  print(pares)
  print(quadrado)
  
def append_exemplo():
  lista = []

  lista.append(1)
  lista.append("Teste")
  lista.append([30,40,20])

  print(lista) # [1, "Teste", [30,40,20]]

def clear_exemplo():
  lista = [1, "Teste", [30,40,20]]
  print(lista) # [1, "Teste", [30,40,20]]

  lista.clear()
  print(lista) # []

def copy_exemplo():
  #o que é passado em uma variavel nao é copiado para original
  lista = [1, "Teste", [30,40,20]]
  print(id(lista)) # [1, "Teste", [30,40,20]]

  nova_lista = lista.copy()
  print(id(nova_lista)) # [1, "Teste", [30,40,20]]

def count_exemplo():
  numeros = [1, 30, 21, 2, 9, 65, 34]
  print(numeros.count(30)) # 1
  
def extend_exemplo():
  linguagens = ["python", "js", "java"]
  print(linguagens) # ['python', 'js', 'java']

  linguagens2 = ["java", "c", "c++", "c#"]
  print(linguagens2) # ['c', 'c++', 'c#']

  linguagens.extend(linguagens2)
  print(linguagens) # ['python', 'js', 'java', 'java', 'c', 'c++', 'c#']

def index_exemplo():
  numeros = [1, 30, 21, 2, 9, 65, 34, 30, 34]
  print(numeros.index(30)) # 1
  print(numeros.index(34)) # 6