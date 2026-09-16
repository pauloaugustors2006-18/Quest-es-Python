codigos_validos = []

print("Insira codigos numéricos divisiveis por 3:")
while len(codigos_validos) < 10:
    numero = int(input(f"Digite o {len(codigos_validos) + 1}º codigo valido: "))
    
    if numero % 3 == 0:
        codigos_validos.append(numero)
    else:
        print(" -> Codigo inválido! O numero precisa ser divisível por 3. Tente novamente.")

soma = sum(codigos_validos)
print(f"\nOs 10 codigos aceitos foram: {codigos_validos}")
print(f"A soma dos codigos eh: {soma}")