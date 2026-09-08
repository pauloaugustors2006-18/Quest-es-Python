valor_financiado = float(input("Digite o valor do financiado:"))
taxa = float(input("Me informe a taxa de juros mensal (%):"))
meses = int(input("Me informe a quantidade de meses:"))

juros = valor_financiado * (taxa /100)  * meses
montante = valor_financiado = juros

print("Juros acumulado:\n", juros)
print("Montante total:\n", montante)