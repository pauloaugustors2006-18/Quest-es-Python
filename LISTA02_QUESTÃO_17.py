agenda_telefonica = {
    "Paulo Augusto": "99999-9999",
    "Raimundo Victor": "98888-8888",
    "Bruno Bueno": "97777-7777"
}
nome = input("Digite o nome:\n")

if nome in agenda_telefonica:
    print("Telefone:", agenda_telefonica[nome])
else:
    print("Contato não encontrado")
#Questão resolvida Pelo Discente: Paulo Augusto 