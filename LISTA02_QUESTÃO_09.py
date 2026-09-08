notas = []
try:
    for i in range(5):
        n = float(input("Digite a nota:\n"))
        notas.append(n)

    print("Notas:", notas)
    print("Media:", sum(notas) / len(notas))
    print("Maior nota:", max(notas))
    print("Menor nota:", min(notas))
except ValueError:
    print("Erro: Digite apenas numeros!\n")
#Questão resolvida Pelo Discente: Paulo Augusto 