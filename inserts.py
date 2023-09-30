from operacoesbd import *

from metodos import *

bancoConexao=abrirBancoDados("127.0.0.1','root','12345','Ouvidoria_2.0")
consultaManifesto= 'insert into manifesto (manifesto) values(%s)'
insertNoBancoDados(bancoConexao,consultaManifesto,cadastroManifesto)
listarBancoDados()
atualizarBancoDados()
excluirBancoDados()
encerrarBancoDados(bancoConexao)