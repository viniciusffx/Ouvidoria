from metodos import *

manifestacoes = []
opcao = 1

while opcao != 5:

    opcao = menu()

    if opcao == 1:

        listar(manifestacoes)

    elif opcao == 2:

        cadastrar(manifestacoes)

    elif opcao == 3:

        listar(manifestacoes)
        excluir(manifestacoes)

    elif opcao == 4:

        listar(manifestacoes)
        alterar(manifestacoes)

    elif opcao != 5:
        print('Opção inválida!')


    else:
        print('Fim')

