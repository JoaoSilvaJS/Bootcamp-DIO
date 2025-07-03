eventos = {}

quantidade = int(input('Quantidade de participantes: '))

# Crie um loop para armazenar participantes e seus temas:
for _ in range(quantidade):
    linha = input().strip()  # Lê a linha de entrada
    nome, tema = linha.split(",")  # Divide a linha em nome e tema

    # Adiciona o participante ao grupo correspondente
    if tema not in eventos:
        eventos[tema] = []  # Cria uma nova lista para o tema, se não existir
    eventos[tema].append(nome)  # Adiciona o nome à lista de participantes do tema


# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")