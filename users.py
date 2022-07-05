import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="senhasegura123",
    database="aloud",
)


cursor = conexao.cursor()


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


usuario = Usuario(cursor, conexao)

usuario.cadastrar_usuario()


cursor.close()
conexao.close()
