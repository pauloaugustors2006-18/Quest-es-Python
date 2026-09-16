num = int(input("Digite um número inteiro não negativo: "))

if num < 0:
    print("O fatorial não é definido para números negativos.")
else:
    fatorial = 1
    for i in range(1, num + 1):
        fatorial *= i
    print(f"O fatorial de {num} ({num}!) é: {fatorial}")