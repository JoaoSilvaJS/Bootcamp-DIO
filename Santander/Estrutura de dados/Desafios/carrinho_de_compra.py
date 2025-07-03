# Lista para armazenar os produtos e preços
carrinho = []
total = 0.0

# Entrada do número de itens
n = int(input('Quantidade de items: ').strip())

# Loop para adicionar itens ao carrinho
for _ in range(n): # Lê o número de itens
    linha = input(' Informe o produto e o valor separado por espaço: ').strip() # Lê a linha de entrada
    
    # Encontra a última ocorrência de espaço para separar nome e preço
    posicao_espaco = linha.rfind(" ") # Encontra a posição do último espaço
    
    # Separa o nome do produto e o preço
    item = linha[:posicao_espaco] # Nome do produto
    preco = float(linha[posicao_espaco + 1:]) # Preço do produto
    
    # Adiciona ao carrinho
    carrinho.append((item, preco)) # Adiciona tupla (item, preco) ao carrinho
    total += preco # Atualiza o total

for item, preco in carrinho:
    print(f'{item}: R${preco:.2f}')

print(f'Total: R${total:.2f}')