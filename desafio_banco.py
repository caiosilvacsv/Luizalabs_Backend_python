from abc import ABC, abstractmethod
from datetime import datetime
import textwrap



class Cliente:
  def __init__(self, endereco : str):
    self._endereco = endereco
    self._contas = []
  
  @property
  def endereco(self):
    return self._endereco
  
  @property
  def contas(self):
    return self._contas
  
  def realizar_transacao(self, conta: Conta, transacao: Transacao):
    transacao.registrar(conta)
  
  def adicionar_conta(self, conta: Conta):
    self._contas.append(conta)
    
class PessoaFisica(Cliente):
  def __init__(self, cpf : str, nome: str, data_nascimento: str, endereco: str):
    super().__init__(endereco)
    self._cpf = cpf
    self._nome = nome
    self._data_nascimento = data_nascimento
  
  @property
  def cpf(self):
    return self._cpf
  
  @property
  def nome(self):
    return self._nome
  
class PessoaJuridica(Cliente):
  def __init__(self, cnpj : str, razao_social: str, endereco: str):
    super().__init__(endereco)
    self._cnpj = cnpj
    self._razao_social = razao_social
    
  @property
  def cnpj(self):
    return self._cnpj
  
  @property
  def razao_social(self):
    return self._razao_social
  
class Conta:
  def __int__(self, numero: int, cliente: Cliente, agencia = "0001"):
    self._numero = numero
    self._agencia = agencia
    self._cliente = cliente
    self._saldo = 0.0
    self._historico = Historico()
    
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
  
  @classmethod
  def nova_conta(cls, cliente: Cliente, numero : int):
    return cls(numero, cliente)
  
  def saldo(self) -> float:
    return self._saldo
  
  def sacar(self, valor : float) -> bool:
    if self._saldo>= valor:
      self._saldo -= valor
      return True
    else: 
      return False
  
  def depositar(self, valor : float) -> bool:
    if valor > 0:
      self._saldo += valor
      return True
    return False
  
class ContaCorrente(Conta):
  def __init__(self, numero: int, cliente: Cliente, agencia = "0001", 
               limite = 500, limite_saque = 3):
    super().__init__(numero, cliente, agencia)
    self._limite = limite
    self._limite_saque = limite_saque
    
  @property
  def limite(self):
    return self._limite
  
  @property
  def limite_saque(self):
    return self._limite_saque
  
  def sacar(self, valor : float):
    numero_saques = len([transacao for transacao in self._historico.transacoes 
                         if transacao["tipo"] == Saque.__name__])
    
    limite_excedido = valor > self._limite
    saque_excedido = self._limite_saque <= numero_saques
    
    if limite_excedido or saque_excedido:
      return False
    else:
      return super().sacar(valor)
    
  def __str__(self):
    return f'''
      Titular: {self._cliente.nome}
      Conta: {self._numero}
      Agencia: {self._agencia}
      Saldo: {self._saldo}
    '''
    
class Historico:
  def __init__(self):
    self._transacoes = []
  
  @property
  def transacoes(self):
    return self._transacoes
  
  def adicionar_transacao(self, transacao : Transacao):
    self._transacoes.append({
      "tipo": transacao.__class__.__name__,
      "valor": transacao._valor,
      "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    })
    
class Transacao(ABC): 
  @property
  @abstractmethod
  def valor(self):
    pass
  
  @classmethod
  def registrar(cls, conta : Conta):
    pass
  
class Saque(Transacao):
  def __init__(self, valor : float):
    self._valor = valor
    
  @property
  def valor(self):
    return self._valor
  
  @classmethod
  def registrar(self, conta : Conta):
    if conta.sacar(self._valor):
      conta.historico.adicionar_transacao(self)
      
class Deposito(Transacao):
  def __init__(self, valor : float):
    self._valor = valor
    
  def valor(self):
    return self._valor
  
  def registrar(self, conta : Conta):
    if conta.depositar(self._valor):
      conta.historico.adicionar_transacao(self)
      

def busca_cliente_conta(clientes : list) -> tuple[PessoaFisica, Conta, str]:
  cpf = input("Informe o CPF: ")

  cliente = filtrar_cliente(cpf, clientes)

  if not cliente:
    print("\n@@@ Cliente nao encontrado. @@@")
    return None, None, cpf
  
  conta = recuperar_conta(cliente)
  
  if not conta:
    return cliente, None, cpf
  
  return cliente, conta, cpf

def transacao(func, clientes : list) -> bool:
  cliente, conta, _ = busca_cliente_conta(clientes)
  
  if cliente is None: 
    return False
  if conta is None: 
    return False
  
  transacao = func(float(input(f"Informe o valor do {func.__name__.lower()}: ")))
  cliente.realizar_transacao(conta, transacao)
  return True
  
def depositar(clientes : list):
  
  resposta = transacao(Deposito, clientes)
  
  if resposta:
    print("\nDeposito realizado com sucesso!")
  else:
    print("\n@@@ Operacao de deposito falhou! @@@")

def sacar(clientes : list):
  resposta = transacao(Saque, clientes)
  
  if resposta:
    print("\nSaque realizado com sucesso!")
  else:
    print("\n@@@ Operacao de saque falhou! @@@")

def exibir_extrato(clientes : list):
  cliente, conta, _ = busca_cliente_conta(clientes)
  
  if cliente is None: 
    return None 
  if conta is None: 
    return None
  
  extrato = ""
  transacoes = conta.historico.transacoes
  
  print("\n======= Extrato =======")
  
  if not transacoes:
    extrato = "Nao foram realizadas movimentacoes."
  else : 
    print("\nData\t\t\tTipo\t\tValor")

    for transacao in conta.historico.transacoes:
      extrato += f"\n{transacao['data']}\t\t{transacao['tipo']}\t\t{transacao['valor']}"
  
  print(extrato)
  print(f"\n Saldo: {conta.saldo:.2f}")  
  print("\n=======================")   

def filtrar_cliente(cpf : str, clientes : list) -> list[PessoaFisica]:
  return [cliente for cliente in clientes if cliente.cpf == cpf]

# FIXME : AttributeError: 'NoneType' object has no attribute 'contas'
def recuperar_conta(clientes : list):
  cliente, _, _ = busca_cliente_conta(clientes)
  if cliente is None:
    return None
  if not cliente.contas:
    
    return None
  else:
    print("\n==== Contas do cliente ====")
    for index, conta in cliente.contas:
      print(f"[{index}] : {conta}")
      
    conta = int(input("Informe o numero da conta: "))
    return cliente.contas[conta]

def criar_cliente(clientes : list):
  cliente, _, cpf= busca_cliente_conta(clientes)
  
  if cliente:
    print("\n@@@ Ja existe um cliente com esse CPF! @@@") 
    return None
  
  nome = input("Informe o nome do cliente: ")
  data_nascimento = input("Informe a data de nascimento do cliente: ")
  endereco = input("Informe o endereco do cliente: ")
  
  cliente = PessoaFisica(cpf, nome, data_nascimento, endereco)
  clientes.append(cliente)
  
  print("\n@@@ Cliente criado com sucesso! @@@")
    
def criar_conta( clientes : list, contas : list):
  cliente, _, _ = busca_cliente_conta(clientes)
  
  if cliente is None : 
    print("\n@@@ Fluxo encerrado! @@@")
    return
  
  nova_conta = ContaCorrente.nova_conta(cliente, len(cliente.contas) + 1)
  contas.append(nova_conta)
  cliente.adicionar_conta(nova_conta)
  
  print("\n=== Conta criada com sucesso! ===")

def listar_contas(contas : list):
  for conta in contas:
    print("_" * 30)
    print(textwrap.dedent(str(conta)))


def menu():
  menu = """\n
  [1]\tDepositar
  [2]\tSacar
  [3]\tExtrato
  [4]\tNova conta
  [5]\tListar contas
  [6]\tNovo usuário
  [0]\tSair
  => """
  return input(textwrap.dedent(menu))
  
def main():
  clientes = []
  contas = []
  
  while True:
    opcao = menu()
    
    if opcao == "1":
      depositar(clientes)
    elif opcao == "2":
      sacar(clientes)
    elif opcao == "3":
      exibir_extrato(clientes)
    elif opcao == "4":
      criar_conta(clientes, contas)
    elif opcao == "5":
      listar_contas(contas)
    elif opcao == "6":
      criar_cliente(clientes)
    elif opcao == "0":
      break

main()

