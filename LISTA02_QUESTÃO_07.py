notas = [9.0, 7.5, 6.0]  # Exemplo de lista
try:
    media = sum(notas) / len(notas)
    print("Média:", media)
except ZeroDivisionError:
    print("A lista de notas está vazia!")
#Questão resolvida Pelo Discente: Paulo Augusto 