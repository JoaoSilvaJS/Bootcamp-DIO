# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
# por extenso, de zero até vinte.

# Seu programa deverá ler um número pelo teclado (entre 0 e 20)
# e mostrálo por extenso.

tupla = ('Zero', 'Um','Dois', 'Três', 'Quatro', 'Cinco','Seis', 'Sete', 'Oito', 'Nove', 'Dez',
         'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

# for numero in range(len(tupla)):
#     print(numero)

while True:
    resultado = int(input('Digite um valor de 0 a 20: '))
    if resultado <= 20:
        break
    print('Valor inválido! tente outra vez...')
  
print(f'Você digitou o número: {tupla[resultado]}')