import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="senhasegura123",
    database="aloud2",
)


cursor = conexao.cursor()


class Tabela:
    def __init__(self, cursor, conexao):
        self.conexao = conexao
        self.cursor = cursor

    def criar_tabela_usuario(self):
        comando = "CREATE TABLE usuario (id_usuario INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(50), sobrenome VARCHAR(100), email VARCHAR(255), senha VARCHAR(8))"
        self.cursor.execute(comando)
        self.conexao.commit()

    def criar_tabela_endereco(self):
        comando = "CREATE TABLE endereco (id_endereco INT AUTO_INCREMENT PRIMARY KEY, cidade VARCHAR(50), UF VARCHAR(50), CEP VARCHAR(10), logradouro VARCHAR(50), numero INT, complemento VARCHAR(50))"
        self.cursor.execute(comando)
        self.conexao.commit()

    def criar_tabela_anuncio(self):
        comando = "CREATE TABLE anuncio (id_anuncio INT AUTO_INCREMENT PRIMARY KEY, cpf_cnpj VARCHAR(20), FOREIGN KEY (cpf_cnpj) REFERENCES usuario_vendedor(cpf_cnpj), titulo_anuncio VARCHAR(100), descricao VARCHAR(255), preco FLOAT(10,2), foto_produto VARCHAR(255), fabricante VARCHAR(50), quantidade_produto INT, status_aprovacao VARCHAR(10), estado_novo BOOLEAN)"
        self.cursor.execute(comando)
        self.conexao.commit()

    def criar_tabela_usuario_vendedor(self):
        comando = "CREATE TABLE usuario_vendedor (cpf_cnpj VARCHAR(20) PRIMARY KEY, data_nascimento DATE, foto_perfil VARCHAR(255), id_usuario INT, FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario), id_endereco INT, FOREIGN KEY (id_endereco) REFERENCES endereco(id_endereco))"
        self.cursor.execute(comando)
        self.conexao.commit()

    def criar_tabela_compra(self):
        comando = "CREATE TABLE compra (id_compra INT AUTO_INCREMENT PRIMARY KEY, id_usuario INT, FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario), id_endereco INT, FOREIGN KEY (id_endereco) REFERENCES endereco(id_endereco), id_anuncio INT, FOREIGN KEY (id_anuncio) REFERENCES anuncio(id_anuncio), valor_total FLOAT(10,2), data_compra DATE, forma_de_pag VARCHAR(50), modo_envio VARCHAR(50))"
        self.cursor.execute(comando)
        self.conexao.commit()

    def criar_tabela_compra_anuncio(self):
        comando = "CREATE TABLE compra_anuncio (id_compra INT, FOREIGN KEY (id_compra) REFERENCES compra(id_compra), id_anuncio INT, FOREIGN KEY (id_anuncio) REFERENCES anuncio(id_anuncio))"
        self.cursor.execute(comando)
        self.conexao.commit()

    def listar_usuarios(self):
        comando = "SELECT * FROM usuario"
        self.cursor.execute(comando)
        lista_usuarios = self.cursor.fetchall()

        print("\nLista de usuários:")
        for usuario in lista_usuarios:
            print(
                f"ID_usuario: {usuario[0]}, Nome: {usuario[1]} {usuario[2]}, Email: {usuario[3]}"
            )


class Endereco:
    def __init__(self, cursor, conexao):
        self.cursor = cursor
        self.conexao = conexao

        self.ID_endereco = 1
        self.logradouro = ""
        self.numero = 0
        self.complemento = ""
        self.bairro = ""
        self.cidade = ""
        self.UF = ""

    def cadastrar_endereco_banco(self):
        comando = f'INSERT INTO endereco (logradouro, numero, complemento, bairro, cidade, UF) VALUES ("{self.logradouro}", "{self.numero}", "{self.complemento}", "{self.bairro}", "{self.cidade}", "{self.UF}")'
        self.cursor.execute(comando)
        self.conexao.commit()

    def editar_endereco_banco(
        self, logradouro, numero, complemento, bairro, cidade, UF
    ):
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.UF = UF

        comando = f'UPDATE endereco SET logradouro = "{self.logradouro}", numero = "{self.numero}", complemento = "{self.complemento}", bairro = "{self.bairro}", cidade = "{self.cidade}", UF = "{self.UF}" WHERE ID_endereco = "{self.ID_endereco}"'

        self.cursor.execute(comando)
        self.conexao.commit()

    def cadastrar_endereco(self):
        print("Endereço: \n")
        self.CEP = input("CEP: ")
        self.logradouro = input("Logradouro: ")
        self.numero = input("Número: ")
        self.complemento = input("Complemento: ")
        self.bairro = input("Bairro: ")
        self.UF = input("União federativa: ")
        self.cidade = input("Municipio: ")

        self.cadastrar_endereco_banco()


class Usuario:
    def __init__(self, cursor, conexao):
        self.cursor = cursor
        self.conexao = conexao

        self.nome = ""
        self.sobrenome = ""
        self.email = ""
        self.senha = ""
        self.ID_usuario = 0
        self.ID_endereco = 0
        self.cpf_cnpj = ""
        self.data_nascimento = ""
        self.foto_perfil = ""

        self.endereco = Endereco(cursor, conexao)

    def __str__(self):
        return self.nome

    def login(self):
        pass

    def editar_usuario_comum_banco(self):
        pass

    def editar_usuario_vendedor_banco(self):
        pass

    def cadastrar_usuario_comum_banco(self, nome, sobrenome, email, senha):
        comando = f'INSERT INTO usuario (nome, sobrenome, email, senha) VALUES ("{nome}", "{sobrenome}", "{email}", "{senha}")'

        self.cursor.execute(comando)
        self.conexao.commit()

    def cadastrar_usuario_vendedor_banco(
        self, cpf_cnpj, data_nascimento, foto_perfil, id_usuario, id_endereco
    ):
        comando = f'INSERT INTO usuario_vendedor (cpf_cnpj, data_nascimento, foto_perfil, id_usuario, id_endereco) VALUES ("{cpf_cnpj}", "{data_nascimento}", "{foto_perfil}", "{id_usuario}", "{id_endereco}")'

        self.cursor.execute(comando)
        self.conexao.commit()

    def cadastrar_usuario(self):
        print("Cadastro de usuário:\n")
        self.nome = input("Nome: ")
        self.sobrenome = input("Sobrenome: ")
        self.email = input("Email: ")
        self.senha = input("Senha: ")

        self.cadastrar_usuario_comum_banco(
            self.nome, self.sobrenome, self.email, self.senha
        )

        self.cursor.execute("SELECT MAX(id_usuario) FROM aloud.usuario")
        self.ID_usuario = cursor.fetchall()[0][0]

        cadastrar_info_vendedor = input(
            'Deseja anunciar produtos/serviços ou apenas comprar? (responda com "sim" ou "não") '
        )

        if cadastrar_info_vendedor == "sim":
            print("Cadastro vendedor: \n")
            self.cpf_cnpj = input("CPF/CNPJ:")
            self.data_nascimento = input("Data de nascimento: ")
            self.foto_perfil = input("Foto de perfil (link): ")

            self.endereco.cadastrar_endereco()

            self.cursor.execute("SELECT MAX(id_endereco) FROM aloud.endereco")
            self.ID_endereco = cursor.fetchall()[0][0]

            self.cadastrar_usuario_vendedor_banco(
                self.cpf_cnpj,
                self.data_nascimento,
                self.foto_perfil,
                self.ID_usuario,
                self.ID_endereco,
            )

        else:
            return

    def editar_usuario_comum(self, nome, sobrenome, email, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha

        # comando = f"UPDATE "


class Anuncio:
    def __init__(self, cursor, conexao):
        self.cursor = cursor
        self.conexao = conexao

        self.cpf_cnpj = ""
        self.titulo_anuncio = ""
        self.descricao = ""
        self.preco = 0.0
        self.foto_produto = ""
        self.fabricante = ""
        self.quantidade_produto = ""
        self.status_aprovacao = ""
        self.estado_novo = ""


usuario = Usuario(cursor, conexao)
tabela = Tabela(cursor, conexao)

# usuario.cadastrar_usuario()
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
