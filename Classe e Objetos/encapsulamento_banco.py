class Conta: 
  def __init__(self, numero_agencia, saldo = 0):
    self._saldo = saldo
    self.numero_agencia = numero_agencia
    
  def depositar(self, valor):
    self._saldo += valor
    
  def sacar(self, valor):
    self._saldo -= valor
    
  def mostrar_saldo(self):
    return self._saldo
  
  
conta = Conta("0001", 1000)
conta.depositar(3)
print(conta.numero_agencia)
print(conta.mostrar_saldo())
conta.sacar(25)
print(conta.mostrar_saldo())
    