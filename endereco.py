from database import Database


class Endereco:
    def __init__(self, cursor, conexao):
        self.cursor = cursor
        self.conexao = conexao
        self.database = Database(cursor, conexao)

        self.ID_endereco = 1
        self.logradouro = ""
        self.numero = 0
        self.complemento = ""
        self.bairro = ""
        self.cidade = ""
        self.UF = ""

    def receber_id_endereco(self):
        return self.ID_endereco

    def cadastrar_endereco(self):
        print("Endereço: \n")
        self.CEP = input("CEP: ")
        self.logradouro = input("Logradouro: ")
        self.numero = input("Número: ")
        self.complemento = input("Complemento: ")
        self.bairro = input("Bairro: ")
        self.UF = input("União federativa: ")
        self.cidade = input("Municipio: ")

        self.database.cadastrar_endereco(
            self.logradouro,
            self.numero,
            self.complemento,
            self.bairro,
            self.cidade,
            self.UF,
            self.CEP,
        )
        self.ID_endereco = self.database.receber_ultimo_id_endereco()

    def editar_endereco(self, id_endereco):
        print("Endereço: \n")
        self.CEP = input("CEP: ")
        self.logradouro = input("Logradouro: ")
        self.numero = input("Número: ")
        self.complemento = input("Complemento: ")
        self.bairro = input("Bairro: ")
        self.UF = input("União federativa: ")
        self.cidade = input("Municipio: ")

        self.database.editar_endereco(
            id_endereco,
            self.logradouro,
            self.numero,
            self.complemento,
            self.bairro,
            self.cidade,
            self.UF,
            self.CEP,
        )
