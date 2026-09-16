uso_cpu = []

print("Digite o uso do processador (%) em 15 periodos consecutivos:")
for i in range(1, 16):
    valor = float(input(f"Periodo {i}: "))
    uso_cpu.append(valor)

maior_uso = max(uso_cpu)
print(f"\nO maior valor de uso de CPU observado foi: {maior_uso}%")