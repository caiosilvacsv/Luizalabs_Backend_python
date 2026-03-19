VOGAIS = "AEIOU"

#Exemplo de for utilizando um interavel
def Interavel():
  texto = input("Digite um texto:")
  print(f"Texto informado: {texto}")

  for letra in texto:
    if letra.upper() in VOGAIS:
      print(letra, end=" ")
  else: 
    print()

#Exemplo de for utilizando a função built-in range
def Range():
  for numero in range(0, 51, 5):
    print(numero, end=" ")
  print()

#Exemplo de while
def While():
  opcao = 1
  while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))
    if opcao == 1: 
      print("Sacando...")
    elif opcao == 2:
      print("Emitindo extrato...")
    elif opcao == 0:
      print("Saindo...")
    else: 
      print("Opção inválida!")
  else: 
    print("Obrigado por utilizar nosso banco!")

#Exemplo de break dentro do while
def BreakWhile():
  while True:
    numero = int(input("Adivinhe para parar: "))
    
    if numero == 10:
      break
    elif numero % 2 == 0:
      print("É par!")
      continue

    print(f"Não é : {numero}")

#Exemplo de break dentro do for
def BreakFor():
  for numero in range(100):
    
    if numero % 2 == 0:
      continue
    elif numero == 81:
      break
    print(numero, end= " ")

Interavel()
Range()
While()
BreakWhile()
BreakFor()