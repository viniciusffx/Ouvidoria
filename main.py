from metodos import *
from operacoesbd import *

bancoConexao = abrirBancoDados('127.0.0.1','root','Vini36050.','ouvidoria2')

opcao = 1

while opcao != 6:

    print()
    print('\nOuvidoria com Metodos\n')
    print('1)Listar\n2)Cadastrar\n3)Excluir por código\n4)Excluir por Usuário\n5)Alterar por código\n6)Sair')
    opcao = int(input('\nDigite a opcao desejada: '))


    if opcao == 1:

        listar(bancoConexao)

    elif opcao == 2:

        cadastrar(bancoConexao)

    elif opcao == 3:

        listar(bancoConexao)
        excluir(bancoConexao)

    elif opcao == 4:

        listar(bancoConexao)
        excluirPorUsuarios(bancoConexao)

    elif opcao == 5:

        listar(bancoConexao)
        alterar(bancoConexao)

    elif opcao != 6:
        print('Opção inválida!')


    else:
        print('Fim')

encerrarBancoDados(bancoConexao)

