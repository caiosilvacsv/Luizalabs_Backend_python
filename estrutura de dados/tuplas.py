#Tuplas

#Tupla não pode ser alterada

def tupla_exemplo():
  
  frutas = ("laranja", "maça", "uva",)

  letras = tuple("python") # ('p', 'y', 't', 'h', 'o', 'n')

  numeros = ([1,2,3], [4,5,6], [7,8,9])

  pais = ("Brasil",)

  print(frutas)
  print(frutas[0])
  print(letras)
  print(letras[-1])
  print(numeros)
  print(pais)

def aninhados():
  matriz = (
    (0,0,1),
    (0,2,0),
    (3,0,0)
  )

  matriz[0]       #(0,0,1)
  matriz[0][2]    # 1
  matriz[0][-1]   #1
  matriz[-1][-3]  #3
  
def fatiamento():
  lista = ('p', 'y', 't', 'h', 'o', 'n')
  
  lista[2:]     # ('t', 'h', 'o', 'n')
  lista[:2]     # ('p', 'y')
  lista[1:3]    # ('y', 't')
  lista[0:3:2]  # ('p','t')
  lista[::]     # ('p', 'y', 't', 'h', 'o', 'n')
  lista[::-1]   # ('n', 'o', 'h', 't', 'y', 'p')

def interacao():
  carros = ("civic", "corolla", "cerato")
  for carro in carros:
    print(carro)
  
  #enumerate
  for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
    
#Metodos
def count_exemplo():
  numeros = (1, 30, 21, 2, 9, 65, 34)
  print(numeros.count(30)) # 1
  print(numeros.count())

def index_exemplo():
  numeros = (1, 30, 21, 2, 9, 65, 34, 30, 34)
  print(numeros.index(30)) # 1
  print(numeros.index(34)) # 6

def len_exemplo():
  numeros = (1, 30, 21, 2, 9, 65, 34, 30, 34)
  print(len(numeros)) # 9
