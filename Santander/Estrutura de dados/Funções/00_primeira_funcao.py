def mensagem():
    print('Olá mundo!')

def mensagem2(nome):
    print(f'Seja bem vindo {nome}!')

def mensagem3(nome = 'Anônimo'):
    print(f'Seja bem vindo {nome}')

mensagem()
mensagem2(nome='Eu')
mensagem3()
mensagem3(nome='Eu de novo')