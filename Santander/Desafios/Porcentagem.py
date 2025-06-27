# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input('Insira o valor do produto: R$ ').strip())
cupom = input('Insira o cupom de desconto: ').strip()

if cupom == 'DESCONTO10':
    preco_final = preco - (preco * 10/100)
    print(f'{preco_final:.2f}')

elif cupom == "DESCONTO20":
    preco_final = preco - (preco * 20/100)
    print(f'{preco_final:.2f}')

elif cupom == "SEM_DESCONTO":
    print('SEM_DESCONTO')
else:
    print('Cupom inválido!')