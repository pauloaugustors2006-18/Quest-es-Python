def exibir_nome_do_programa():
    print("====================================")
    print("   SISTEMA DE GERENCIAMENTO ACADEMICO")
    print("====================================")


def exibir_menu():
    print("SISTEMA ACADEMICO")
    print("1 - Cadastrar estudante")
    print("2 - Listar estudantes")
    print("3 - Alterar situacao")
    print("0 - Sair")


def cadastrar_estudante():
    print("Opcao Cadastrar estudante selecionada.")


def listar_estudantes():
    print("Opcao Listar estudantes selecionada.")


def alterar_situacao_estudante():
    print("Opcao Alterar situacao selecionada.")


def opcao_invalida():

    print("Opcao invalida! Essa opcao nao existe.")


def finalizar_programa():
    
    print("Sistema sendo encerrado...")


def main():
   
    
    exibir_nome_do_programa()

    while True:
        exibir_menu()

        opcao = input("Digite uma opcao: ")

        if opcao == "1":
            cadastrar_estudante()
        elif opcao == "2":
            listar_estudantes()
        elif opcao == "3":
            alterar_situacao_estudante()
        elif opcao == "0":
            finalizar_programa()
            break
        else:
            opcao_invalida()
main()