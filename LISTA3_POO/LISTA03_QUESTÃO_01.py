anterior = 0

for ciclo in range(10):
    num_anterior = 0 if ciclo == 0 else ciclo - 1
    soma = ciclo + num_anterior
    print(f"Ciclo Atual: {ciclo} | Ciclo Anterior: {num_anterior} | Soma: {soma}")