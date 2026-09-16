def calcular_resultado(v1, v2):
    produto = v1 * v2
    if produto <= 1000:
        return produto
    else:
        return v1 + v2


res1 = calcular_resultado(20, 30)
res2 = calcular_resultado(50, 30)

print(f"Teste 1: {res1}")
print(f"Teste 2: {res2}")