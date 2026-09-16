num1 = int(input("Digite o primeiro codigo:\n "))
num2 = int(input("Digite o segundo codigo:\n "))

inicio = min(num1, num2)
fim = max(num1, num2)

print(f"\nIdentificadores no intervalo entre {inicio} e {fim}:")
for codigo in range(inicio, fim + 1):
    print(codigo, end=" ")