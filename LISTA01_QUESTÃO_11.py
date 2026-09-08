#Décima Primeira Questão
valor = float(input("Digite o valor do emprestimo:\n"))
taxa = float(input("Digite o valor da Taxa(%):\n"))
meses = int(input("Digite a quantidade de meses:\n"))

juros = valor * (taxa /100) * meses
total = valor + juros

print(f"Juros pagos:\n", juros)
print(f"Total:\n", total)