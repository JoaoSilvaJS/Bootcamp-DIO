lanche = ('hambúrguer', 'suco', 'pizza', 'pudim')

print('#' * 30)
print('Estrutura simples apenas quando os nomes das tuplas são necessários')
print()

for comida in lanche:
    print(f'Vou comer {comida}')
print('Comi demais!')

print('#' * 30)
print('Estrutura mais composta quando os nomes e posição das tuplas são necessários')
print()

for cont in range(0, len(lanche)):
    print(f'Vou comer {lanche[cont]}') # Para mostrar apenas a quantidade retirar o [cont]

print('#' * 30)
print('Outra estrutura mais composta quando os nomes e posição das tuplas são necessários')
print()

for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer{comida} na posição {posicao}')

print('Comi demais!')
print('Quantidade de lanches:', len(lanche))