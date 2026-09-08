#Quarta questão
print("1- Descobrir a hipotenusa:\n")

print("2- Descobrir um cateto:\n")

escolha = int(input("Digite o valor 1 ou 2:\n"))

if escolha == 1:
    cateto_a = float(input("Digite o valor do cateto A:\n"))
    cateto_b = float(input("Digite o valor de cateto B:\n"))
    resultado = (cateto_a ** 2 + cateto_b ** 2) ** 0.5
    print("O Valor da Hipotenusa:\n", resultado)
    
elif escolha == 2:

    h = float(input("Digite o valor da hipotenusa:\n"))
    a = float(input("Digite o valor do cateto conhecido:\n"))
    resultado = (h ** 2 - a ** 2) ** 0.5
    print("O valor do outro cateto eh:\n", resultado)

else:

    print("Opcao Invalida 1 ou 2:\n")