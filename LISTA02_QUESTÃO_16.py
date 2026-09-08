alunos = {
    "Paulo Augusto": 10,
    "Raimundo Victor": 1
}
for nome, nota in alunos.items():

    if nota >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    print("Aluno:", nome)
    print("Nota:", nota)
    print("Situacao:", situacao)
    print()
    
#Questao resolvida Pelo Discente: Paulo Augusto 