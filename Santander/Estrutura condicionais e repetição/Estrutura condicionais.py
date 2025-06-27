print('#' * 38)
print('#' * 38)

saldo = 2000
saque = float(input('Informe o valor do saque: R$'))

if saldo >= saque:
    print('Contando cédulas... \nSaque realizado com sucesso!')

else:
    print('Saldo insufucuente!')

print('#' * 38)
print('#' * 10, 'Exemplo com ELIF', '#' * 10)
print('#' * 38)

opcao = int(input('Informe uma opção:\n[1] Sacar \n[2] Extrato\n'))
if opcao == 1:
    valor = float(input('Informe o valor do saque: '))

elif opcao == 2:
    print('Exibindo o extrato...')

else:
    print('Opção inválida')

print('#' * 38)
print('#' * 38)

print('#' * 38)
print('#' * 10, 'Exemplo com IF', '#' * 10)
print('#' * 38)

maior_idade = 18
idade = int(input('Informe sua idade: '))

if idade >= 18:
    print('Maior idade, pode tirar a CNH')
else:
    print('Ainda não pode tirar a CNH')

print('#' * 38)
print('#' * 10, 'Exemplo com IF ternário', '#' * 10)
print('#' * 38)

saldo = 2000
saque = 50

status = 'Sucesso' if saldo >= saque else 'Falha'

print(f'{status} ao realizar o saque!')