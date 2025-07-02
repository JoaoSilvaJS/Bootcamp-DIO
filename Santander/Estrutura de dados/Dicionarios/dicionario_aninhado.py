contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '1234-5678'},
    'maria@gmail.com': {'nome': 'Maria', 'telefone': '9876-5432'},
    'marcia@gmail.com': {'nome': 'Márcia', 'telefone': '5555-5555'},
    'joao@gmail.com': {'nome': 'João', 'telefone': '2222-2222', 'extra': {'a':1}},
} # Dicionário de contatos

telefone = contatos['maria@gmail.com']['telefone'] # Acessando o telefone de Maria
print(telefone)

extra = contatos['joao@gmail.com']['extra']['a'] #  Acessando o valor extra de João
print(extra)