nome = input("Digite o nome: ")
ano_nascimento = int(input("Digite o ano de nascimento:\n"))

ano_atual = 2026
idade = ano_atual - ano_nascimento

if idade >= 18:
    situacao = "Pode entrar desacompanhado."
else:
    situacao = "Precisa estar acompanhado com um responsável."

print("Nome:", nome)
print("Idade:", idade)
print("Situação:", situacao)