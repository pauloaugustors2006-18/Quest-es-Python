preco = float(input("Digite o preço do produto:\n"))
quantidade = int(input("Digite a quantidade comprada:\n"))
desconto = float(input("Digite o desconto em reais:\n"))

total = preco * quantidade
valor_final = total - desconto

print("Valor da compra:\n", total)
print("Desconto:\n", desconto)
print("Valor final:\n", valor_final)