softwares = ["VS Code", "Python", "Git", "Docker", "Postman"]
print("Lista original:", softwares)

novo_software = input("\nDigite o nome do novo software a ser adicionado: ")
softwares.append(novo_software)

removido = softwares.pop(1)
print(f"Software removido da 2ª posicao: {removido}")

print("Lista final atualizada:", softwares)