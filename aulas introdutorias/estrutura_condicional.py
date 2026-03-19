MAIOR_IDADE = 18
IDADE_ESPECIAL = MAIOR_IDADE-1

def Idade():
  idade = int(input("Digite a sua idade: "))

  if idade >= MAIOR_IDADE:
    print("Maior de idade pode tirar CNH")

  if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH")

  if idade >= MAIOR_IDADE:
    print("Maiode de idade pode tirar a CNH")
  else:
    print("Ainda não pode tirar a CNH")

  if idade >= IDADE_ESPECIAL:
    print("Pode executar as aulas")
  elif idade >= MAIOR_IDADE:
    print("Pode tirar CNH")
  else:
    print("Não pode tirar CNH")

def BancoAninhada():
  conta_normal= False
  conta_universitaria = False
  conta_especial = True

  saldo = 200
  saque = 250
  cheque_especial = 300


  if conta_normal:

    if saldo>=saque:
      print("Saque realizado com sucesso.")
    elif saldo <= (saldo+cheque_especial):
      print("Saque realizado com ajuda do cheque espeical")
    else: 
      print("Não foi possivel realizar o saque")

  elif conta_universitaria:
  
    if saldo >= saque:
      print("Saque realizado com sucesso")
    else:
      print("Saldo insuficiente")
  
  elif conta_especial:
    print("conta especial selecionada")

  else:
    print("Nenhuma conta foi selecionada")

def BancoTernaria():
  saque = 200
  saldo = 500

  status = "Sucesso" if saldo >= saque else "Falha"
  
  print(f"{status} ao realizar o saque")


while(opcao!=4):
  opcao = int(input(" 1 - verificador de idade;" 
  "\n 2 - Banco Aninhado;" 
  "\n 3 - Banco Ternaria;" 
  "\n 4 - Sair;"
  "\n\n Sua escolha: "))

  if opcao == 1:
    Idade()
  elif opcao == 2:
    BancoAninhada()
  elif opcao == 3:
    BancoTernaria()
  else:
    print("Opção inválida")