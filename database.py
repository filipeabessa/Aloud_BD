class Database:
    def __init__(self, cursor, conexao):
        self.conexao = conexao
        self.cursor = cursor

    def criar_tabela_usuario(self):
        comando = "CREATE TABLE usuario (id_usuario INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(50), sobrenome VARCHAR(100), email VARCHAR(255), senha VARCHAR(8))"
        self.cursor.execute(comando)
        self.conexao.commit()

    def criar_tabela_endereco(self):
        comando = "CREATE TABLE endereco (id_endereco INT AUTO_INCREMENT PRIMARY KEY, cidade VARCHAR(50), UF VARCHAR(50), CEP VARCHAR(10), logradouro VARCHAR(50), numero INT, complemento VARCHAR(50), bairro VARCHAR(50))"
        self.cursor.execute(comando)
        self.conexao.commit()

    def criar_tabela_anuncio(self):
        comando = "CREATE TABLE anuncio (id_anuncio INT AUTO_INCREMENT PRIMARY K VARCHAR(20), FOREIGN KEY (cpf_cnpj) REFERENCES usuario_vendedor(cpf_cnpj), titulo_anuncio VARCHAR(100), descricao VARCHAR(255), preco FLOAT(10,2), foto_produto VARCHAR(255), fabricante VARCHAR(50), quantidade_produto INT, status_aprovacao VARCHAR(10), estado_novo BOOLEAN)"
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

    def criar_tabelas(self):
        self.criar_tabela_usuario()
        self.criar_tabela_endereco()
        self.criar_tabela_usuario_vendedor()
        self.criar_tabela_anuncio()
        self.criar_tabela_compra()
        self.criar_tabela_compra_anuncio()

    def listar_usuarios(self):
        comando = "SELECT * FROM usuario"
        self.cursor.execute(comando)
        lista_usuarios = self.cursor.fetchall()

        print("\nLista de usuários:")
        for usuario in lista_usuarios:
            print(
                f"ID_usuario: {usuario[0]}, Nome: {usuario[1]} {usuario[2]}, Email: {usuario[3]}"
            )

    def cadastrar_usuario_comum(self, nome, sobrenome, email, senha):
        comando = f'INSERT INTO usuario (nome, sobrenome, email, senha) VALUES ("{nome}", "{sobrenome}", "{email}", "{senha}")'

        self.cursor.execute(comando)
        self.conexao.commit()

    def cadastrar_usuario_vendedor(
        self, cpf_cnpj, data_nascimento, foto_perfil, id_usuario, id_endereco
    ):
        comando = f'INSERT INTO usuario_vendedor (cpf_cnpj, data_nascimento, foto_perfil, id_usuario, id_endereco) VALUES ("{cpf_cnpj}", "{data_nascimento}", "{foto_perfil}", "{id_usuario}", "{id_endereco}")'

        self.cursor.execute(comando)
        self.conexao.commit()

    def editar_usuario_comum(self, ID_usuario, nome, sobrenome, email, senha):
        comando = f'UPDATE usuario SET nome = "{nome}", sobrenome = "{sobrenome}", email = "{email}", senha = "{senha}" WHERE ID_usuario = "{ID_usuario}"'

        self.cursor.execute(comando)
        self.conexao.commit()

    def editar_usuario_vendedor(self, ID_usuario, data_nascimento, foto_perfil):
        comando = f'UPDATE usuario_vendedor SET data_nascimento = "{data_nascimento}", foto_perfil = "{foto_perfil}" WHERE ID_usuario = "{ID_usuario}"'

        self.cursor.execute(comando)
        self.conexao.commit()

    def criar_anuncio(
        self,
        cpf_cnpj_vendedor,
        titulo_anuncio,
        descricao,
        preco,
        foto_produto,
        fabricante,
        quantidade_produto,
        status_aprovacao,
        estado_novo,
    ):
        comando = f'INSERT INTO anuncio (cpf_cnpj, titulo_anuncio, descricao, preco, foto_produto, fabricante, quantidade_produto, status_aprovacao, estado_novo) VALUES ("{cpf_cnpj_vendedor}", "{titulo_anuncio}", "{descricao}", "{preco}", "{foto_produto}", "{fabricante}", "{quantidade_produto}", "{status_aprovacao}", "{estado_novo}")'

        self.cursor.execute(comando)
        self.conexao.commit()

    def editar_anuncio(
        self,
        id_anuncio,
        titulo_anuncio,
        descricao,
        preco,
        foto_produto,
        fabricante,
        quantidade_produto,
        status_aprovacao,
        estado_novo,
    ):

        comando = f'UPDATE anuncio SET titulo_anuncio = "{titulo_anuncio}", descricao = "{descricao}", preco = "{preco}", foto_produto = "{foto_produto}", fabricante = "{fabricante}", quantidade_produto = "{quantidade_produto}", status_aprovacao = "{status_aprovacao}", estado_novo = "{estado_novo}" WHERE id_anuncio = "{id_anuncio}"'

        self.cursor.execute(comando)
        self.conexao.commit()

    def excluir_anuncio(self, id_anuncio):
        comando = f'DELETE FROM anuncio WHERE ID_anuncio = "{id_anuncio}"'

        self.cursor.execute(comando)
        self.conexao.commit()

    def listar_anuncios_vendedor(self, cpf_cnpj):
        comando = f'SELECT * FROM anuncio WHERE cpf_cnpj = "{cpf_cnpj}"'

        self.cursor.execute(comando)
        return self.cursor.fetchall()

    def cadastrar_endereco(
        self, logradouro, numero, complemento, bairro, cidade, UF, cep
    ):
        comando = f'INSERT INTO endereco (logradouro, numero, complemento, bairro, cidade, UF, CEP) VALUES ("{logradouro}", "{numero}", "{complemento}", "{bairro}", "{cidade}", "{UF}", "{cep}")'
        self.cursor.execute(comando)
        self.conexao.commit()

    def editar_endereco(
        self, ID_endereco, logradouro, numero, complemento, bairro, cidade, UF, cep
    ):
        comando = f'UPDATE endereco SET logradouro = "{logradouro}", numero = "{numero}", complemento = "{complemento}", bairro = "{bairro}", cidade = "{cidade}", UF = "{UF}", CEP = "{cep}" WHERE ID_endereco = "{ID_endereco}"'

        self.cursor.execute(comando)
        self.conexao.commit()

    def remover_qtd_produto_estoque(
        self, id_anuncio, quantidade_estoque, quantidade_remocao
    ):
        comando = f'UPDATE anuncio SET quantidade_produto = "{quantidade_estoque - quantidade_remocao}" WHERE id_anuncio = "{id_anuncio}"'
        self.cursor.execute(comando)
        self.conexao.commit()

    def comprar(
        self,
        id_anuncio,
        id_usuario,
        id_endereco,
        carrinho_compras,
        data_compra,
        forma_pagamento,
        modo_envio,
    ):
        valor_total = 0
        for produto in carrinho_compras:
            valor_total = valor_total + (produto[0] * produto[2])
            self.remover_qtd_produto_estoque(produto[0], produto[1], produto[2])

        comando = f'INSERT INTO compra (id_anuncio, id_usuario, id_endereco, valor_total, data_compra, forma_de_pag, modo_envio) VALUES ("{id_anuncio}", "{id_usuario}", "{id_endereco}", "{valor_total}", "{data_compra}", "{forma_pagamento}", "{modo_envio}")'

        self.cursor.execute(comando)
        self.conexao.commit()

    def listar_compras(self, id_usuario):
        comando = f'SELECT * FROM compra WHERE id_usuario = "{id_usuario}"'

        self.cursor.execute(comando)
        return self.cursor.fetchall()
