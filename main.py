import mysql.connector

from usuarios import Usuario
from database import Database
from anuncios import Anuncio
from interacoes import Interacoes

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="senhasegura123",
    database="aloud2",
)

cursor = conexao.cursor()

database = Database(cursor, conexao)
usuarios = Usuario(cursor, conexao, database)
anuncios = Anuncio(cursor, conexao, database, usuarios)
interacoes = Interacoes(usuarios, anuncios, usuarios)

# database.criar_tabelas()
interacoes.chamar_boas_vindas()
while usuarios.verificar_logado() == False:
    interacoes.chamar_menu_inicial()
    if usuarios.verificar_logado() == True:
        break

if usuarios.eh_vendedor == True:
    interacoes.chamar_menu_vendedor()

else:
    interacoes.chamar_menu_usuario_comum()

cursor.close()
conexao.close()
