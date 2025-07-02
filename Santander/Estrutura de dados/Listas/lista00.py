frutas = ['maça', 'banana', 'laranja', 'uva', 'pera']

def separador():
    print('*' * 30)

# Exemplo de manipulação de listas em Python
print(frutas) # Imprime a lista completa
print(frutas[0], frutas[3]) # Imprime o primeiro e o quarto elemento
print(frutas[-1])  # Imprime o último elemento
print(frutas[1:4])  # Imprime do índice 1 ao 3
print(frutas[::-1])  # Imprime a lista ao contrário

separador()

# Adicionando elementos à lista
frutas.append('kiwi')  # Adiciona 'kiwi' ao final da lista
print(frutas)
frutas.insert(2, 'abacaxi')  # Insere 'abacaxi' na posição 2
print(frutas)
# Removendo elementos da lista
frutas.remove('banana')  # Remove 'banana' da lista
print(frutas)
frutas.pop()  # Remove o último elemento da lista
print(frutas)

separador()

lista = ['p', 'y', 't', 'h', 'o', 'n']

print(lista[2:])  # Imprime a sublista a partir do índice 2
print(lista[:2]) # Imprime a sublista até o índice 2
print(lista[1:4])  # Imprime a sublista do índice 1 ao 3
print(lista[0:3:2])  # Imprime a sublista do índice 0 ao 2, pulando de 2 em 2 # Imprime a lista completa
print(lista[::-1])  # Imprime a lista ao contrário

separador()

for i in lista:
    print(i) # Imprime cada elemento da lista em uma linha
    print(i, end=' ')  # Imprime cada elemento da lista na mesma linha, separado por espaço

separador()

for indice, valor in enumerate(lista):
    print(f'Índice: {indice}, Valor: {valor}')  # Imprime o índice e o valor de cada elemento da lista

separador()

numeros  = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]  # Lista de números pares
impares = [numero for numero in numeros if numero % 2 != 0]  # Lista de números ímpares
print(f'Números pares: {pares}')
print(f'Números ímpares: {impares}')

separador()

numeros  = [1, 30, 21, 2, 9, 65, 34]
pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)  # Adiciona o número à lista de pares se for par
    else:
        impares.append(numero)  # Adiciona o número à lista de ímpares se for ímpar
print(f'Números pares: {pares}')
print(f'Números ímpares: {impares}')
