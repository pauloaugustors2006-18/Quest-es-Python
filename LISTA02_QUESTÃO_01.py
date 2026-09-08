soma = 0
cont = 0

while cont < 10:
    n = int(input("Número:\n"))
    if n % 6 == 0:
        soma += n
        cont += 1
    else:
        print("Erro! Não é divisível por 6.\n")
print("Soma:", soma)
#Questão resolvida Pelo Discente: Paulo Augusto  