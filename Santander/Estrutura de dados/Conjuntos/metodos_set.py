conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.union(conjunto_b)  # União dos conjuntos A e B
print(conjunto_a) # {1, 2}

conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.update(conjunto_b)  # Atualiza o conjunto A com os elementos do conjunto B
print(conjunto_a) # {1, 2, 3, 4}

conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.intersection(conjunto_b)  # Interseção dos conjuntos A e B
print(conjunto_a) # {1, 2, 3, 4}

conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.difference(conjunto_b)  # Diferença dos conjuntos A e B
print(conjunto_a) # {1, 2}

conjunto_b.difference(conjunto_a)  # Diferença dos conjuntos B e A
print(conjunto_b) # {3, 4}

conjunto_a.symmetric_difference(conjunto_b)  # Diferença simétrica dos conjuntos A e B
print(conjunto_a) # {1, 2, 3, 4}