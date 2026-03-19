#AND = para ser verdadeiro as duas precisam ser verdadeiras
#OR = para ser verdadeiro apenas uma precisa ser verdadeira
#NOT = inverte o valor

print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)
print(not True)
print(not False)
print(not not True)
print(10*"-")

#Exemplos
saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp_1 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp_1)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

conta_normal_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_saldo_suficiente or conta_especial_saldo_suficiente
print(exp_3)