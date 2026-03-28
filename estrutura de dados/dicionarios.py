'''
Conjunto não ordenados de pares chaves e valores;
chave imutavel e unico;
valor mutavel;
dicionario = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3'}
'''
def dicionario_exemplo():
  pessoa = {
    "nome": "teste", 
    "sobrenome": "test", 
    "idade": 20, 
    "altura": 1.80, 
    "altura": 1.80
    }
  pessoa = dict(
    nome = "teste", 
    sobrenome = "test", 
    idade = 20, 
    altura = 1.80
  )
  pessoa["telefone"] = "999999999"

  print(pessoa) # {'nome': 'teste', 'sobrenome': 'test', 'idade': 20, 'altura': 1.8, 'telefone': '999999999'}
  print(pessoa["telefone"]) # 999999999
  pessoa["nome"] = "Teste" # {'nome': 'Teste', 'sobrenome': 'test', 'idade': 20, 'altura': 1.8, 'telefone': '999999999'}

def dict_aninhados():
  contatos = {
    "email01@gmail.com": {"nome": "Teste", "telefone": "99999999"},
    "email02@gmail.com": {"nome": "Teste", "telefone": "11111111"},
  }
  
  print(contatos["email02@gmail.com"]["telefone"])

def interacao():
  contatos = {
    "email01@gmail.com": {"nome": "Teste", "telefone": "99999999"},
    "email02@gmail.com": {"nome": "Teste", "telefone": "11111111"},
  }
  
  for chave in contatos:
    print(chave, contatos[chave])
  
  for chave, valor in contatos.items():
    print(contatos, valor)
    
#Metodos
def clear_exemplo():
  contatos = {
    "email01@gmail.com": {"nome": "Teste", "telefone": "99999999"},
    "email02@gmail.com": {"nome": "Teste", "telefone": "11111111"},
  }
  
  print(contatos) # {'email01@gmail.com': {'nome': 'Teste', 'telefone': '99999999'}, 'email02@gmail.com': {'nome': 'Teste', 'telefone': '11111111'}}
  
  contatos.clear()
  print(contatos) # {}

def copy_exemplo():
  contatos= {
    "email01@gmail.com": {"nome": "teste", "telefone": "99999999"},
  }
  
  copia = contatos.copy()
  copia["email02@gmail.com"] = {"nome": "Test"}
  print(contatos)
  print(copia)
  
def fromkeys_exemplo():
  #Caso não haja dicionario existente o fromkeys cria um
  dict.fromkeys(["nome", "telefone"]) # {'nome': None, 'telefone': None}
  dict.fromkeys(["nome", "telefone"], "vazio") # {'nome': "vazio", 'telefone': "vazio"}
  #Se houver um dicionario, subtitua o dict pelo nome de tal.
  
def get_exemplo():
  contatos = {
    "email01@gmail.com": {"nome": "Teste", "telefone": "99999999"},
  }

  ##contato["chave inexistente"]              # KeyError
  print(contatos.get("chave inexistente"))    #None
  print(contatos.get("chave inexistente",{})) #{}
  print(contatos.get("email01@gmail.com"),{}) #{'nome': 'Teste', 'telefone': '99999999'}

def items_exemplo():
  contatos = {
    "email01@gmail.com": {"nome": "Teste", "telefone": "99999999"},
  }
  
  print(contatos.items())
  
  for chave, valor in contatos.items():
    print(chave, valor)

def keys_exemplo():
  contatos = {
    "email01@gmail.com": {"nome": "Teste", "telefone": "99999999"},
  }
  
  print(contatos.keys()) # dict_keys(['email01@gmail.com'])
  
  for chave in contatos.keys():
    print(chave) # email01@gmail.com
  
def pop_exemplo():
  contatos = {
    "email01@gmail.com": {"nome": "Teste", "telefone": "99999999"},
  }
  
  print(contatos.pop("email01@gmail.com")) # {'nome': 'Teste', 'telefone': '99999999'}
  print(contatos.pop("email01@gmail.com")) # KeyError : 'email01@gmail.com'
  #Segundo argumento é o que retorna caso não encontre
  print(contatos.pop("email01@gmail.com", {})) # {}
  print(contatos) # {}
  
def popitem_exemplo():
  contatos = {
    "email01@gmail.com": {"nome": "Teste", "telefone": "99999999"},
  }
  
  #Retira os itens em sequencia
  print(contatos.popitem()) # ('email01@gmail.com', {'nome': 'Teste', 'telefone': '99999999'})
  print(contatos) # {}

def setdefault_exemplo():
  contatos = {"nome": "Teste", "telefone": "99999999",}
  
  print(contatos.setdefault("nome", "Junior")) # {'nome': 'Teste', 'telefone': '99999999'}
  print(contatos.setdefault("idade", 20)) # {'nome': 'Teste', 'telefone': '99999999', 'idade' : 20}

def update_exemplo():
  contatos = {
    "email01@gmail.com": {"nome": "Teste", "telefone": "99999999"},
  }
  
  contatos.update({"email01@gmail.com": {"telefone": "11111111"}})
  print(contatos)
  
  contatos.update({"email02@gmail.com": {"nome":" Testinho", "telefone": "22222222"}})
  print(contatos)
  
def values_exemplo():
  contatos = {
    "email01@gmail.com": {"nome": "Teste", "telefone": "99999999"},
    "email02@gmail.com": {"nome": "teste", "telefone": "11111111"},
    "email03@gmail.com": {"nome": "testinho", "telefone": "22222222"},
  }
  
  print(contatos.values())

def in_exemplo():
  contatos = {
    "email01@gmail.com": {"nome": "Teste", "telefone": "99999999"},
    "email02@gmail.com": {"nome": "teste", "telefone": "11111111"},
    "email03@gmail.com": {"nome": "testinho", "telefone": "22222222"},
  }
  
  print("email01@gmail.com" in contatos) # True
  print("teste@gmail.com" in contatos) # False
  print("idade" in contatos["email01@gmail.com"]) # False
  print("telefone" in contatos["email01@gmail.com"]) # True
  
def del_exemplo():
  contatos = {
    "email01@gmail.com": {"nome": "Teste", "telefone": "99999999"},
    "email02@gmail.com": {"nome": "teste", "telefone": "11111111"},
    "email03@gmail.com": {"nome": "testinho", "telefone": "22222222"},
  }
  
  del contatos["email01@gmail.com"]
  print(contatos)
  
  del contatos["email01@gmail.com"]["telefone"]
  print(contatos)