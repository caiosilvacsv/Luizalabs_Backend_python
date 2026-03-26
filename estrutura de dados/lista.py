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

def pop_exemplo():
  linguagens = ["python", "js", "java", "c", "c++", "c#"]
  print(linguagens) # ['python', 'js', 'java', 'c', 'c++', 'c#']

  linguagens.pop() #remove o ultimo item | c#
  linguagens.pop() #remove o penultimo item | c++
  linguagens.pop(0) #remove o primeiro item | python

  print(linguagens) # ['js', 'java', 'c']

def remove_exemplo():
  linguagens = ["python", "js", "java", "java", "c", "c++", "c#"]
  print(linguagens) # ['python', 'js', 'java', 'java', 'c', 'c++', 'c#']

  linguagens.remove("java") #remove a primeira ocorrencia do  item | java
  print(linguagens) # ['python', 'js', 'java', 'c', 'c++', 'c#']


def reverse_exemplo():
  linguagens = ["python", "js", "java", "java", "c", "c++", "c#"]
  print(linguagens) # ['python', 'js', 'java', 'java', 'c', 'c++', 'c#']
  
  linguagens.reverse()
  print(linguagens) # ['c#', 'c++', 'c', 'java', 'java', 'js', 'python']

  #dá pra ser feito com o slice (fatiamento)
  print(linguagens[::-1]) # ['python', 'js', 'java', 'java', 'c', 'c++', 'c#']

def sort_exemplo():
  linguagens = ["python", "js", "java", "java", "c", "c++", "c#"]

  linguagens.sort() #ordena a lista por ordem alfabetica
  print(linguagens) # ['c', 'c++', 'c#', 'java', 'java', 'js', 'python']

  linguagens.sort(reverse=True) # ordena a lista por ordem alfabetica invertida
  print(linguagens) # ['python', 'js', 'java', 'java', 'c#', 'c++', 'c']

  linguagens.sort(key=lambda x: len(x)) #ordena a lista por tamanho da palavra
  print(linguagens) # ['c', 'js', 'c#', 'c++', 'java', 'java', 'python']
  
  linguagens.sort(key=lambda x: len(x), reverse=True) #ordena a lista por tamanho da palavra invertida
  print(linguagens) # ['python', 'java', 'java', 'c++', 'c#', 'js', 'c']

def len_exemplo():
  linguagens = ["python", "js", "java", "java", "c", "c++", "c#"]

  print(len(linguagens)) # 7

def sorted_exemplo():
  linguagens = ["python", "js", "java", "java", "c", "c++", "c#"]

  print(sorted(linguagens, key=lambda x: len(x))) # ['c', 'js', 'c#', 'c++', 'java', 'java', 'python']
  print(sorted(linguagens, key=lambda x: len(x), reverse=True)) # ['python', 'java', 'java', 'c++', 'js', 'c#', 'c']
  print(sorted(linguagens))  # ['c', 'js', 'c#', 'c++', 'java', 'java', 'python']