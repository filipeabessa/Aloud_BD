class Endereco:
    def __init__(self, cursor, conexao, database):
        self.cursor = cursor
        self.conexao = conexao
        self.database = database

        self.ID_endereco = 1
        self.logradouro = ""
        self.numero = 0
        self.complemento = ""
        self.bairro = ""
        self.cidade = ""
        self.UF = ""

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
