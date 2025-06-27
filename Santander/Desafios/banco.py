saldo = 0
limite = 500
extrato = ''
numero_saques = 0
limite_saque = 3

print('''
============== MENU ==============
==================================

 1. Depositar
 2. Sacar
 3. Extrato
 0. Sair  

==================================
==================================
''')

def menu():
    print('==================================')

while True:

    operacao = float(input('Informe a operação desejada: '))
    if operacao == 1:

        deposito = float(input('Informe o valor do depósito: R$ '))
        
        if deposito > 0:
            saldo += deposito
            extrato += f'Depósito: R$ {saldo:.2f}\n'
            
        else:
            print('Inválido! O valor não pode ser igual a 0 ou menor!')
            break

    elif operacao == 2:

        valor = float(input('Informe o valor do saque: R$ '))

        excedeu_saldo = valor > saldo 
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saque

        if excedeu_saldo:
            print('Saldo insuficiente!')
        
        elif excedeu_limite:
            print('Você excedeu o limite de saque!')
            
        elif excedeu_saques:
            print('Você excedeu o limite diário de saques!')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque : R$ {valor:.2f}\n'
            numero_saques += 1
            
        else:
            print('O valor informado é inválido!')

    elif operacao == 3:
        menu()
        print('EXTRATO')
        menu()
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'Saldo atual: {saldo:.2f}')
        menu()

    elif operacao == 0:
        menu()
        print('Obrigado por ser nosso cliente!!!')
        menu()
        break

    else:
        print('Opção inválida')