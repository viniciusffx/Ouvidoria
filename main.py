from metodos import *
from operacoesbd import *

bancoConexao = abrirBancoDados('127.0.0.1','root','Vini36050.','ouvidoria2.0')

opcao = 1

while opcao != 5:

    print()
    print('\nOuvidoria com Metodos\n')
    print('1)Listar\n2)Cadastrar\n3)Excluir\n4)Alterar\n5)Sair')
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
        alterar(bancoConexao)

    elif opcao != 5:
        print('Opção inválida!')


    else:
        print('Fim')

encerrarBancoDados(bancoConexao)

