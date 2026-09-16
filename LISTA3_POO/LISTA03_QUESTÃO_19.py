uso_cpu = []

print("Digite os 7 valores de utilização da CPU:")
for i in range(1, 8):
    valor = int(input(f"Registro {i}: "))
    uso_cpu.append(valor)

print("\nValores na ordem inversa de registro:")
print(uso_cpu[::-1])