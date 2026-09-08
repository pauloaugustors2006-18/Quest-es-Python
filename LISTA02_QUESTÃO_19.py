aluno = {
    "Joao": {
        "Nota 1": 8.0,
        "Nota 2": 7.5
    }
}
for nome, dados in aluno.items():
    media = (dados["Nota 1"] + dados["Nota 2"]) / 2
    
    if media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    print("Aluno:", nome)
    print("Nota 1:", dados["Nota 1"])
    print("Nota 2:", dados["Nota 2"])
    print("Media:", media)
    print("Situacao:", situacao)