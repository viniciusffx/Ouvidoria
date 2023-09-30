from operacoesbd import *
bancoConexao=abrirBancoDados("127.0.0.1','root','Vini36050.','ouvidoria2.0")
def menu():
    print()
    print('\nOuvidoria com Metodos\n')
    print('1)Listar\n2)Cadastrar\n3)Excluir\n4)Alterar\n5)Sair')
    opcao = int(input('\nDigite a opcao desejada: '))
    return opcao


def listar(manifestacoes):
    if len(manifestacoes) > 0:
        print('\nLista de Manifestos')

        consultaManifestacoes = 'select * from manifesto'
        manifesto = listarBancoDados(bancoConexao, consultaManifestacoes)

        for m in manifesto:
            print(m)

    else:
        print('\nSem manifestos cadastrados!')

    return manifestacoes


def cadastrar(manifestacoes):
    cadastroManifesto = input('\nDigite sua ocorrencia: ')

    if len(cadastroManifesto) > 0:

        manifestacoes.append(cadastroManifesto)
        print('\nOcorrencia cadastrada com sucesso!')

    else:
        print('Sem caracteres digitados!')

    return manifestacoes


def excluir(manifestacoes):
    if len(manifestacoes) > 0:

        removerManifesto = int(input('\nDigite a ocorrencia que deseja remover: '))

        manifestacoes.pop(removerManifesto - 1)
        print('\nManifesto removido com sucesso!')

    else:
        print('Sem ocorrencias!')

    return manifestacoes


def alterar(manifestacoes):

    if len(manifestacoes) > 0:

        alterarManifesto = int(input('\nDigite o manifesto que deseja alterar: '))
        novoManifesto = input('\nDigite o novo manifesto: ')

        manifestacoes[alterarManifesto - 1] = novoManifesto
        print('\nManifesto alterado com sucesso!')

    else:
        print('\nsem ocorrencias cadastradas!')

    return manifestacoes
encerrarBancoDados(bancoConexao)
