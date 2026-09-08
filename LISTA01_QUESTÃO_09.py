l1 = float(input("Digite o valor do lado 1:"))
l2 = float(input("Digite o valor do lado 2:"))
l3 = float(input("Digite o valor do lado 3:"))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print("Os valores formam um triângulo")
if l1 == l2 and l2 == l3:
    print("O triângulo eh equilatero")
elif l1 != l2 and l1 != l3 and l2 != l3:
    print("O triângulo eh escaleno")
else:
    print("Os valores não formam um triângulo")