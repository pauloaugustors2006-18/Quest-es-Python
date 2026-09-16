numero = int(input("Digite um numero inteiro entre 1 e 10 para ver a tabuada: "))

print(f"\n--- TABUADA DO {numero} ---")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i:2d} = {resultado:2d}")