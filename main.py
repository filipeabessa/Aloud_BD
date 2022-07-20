import mysql.connector

from usuarios import Usuario
from anuncios import Anuncios
from interacoes import Interacoes
from carrinho import Carrinho
from database import Database

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="senhasegura123",
    database="aloud2",
)

cursor = conexao.cursor()

database = Database(cursor, conexao)
usuario = Usuario(cursor, conexao)
carrinho_compras = Carrinho(cursor, conexao, usuario.ID_usuario)
anuncios = Anuncios(cursor, conexao, usuario)
interacoes = Interacoes(cursor, conexao, usuario)

# database.criar_tabelas()
interacoes.chamar_boas_vindas()
while usuario.verificar_logado() == False:
    interacoes.chamar_menu_inicial()
    if usuario.verificar_logado() == True:
        break

if usuario.eh_vendedor == True:
    interacoes.chamar_menu_vendedor()

else:
    interacoes.chamar_menu_usuario_comum()

cursor.close()
conexao.close()
