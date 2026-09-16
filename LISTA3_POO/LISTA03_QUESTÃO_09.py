inicio_input = int(input("Digite o primeiro identificador: "))
fim_input = int(input("Digite o ultimo identificador: "))

inicio = min(inicio_input, fim_input)
fim = max(inicio_input, fim_input)

intervalo = list(range(inicio, fim + 1))
media = sum(intervalo) / len(intervalo)

print(f"\nA media dos numeros no intervalo de {inicio} a {fim} eh: {media:.2f}")