class Pokemon:
    def __init__(self, numero, nome, tipo, nivel, hp):
        self.numero = numero
        self.nome = nome
        self.tipo = tipo
        self.nivel = nivel
        self.hp = hp


pokedex = {}

while True:
    print("\nPOKEDEX")
    print("0 - Sair")
    print("1 - Cadastrar Pokémon")
    print("2 - Consultar Pokémon")
    print("3 - Atualizar Pokémon")
    print("4 - Excluir Pokémon")
    print("5 - Listar Pokémon")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        break

    elif opcao == "1":
        numero = int(input("Número da Pokédex: "))
        nome = input("Nome: ")
        tipo = input("Tipo: ")
        nivel = int(input("Nível: "))
        hp = int(input("HP: "))

        pokemon = Pokemon(numero, nome, tipo, nivel, hp)

        pokedex[numero] = pokemon

        print("Pokémon cadastrado com sucesso!")

    elif opcao == "2":
        numero = int(input("Digite o número da Pokédex: "))

        if numero in pokedex:
            pokemon = pokedex[numero]

            print("\nNúmero:", pokemon.numero)
            print("Nome:", pokemon.nome)
            print("Tipo:", pokemon.tipo)
            print("Nível:", pokemon.nivel)
            print("HP:", pokemon.hp)

        else:
            print("Pokémon não encontrado!")

    elif opcao == "3":
        numero = int(input("Digite o número da Pokédex: "))

        if numero in pokedex:
            pokemon = pokedex[numero]

            pokemon.nome = input("Novo nome: ")
            pokemon.tipo = input("Novo tipo: ")
            pokemon.nivel = int(input("Novo nível: "))
            pokemon.hp = int(input("Novo HP: "))

            print("Pokémon atualizado com sucesso!")

        else:
            print("Pokémon não encontrado!")

    elif opcao == "4":
        numero = int(input("Digite o número da Pokédex: "))

        if numero in pokedex:
            del pokedex[numero]

            print("Pokémon excluído com sucesso!")

        else:
            print("Pokémon não encontrado!")

    elif opcao == "5":
        if len(pokedex) == 0:
            print("Nenhum Pokémon cadastrado!")

        else:
            for pokemon in pokedex.values():

                print("\nNúmero:", pokemon.numero)
                print("Nome:", pokemon.nome)
                print("Tipo:", pokemon.tipo)
                print("Nível:", pokemon.nivel)
                print("HP:", pokemon.hp)

    else:
        print("Opção inválida!")