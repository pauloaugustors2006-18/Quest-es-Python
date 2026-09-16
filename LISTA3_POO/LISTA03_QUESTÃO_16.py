limite1 = int(input("Digite o primeiro limite do intervalo: "))
limite2 = int(input("Digite o segundo limite do intervalo: "))

inicio = min(limite1, limite2)
fim = max(limite1, limite2)

multiplos_de_7 = 0

for codigo in range(inicio, fim + 1):
    if codigo % 7 == 0:
        multiplos_de_7 += 1

print(f"\nNo intervalo de {inicio} a {fim}, existem {multiplos_de_7} códigos múltiplos de 7.")