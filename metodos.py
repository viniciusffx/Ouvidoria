from operacoesbd import *

bancoConexao = abrirBancoDados('127.0.0.1','root','Vini36050.','ouvidoria2.0')



def listar(bancoConexao):

    print('\nLista de Manifestos\n')

    sqlListarManifestos = 'select * from manifestacoes'
    manifestos = listarBancoDados(bancoConexao, sqlListarManifestos)

    for i in range(len(manifestos)):
        print(manifestos[i][0], ')', manifestos[i][1])


def cadastrar(bancoConexao):

    print('\nCadastro de Manifestações')

    cadastroManisfestacao = input('Digite sua ocorrência: ')

    if len(cadastroManisfestacao) > 0:

        sqlCadastrarManifesto = 'insert into manifestacoes(manifestos) values (%s)'
        dados = [cadastroManisfestacao]
        insertNoBancoDados(bancoConexao, sqlCadastrarManifesto, dados)
    else:
        print('Opção Inválida')


def excluir(bancoConexao):

    opcaoRemover = int(input('Digite o manifesto a ser removido: '))

    dados = [opcaoRemover]

    sqlRemoverManifesto = 'DELETE FROM manifestacoes WHERE codigo = %s'
    excluirBancoDados(bancoConexao, sqlRemoverManifesto, dados)
    print('Manifestação removida com sucesso!')


def alterar(bancoConexao):

    opcaoAlterar = int(input('Digite o codigo manifesto a ser Alterado: '))
    novoManifesto = input('Digite o novo manifesto')

    dados = [novoManifesto, opcaoAlterar]

    atualizacaoDeManifesto = 'UPDATE manifestacoes SET manifestos = %s WHERE codigo =%s ;'
    atualizarBancoDados(bancoConexao, atualizacaoDeManifesto, dados)
    print('\nManifesto alterado com sucesso!\n')


encerrarBancoDados(bancoConexao)