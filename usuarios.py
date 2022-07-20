from endereco import Endereco

# from compras import Compras
from database import Database
from carrinho import Carrinho


class Usuario:
    def __init__(self, cursor, conexao):
        self.cursor = cursor
        self.conexao = conexao
        self.database = Database(cursor, conexao)

        self.nome = ""
        self.sobrenome = ""
        self.email = ""
        self.senha = ""
        self.ID_usuario = 0
        self.ID_endereco = 0
        self.cpf_cnpj = ""
        self.data_nascimento = ""
        self.foto_perfil = ""
        self.logado = False
        self.eh_vendedor = False
        self.ID_carrinho = 0

        self.endereco = Endereco(cursor, conexao)
        # self.compras = Compras(cursor, conexao)

    def __str__(self):
        return self.nome

    def receber_cpf_cnpj(self):
        return self.cpf_cnpj

    def verificar_logado(self):
        return self.logado

    def login(self):
        print("Login: \n")
        self.email = input("Email: ")
        self.senha = input("Senha: ")

        comando = f'SELECT * FROM usuario WHERE email = "{self.email}" AND senha = "{self.senha}"'
        self.cursor.execute(comando)
        infos_usuario = self.cursor.fetchall()

        if len(infos_usuario) > 0:
            self.ID_usuario = infos_usuario[0][0]
            self.nome = infos_usuario[0][1]
            self.sobrenome = infos_usuario[0][2]
            self.email = infos_usuario[0][3]

            comando = (
                f'SELECT * FROM usuario_vendedor WHERE id_usuario = "{self.ID_usuario}"'
            )
            self.cursor.execute(comando)
            infos_usuario_vendedor = self.cursor.fetchall()

            if len(infos_usuario_vendedor) > 0:
                self.eh_vendedor = True
                self.cpf_cnpj = infos_usuario_vendedor[0][0]
                self.data_nascimento = infos_usuario_vendedor[0][1]
                self.foto_perfil = infos_usuario_vendedor[0][2]
                self.ID_endereco = infos_usuario_vendedor[0][4]

            else:
                self.eh_vendedor = False

            print("\nLogin realizado com sucesso!\n")
            self.logado = True

        else:
            print("\nEmail ou senha incorretos!\n")

    def cadastrar_usuario(self):
        print("Cadastro de usuário:\n")
        self.nome = input("Nome: ")
        self.sobrenome = input("Sobrenome: ")
        self.email = input("Email: ")
        self.senha = input("Senha: ")

        self.database.cadastrar_usuario_comum(
            self.nome, self.sobrenome, self.email, self.senha
        )

        self.cursor.execute(
            f"SELECT MAX(id_usuario) FROM {self.conexao.database}.usuario"
        )
        self.ID_usuario = self.cursor.fetchall()[0][0]

        carrinho = Carrinho(self.cursor, self.conexao, self.ID_usuario)
        carrinho.criar_carrinho()

        cadastrar_info_vendedor = input(
            "Deseja anunciar produtos/serviços ou apenas comprar? (se deseja apenas comprar digite 1, e se deseja também anunciar, digite 2) "
        )

        if cadastrar_info_vendedor == "2":
            self.eh_vendedor = True
            print("Cadastro vendedor: \n")
            self.cpf_cnpj = input("CPF/CNPJ:")
            self.data_nascimento = input("Data de nascimento (aaaa-mm-dd): ")
            self.foto_perfil = input("Foto de perfil (link): ")

            self.endereco.cadastrar_endereco()

            self.cursor.execute(
                f"SELECT MAX(id_endereco) FROM {self.conexao.database}.endereco"
            )
            self.ID_endereco = self.cursor.fetchall()[0][0]

            self.database.cadastrar_usuario_vendedor(
                self.cpf_cnpj,
                self.data_nascimento,
                self.foto_perfil,
                self.ID_usuario,
                self.ID_endereco,
            )

        else:
            return

    def editar_usuario_comum(self):
        print("Edição de usuário:\n")
        self.nome = input("Nome: ")
        self.sobrenome = input("Sobrenome: ")
        self.email = input("Email: ")
        self.senha = input("Senha: ")

        self.database.editar_usuario_comum(
            self.ID_usuario, self.nome, self.sobrenome, self.email, self.senha
        )

    def editar_usuario_vendedor(self):
        self.editar_usuario_comum()
        self.data_nascimento = input("Data de nascimento (aaaa-mm-dd): ")
        self.foto_perfil = input("Foto de perfil (link): ")

        self.database.editar_usuario_vendedor(
            self.ID_usuario, self.data_nascimento, self.foto_perfil
        )

    def editar_endereco(self):
        self.endereco.editar_endereco(self.ID_endereco)

    # def listar_compras(self):
    #     self.compras.listar_compras(self.ID_usuario)

    def visualizar_informacoes_perfil(self):
        if self.eh_vendedor:
            informacoes_usuario = self.database.pegar_informacoes_perfil(
                self.ID_usuario, True
            )
            informacoes_usuario = informacoes_usuario[0]
            print(f"\nNome: {informacoes_usuario[1]} {informacoes_usuario[2]}")
            print(f"Email: {informacoes_usuario[3]}")
            print(f"Data de nascimento: {informacoes_usuario[6]}\n")

        else:
            informacoes_usuario = self.database.pegar_informacoes_perfil(
                self.ID_usuario, False
            )
            informacoes_usuario = informacoes_usuario[0]
            print(f"\nNome: {informacoes_usuario[1]} {informacoes_usuario[2]}")
            print(f"Email: {informacoes_usuario[3]}\n")
