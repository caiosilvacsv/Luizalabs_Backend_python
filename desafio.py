# código do desafio presente na video aula

from abc import ABC, abstractmethod
from datetime import datetime
import textwrap

class Cliente:
  def __init__(self, endereco):
    self.endereco = endereco
    self.contas = []
    
  def realiza_transacao(self, conta, transacao):
    transacao.registrar(conta)
 
  def adiciona_conta(self, conta):
    self.contas.append(conta)
    
class PessoaFisica(Cliente):
  def __init__(self,nome, data_nascimento, cpf, endereco):
    super().__init__(endereco)
    self.cpf = cpf
    self.nome = nome
    self.data_nascimento = data_nascimento

class Conta:
  def __init__(self, cliente, numero):
    self._saldo = 0.0
    self._numero = numero
    self._agencia = "0001"
    self._cliente = cliente
    self._historico = Historico()

  @classmethod
  def nova_conta(cls, cliente, numero):
    return cls(cliente, numero)
  
  @property
  def saldo(self):
    return self._saldo
  
  @property
  def numero(self):
    return self._numero
  
  @property
  def agencia(self):
    return self._agencia
  
  @property
  def cliente(self):
    return self._cliente
  
  @property
  def historico(self):
    return self._historico
  
  def sacar(self, valor):
    saldo = self._saldo
    excedeu_saldo =  valor > saldo

    if excedeu_saldo :
      print("@@@ Operação falhou! Você não tem saldo o suficiente. @@@")

    elif valor > 0:
      self._saldo -= valor
      print("\n=== Saque realizado com sucesso! ===")
      return True
    
    else: 
      print("@@@ Operação falhou! O valor informado é inválido. @@@")

    return False 
    
  def depositar(self, valor):
    if valor > 0: 
      self._saldo += valor
      print("\n=== Depósito realizado com sucesso! ===")
    else: 
      print("@@@ Operação falhou! O valor informado é inválido. @@@")
      return False
    
    return True

class ContaCorrente(Conta):
  def __init__(self, cliente, numero, limite = 500.00 , saques = 3):
    super().__init__(cliente, numero)
    self.limite = limite
    self.limite_saques = saques

  def sacar(self, valor):
    numero_saques = len([transacao for transacao in self.historico.transacoes 
                         if transacao["tipo"] == Saque.__name__])
    
    excedeu_limite = valor > self.limite
    excedeu_saques = numero_saques >= self.limite_saques

    if excedeu_limite:
      print("\n@@@ Operacao falhou! O valor do saque excede o limite.@@@")
    
    elif excedeu_saques:
      print("\n@@@ Operacao falhou! Numero maximo de saques excedido.@@@")
    
    else:
      return super().sacar(valor)
    
    return False

  def __str__(self):
    return f"""\
      Nome: \t {self.cliente.nome}
      Agencia: \t{self.agencia}
      C/C: \t{self.numero}
    """
      
class Historico:
  def __init__(self):
    self._transacoes = []

  @property
  def transacoes(self):
    return self._transacoes

  def adicionar_transacao(self, transacao):
    self._transacoes.append(
      {
        "tipo": transacao.__class__.__name__,
        "valor": transacao.valor,
        "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"), 
      }
    )
  
class Transacao(ABC):
  @property
  @abstractmethod
  def valor(self):
    pass

  @classmethod
  def registrar(cls, conta):
    pass

class Deposito(Transacao):
  def __init__(self, valor):
    self._valor = valor

  @property
  def valor(self):
    return self._valor
  
  def registrar(self, conta):
    sucesso_transacao = conta.depositar(self._valor)

    if sucesso_transacao:
      conta.historico.adicionar_transacao(self)

class Saque(Transacao):
  def __init__(self, valor):
    self._valor = valor

  @property
  def valor(self):
    return self._valor

  def registrar(self, conta):
    sucesso_transacao = conta.sacar(self._valor)

    if sucesso_transacao:
      conta.historico.adicionar_transacao(self)

def menu():
  menu = """\n
  =========================
  [d]\tDepositar
  [s]\tSacar
  [e]\tExtrato
  [nc]\tNova Conta
  [lc]\tListar Contas
  [nu]\tNovo Usuário
  [q]\tSair

  => """
  return input(textwrap.dedent(menu))

def depositar(clientes):
  cpf = input("Informe o CPF do cliente: ")

  cliente = filtrar_cliente(cpf, clientes)

  if not cliente:
    print("\n@@@ Cliente nao encontrado. @@@")
    return
  
  valor = float(input("Informe o valor do deposito: "))
  
  transacao = Deposito(valor)

  conta = recuperar_conta_cliente(cliente)
  
  if not conta:
    return
  
  cliente.realiza_transacao(conta, transacao)
  print("\nDeposito realizado com sucesso!")

def sacar(clientes):
  cpf = input("Informe o CPF do cliente: ")

  cliente = filtrar_cliente(cpf, clientes)

  if not cliente:
    print("\nCliente nao encontrado")
    return
  
  valor = float(input("Informe o valor do saque: "))
   
  transacao = Saque(valor)

  conta = recuperar_conta_cliente(cliente)
  
  if not conta:
    return
  
  cliente.realiza_transacao(conta, transacao)
  print("\nSaque realizado com sucesso!")

def exibir_extrato(clientes):

  cpf = input("Informe o CPF do cliente: ")

  cliente = filtrar_cliente(cpf, clientes)

  if not cliente:
    print("\n @@@ Cliente não encontrado @@@")
    return
  
  conta = recuperar_conta_cliente(cliente)
  if not conta:
    return

  print("\n=============== Extrato ===============")
  transacoes = conta.historico.transacoes
  extrato = ""
  if not transacoes:
    extrato = "Não foram realizadas movimentacoes"
  else:
    print("Data\t\tTipo\t\tValor")

    for transacao in transacoes:
      extrato += f"{transacao['data']}\t{transacao['tipo']}\t{transacao['valor']}\n"
  
  print(extrato)
  print(f"\nSaldo : \n\t R$ {conta.saldo:.2f}")
  print("=======================================")

def criar_clientes(clientes):
  cpf = input("Informe o CPF (somente numeros): ")
  cliente = filtrar_cliente(cpf, clientes)

  if cliente:
    print("\n@@@ Já existe um cliente com esse CPF. @@@")
    return

  nome = input("Informe o nome completo: ")
  data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
  endereco = input("Informe o endereço: ")

  cliente = PessoaFisica(nome = nome, data_nascimento = data_nascimento, 
  cpf = cpf, endereco = endereco)
  
  clientes.append(cliente)

  print("\n Cliente criado com sucesso! ")

def filtrar_cliente(cpf, clientes):
  clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
  return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
  if not cliente.contas: 
    print("\n@@@@ Cliente nao possui contas. @@@@")
    return
  
  # FIXME : não permite escolher a conta
  return cliente.contas[0]

def criar_conta(numero_conta, clientes, contas):
  cpf = input("Informe o CPF do cliente: ")
  cliente = filtrar_cliente(cpf, clientes)

  if not cliente:
      print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
      return

  conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
  contas.append(conta)
  cliente.adiciona_conta(conta)

  print("\n=== Conta criada com sucesso! ===")

def listar_contas(contas):
  for conta in contas:
    print("-" * 100)
    print(textwrap.dedent(str(conta)))

def main():
  clientes = []
  contas = []

  while True:
    opcao = menu()

    if opcao == "d":
      depositar(clientes)

    elif opcao == "s":
      sacar(clientes)

    elif opcao == "e":
      exibir_extrato(clientes)

    elif opcao == "nu":
      criar_clientes(clientes)

    elif opcao == "nc":
      criar_conta(len(contas) + 1,clientes, contas)

    elif opcao == "lc":
      listar_contas(contas)

    elif opcao == "q":
      break

main()