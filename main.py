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

usuarios = Usuario(cursor, conexao)
database = Database(cursor, conexao)
anuncios = Anuncio(cursor, conexao)
interacoes = Interacoes(usuarios)


cursor.close()
conexao.close()
