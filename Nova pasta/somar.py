def somar (a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f'O reultado da operação {a} + {b} é: {resultado}')

exibir_resultado(10, 10, somar)