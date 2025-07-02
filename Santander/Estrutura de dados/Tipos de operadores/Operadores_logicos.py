print('''
Operador:
AND: todas as condiçoes precisam ser verdadeiro para ser verdadeiro
OR: Apenas uma condição precisa ser verdadeiro para ser verdadeiro
NOT: Se a condição for verdade o resuldado é falso e se for verdade o resultado é falso
''')

saldo = 1000
saque = 200
limite = 100

saldo >= saque

saque <= limite

print('AND: saldo >= saque and saque <= limite = ', saldo >= saque and saque <= limite)
print('OR: saldo >= saque or saque <= limite = ', saldo >= saque or saque <= limite)

contatos_emergencia = []

print('NOT: not 1000 > 1500 = ', not 1000 > 1500)
print('NOT: contatos_emergencia = ', contatos_emergencia) # lista vazia é falso
print('NOT: not "saque 1500 = "', not "saque 1500;") # sting com valor é verdadeiro
print('NOT: not "" = ', not "") # string sem valor é falso

print()
print('#' * 30)
print()

print('verdade e verdade = verdade', True and True)
print('verdade e falso = falso', True and False)
print('falso e falso = falso ', False and False)
print('verdade ou verdade = verdade ', True or True)
print('verdade ou falso = verdade', True or False)
print('falso ou falso = falso ', False or False)

saldo = 1000
saque = 250
lmite = 200
conta_especial = True

exp = (saldo>= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp)