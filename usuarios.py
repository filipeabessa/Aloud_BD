from endereco import Endereco


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
        self.logado = False
        self.eh_vendedor = False

        self.endereco = Endereco(cursor, conexao)

    def __str__(self):
        return self.nome

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

            print(self.ID_usuario)
            comando = (
                f'SELECT * FROM usuario_vendedor WHERE id_usuario = "{self.ID_usuario}"'
            )
            self.cursor.execute(comando)
            infos_usuario_vendedor = self.cursor.fetchall()
            print(infos_usuario_vendedor)

            if len(infos_usuario_vendedor) > 0:
                self.eh_vendedor = True
                self.cpf_cnpj = infos_usuario_vendedor[0][0]
                self.data_nascimento = infos_usuario_vendedor[0][1]
                self.foto_perfil = infos_usuario_vendedor[0][2]
                self.ID_endereco = infos_usuario_vendedor[0][4]

            else:
                self.eh_vendedor = False

            print("Login realizado com sucesso!")
            self.logado = True
        else:
            print("Email ou senha incorretos!")

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

        self.cursor.execute(
            f"SELECT MAX(id_usuario) FROM {self.conexao.database}.usuario"
        )
        self.ID_usuario = self.cursor.fetchall()[0][0]

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
