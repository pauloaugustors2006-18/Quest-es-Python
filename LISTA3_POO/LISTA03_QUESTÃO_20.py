medicoes_memoria = []

print("Digite a memoria utilizada nos 5 testes (MB/GB):")
for i in range(1, 6):
    valor = float(input(f"Teste {i}: "))
    medicoes_memoria.append(valor)

soma_total = sum(medicoes_memoria)

print(f"\nMedições registradas: {medicoes_memoria}")
print(f"Soma total da memória utilizada: {soma_total}")