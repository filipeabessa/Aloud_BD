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
