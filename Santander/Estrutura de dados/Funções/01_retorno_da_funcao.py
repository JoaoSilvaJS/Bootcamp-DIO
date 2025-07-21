def calcular_total(numeros):
    return sum(numeros)

def sucessor_e_antecessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print(calcular_total([10, 20, 34]))
print(sucessor_e_antecessor(10))