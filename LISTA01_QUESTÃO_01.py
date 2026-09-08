#Primeira Questão
horas = int(input("Digite as horas do Relatorio:\n"))
minutos = int(input("Digite os minutos do Relatorio:\n"))

segundos = (horas * 60) + (minutos * 3600)
print("Os segundos do relatorio são:\n", segundos)