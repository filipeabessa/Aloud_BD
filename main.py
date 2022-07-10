import mysql.connector

from usuarios import Usuario
from database import Database

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="senhasegura123",
    database="aloud2",
)

cursor = conexao.cursor()

usuario = Usuario(cursor, conexao)
tabela = Database(cursor, conexao)

tabela.listar_usuarios()

print("Bem-vindo à Aloud! O que você deseja fazer? \n")
resposta = input("1 - Cadastrar usuário\n2 - Login\n3 - Buscar produtos/serviços\n")

if resposta == "1":
    usuario.cadastrar_usuario()

elif resposta == "2":
    print("Ainda não implementado")

elif resposta == "3":
    print("Ainda não implementado")


resposta_2 = input('Deseja listar usuários? (responda com "sim" ou "não")')
if resposta_2 == "sim":
    tabela.listar_usuarios()

print("\nObrigado por usar a Aloud!")


cursor.close()
conexao.close()
