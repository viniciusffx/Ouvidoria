from operacoesbd import *

bancoConexao = abrirBancoDados('127.0.0.1','root','Vini36050.','ouvidoria2')



def listar(bancoConexao):

    print('\nLista de Manifestos\n')

    sqlListarManifestos = 'select * from manifestacoes'
    manifestos = listarBancoDados(bancoConexao, sqlListarManifestos)

    if len(manifestos) == 0:
        print('Sem manifestações e usuários cadastrados!')

    else:
        for i in range(len(manifestos)):
            print(manifestos[i][0], ')','Usuário:',manifestos[i][1],'\n    Manifesto:',manifestos[i][2])


def cadastrar(bancoConexao):

    print('\nCadastro de Manifestações')

    cadastroUsuarios = input('\nDigite seu nome: ')
    cadastroManisfestacao = input('\nDigite sua ocorrência: ')

    if len(cadastroManisfestacao) > 0:

        sqlCadastrarManifesto = 'insert into manifestacoes(usuarios,manifestos) values (%s,%s)'

        dados = [cadastroUsuarios,cadastroManisfestacao]
        insertNoBancoDados(bancoConexao, sqlCadastrarManifesto, dados)
        print('\nUsuário e manifesto cadastrados com sucesso!')

    else:
        print('Opção Inválida!')

def listarPorUsuario(bancoConexao):

    sqlListarManifestos = 'select * from manifestacoes'
    manifestos = listarBancoDados(bancoConexao,sqlListarManifestos)

    if len(manifestos) == 0:
        print('\nSem manifestos e usuários cadastrados!')

    else:

        opcaolistarPorUsuario = input('Digite o usuário para pesquisar seu manifesto: ')
        opcaolistarPorUsuario = '\'' + opcaolistarPorUsuario + '\''

        sqlPesquisaPorUsuario = 'select * from manifestacoes WHERE usuarios = ' + opcaolistarPorUsuario

        manifestos = listarBancoDados(bancoConexao, sqlPesquisaPorUsuario)

        for i in range(len(manifestos)):
            print(manifestos[i][0], ')', 'Usuário:', manifestos[i][1], '\n    Manifesto:', manifestos[i][2])

def excluir(bancoConexao):

    print('\nLista de Manifestos\n')

    sqlListarManifestos = 'select * from manifestacoes'
    manifestos = listarBancoDados(bancoConexao, sqlListarManifestos)

    if len(manifestos) == 0:
        print('Sem manifestações e usuários cadastrados!')

    else:
        for i in range(len(manifestos)):
            print(manifestos[i][0], ')','Usuário:',manifestos[i][1],'\n    Manifesto:',manifestos[i][2])

        opcaoRemover = int(input('\nDigite o código do manifesto a ser removido: '))

        sqlRemoverManifesto = 'DELETE FROM manifestacoes WHERE codigo = %s'
        dados = [opcaoRemover]

        excluirBancoDados(bancoConexao, sqlRemoverManifesto, dados)
        print('\nManifestação removida com sucesso!')

def excluirPorUsuarios(bancoConexao):

    print('\nLista de Manifestos\n')

    sqlListarManifestos = 'select * from manifestacoes'
    manifestos = listarBancoDados(bancoConexao, sqlListarManifestos)

    if len(manifestos) == 0:
        print('Sem manifestações e usuários cadastrados!')

    else:
        for i in range(len(manifestos)):
            print(manifestos[i][0], ')', 'Usuário:', manifestos[i][1], '\n    Manifesto:', manifestos[i][2])

        opcaoRemover = input('\nDigite o usuário que deseja excluir os manifestos: ')

        dados = [opcaoRemover]

        sqlRemoverManifestoPorUsuario = 'DELETE FROM manifestacoes WHERE usuarios like %s'
        excluirBancoDados(bancoConexao,sqlRemoverManifestoPorUsuario,dados)
        print('\nUsuário e manifesto removidos com sucesso!')

def alterar(bancoConexao):

    print('\nLista de Manifestos\n')

    sqlListarManifestos = 'select * from manifestacoes'
    manifestos = listarBancoDados(bancoConexao, sqlListarManifestos)

    if len(manifestos) == 0:
        print('Sem manifestações e usuários cadastrados!')

    else:

        for i in range(len(manifestos)):
            print(manifestos[i][0], ')', 'Usuário:', manifestos[i][1], '\n    Manifesto:', manifestos[i][2])

        opcaoAlterar = int(input('\nDigite o codigo do manifesto a ser alterado: '))
        novoManifesto = input('\nDigite o novo manifesto: ')

        dados = [novoManifesto, opcaoAlterar]

        atualizacaoDeManifesto = 'UPDATE manifestacoes SET manifestos = %s WHERE codigo =%s ;'
        atualizarBancoDados(bancoConexao, atualizacaoDeManifesto, dados)
        print('\nManifesto alterado com sucesso!\n')


encerrarBancoDados(bancoConexao)