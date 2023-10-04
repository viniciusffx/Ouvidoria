from operacoesbd import *

bancoConexao = abrirBancoDados('127.0.0.1','root','Vini36050.','ouvidoria2')



def listar(bancoConexao):

    print('\nLista de Manifestos\n')

    sqlListarManifestos = 'select * from manifestacoes'
    manifestos = listarBancoDados(bancoConexao, sqlListarManifestos)
    quantidade= manifestos[0][0]
    if quantidade ==0:
        print('Não existem manifestações cadastradas!')
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
        print('\nCadastro feito com sucesso!')

    else:
        print('Opção Inválida')


def excluir(bancoConexao):

    opcaoRemover = int(input('\nDigite o codigo do manifesto a ser removido: '))

    dados = [opcaoRemover]

    sqlRemoverManifesto = 'DELETE FROM manifestacoes WHERE codigo = %s'
    excluirBancoDados(bancoConexao, sqlRemoverManifesto, dados)
    print('\nManifestação removida com sucesso!')

def excluirPorUsuarios(bancoConexao):

    opcaoRemover = input('\nDigite o usuário que deseja excluir os manifestos: ')

    dados = [opcaoRemover]

    sqlRemoverManifestoPorUsuario = 'DELETE FROM manifestacoes WHERE usuarios like %s'
    excluirBancoDados(bancoConexao,sqlRemoverManifestoPorUsuario,dados)
    print('\nManifestação removida com sucesso!')

def alterar(bancoConexao):

    opcaoAlterar = int(input('\nDigite o codigo do manifesto a ser alterado: '))
    novoManifesto = input('\nDigite o novo manifesto: ')

    dados = [novoManifesto, opcaoAlterar]

    atualizacaoDeManifesto = 'UPDATE manifestacoes SET manifestos = %s WHERE codigo =%s ;'
    atualizarBancoDados(bancoConexao, atualizacaoDeManifesto, dados)
    print('\nManifesto alterado com sucesso!\n')


def listarPorUsuario(bancoConexao):

    opcaolistarPorUsuario = input('Digite o usuário para pesquisar seu manifesto: ')
    opcaolistarPorUsuario= '\n'+opcaolistarPorUsuario+'\n'
    sqlPesquisaPorUsuario = 'select * from manifestacoes WHERE usuarios LIKE ' + opcaolistarPorUsuario
    manifesto=listarBancoDados(bancoConexao,sqlPesquisaPorUsuario)

    for i in range(len(manifesto)):
        print(manifesto[i][0], ')', 'Usuário:', manifesto[i][1], '\n    Manifesto:', manifesto[i][2])


encerrarBancoDados(bancoConexao)