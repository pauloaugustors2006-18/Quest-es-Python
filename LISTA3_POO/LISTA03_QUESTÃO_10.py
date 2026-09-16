latencias = []

print("Digite as 10 medicoes de latencia (ms):")
for i in range(1, 11):
    valor = float(input(f"Medicao {i}: "))
    latencias.append(valor)

menor_latencia = min(latencias)
print(f"\nA menor latencia registrada foi: {menor_latencia} ms")