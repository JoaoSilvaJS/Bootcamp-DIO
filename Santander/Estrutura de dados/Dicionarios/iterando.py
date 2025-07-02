contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '1234-5678'},
    'maria@gmail.com': {'nome': 'Maria', 'telefone': '9876-5432'},
    'marcia@gmail.com': {'nome': 'Márcia', 'telefone': '5555-5555'},
    'joao@gmail.com': {'nome': 'João', 'telefone': '2222-2222', 'extra': {'a':1}},
} # Dicionário de contatos

for chave in contatos:
    print(chave, contatos[chave])

print()
print()

# Iterando sobre chaves e valores
print('--- Iterando sobre chaves e valores ---')
print()
print()

for chave, valor in contatos.items():
    print(chave, valor)