vogais = 0
consoantes = 0
lista_vogais = ['a', 'e', 'i', 'o', 'u']

for i in range(1, 11):
    letra = input(f"Digite a {i}ª letra: ").strip().lower()
    
    if letra.isalpha() and len(letra) == 1:
        if letra in lista_vogais:
            vogais += 1
        else:
            consoantes += 1
    else:
        print("Entrada inválida! Digite apenas uma letra.")

print("\n--- Resultado ---")
print(f"Quantidade de vogais: {vogais}")
print(f"Quantidade de consoantes: {consoantes}")