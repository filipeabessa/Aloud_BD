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

    def listar_usuarios(self):
        comando = "SELECT * FROM usuario"
        self.cursor.execute(comando)
        lista_usuarios = self.cursor.fetchall()

        print("\nLista de usuários:")
        for usuario in lista_usuarios:
            print(
                f"ID_usuario: {usuario[0]}, Nome: {usuario[1]} {usuario[2]}, Email: {usuario[3]}"
            )

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
