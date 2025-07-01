linguagens = ['Python', 'js', 'c', 'Java', 'C++', 'C#']
print(linguagens)

linguagens.sort()  # Ordena a lista em ordem alfabética
print(linguagens)

linguagens.sort(reverse=True)  # Ordena a lista em ordem alfabética inversa
print(linguagens)

linguagens.sort(key=len)  # Ordena a lista pelo tamanho das strings
print(linguagens)

linguagens.sort(key=len, reverse=True)  # Ordena a lista pelo tamanho das strings em ordem decrescente
print(linguagens)