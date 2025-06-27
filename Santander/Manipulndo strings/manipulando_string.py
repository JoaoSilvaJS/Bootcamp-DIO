curso = '    pYtHoN  '

print(curso.upper().strip()) #Tudo maiúsculo

print(curso.title()) #Primeira letra maiúculo

print(curso.lower()) #Tudo minúsculo

print(curso.strip()) #Tira os espaços

print(curso.lstrip()) #Tira os espaços da esquerda

print(curso.rstrip()) #Tira os espaços da direita
print()

print('''
########################################
### Junção e centralização de string ###
########################################
''')
curso = 'Python'

print(curso.center(10, '#')) # Não é necessário informar o '#'

print('.'.join(curso))