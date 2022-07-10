class Anuncio:
    def __init__(self, cursor, conexao, database, usuarios):
        self.cursor = cursor
        self.conexao = conexao
        self.database = database
        self.usuarios = usuarios

    def criar_anuncio(self):
        cpf_cnpj = self.usuarios.cpf_cnpj
        titulo_anuncio = input("Digite o título do anúncio: ")
        descricao = input("Digite a descrição do anúncio: ")
        preco = input("Digite o preço do anúncio: ")
        foto_produto = input("Digite o link da foto do anúncio: ")
        fabricante = input("Digite o fabricante do produto: ")
        quantidade_produto = input("Digite a quantidade do produto: ")
        estado_novo = input(
            'Digite o estado do produto ("1" para novo e "2" para usado): '
        )
        status_aprovacao = "Aprovado"

        self.database.criar_anuncio(
            cpf_cnpj,
            titulo_anuncio,
            descricao,
            preco,
            foto_produto,
            fabricante,
            quantidade_produto,
            status_aprovacao,
            estado_novo,
        )

    def editar_anuncio(self, cpf_cnpj):
        self.listar_anuncios_vendedor_id_titulo(cpf_cnpj)

        id_anuncio = input("Digite o ID do anúncio que deseja editar: ")
        titulo_anuncio = input("Digite o título do anúncio: ")
        descricao = input("Digite a descrição do anúncio: ")
        preco = input("Digite o preço do anúncio: ")
        foto_produto = input("Digite o link da foto do anúncio: ")
        fabricante = input("Digite o fabricante do produto: ")
        quantidade_produto = input("Digite a quantidade do produto: ")
        status_aprovacao = "Aprovado"
        estado_novo = input(
            'Digite o estado do produto ("1" para novo e "2" para usado): '
        )

        self.database.editar_anuncio(
            id_anuncio,
            titulo_anuncio,
            descricao,
            preco,
            foto_produto,
            fabricante,
            quantidade_produto,
            status_aprovacao,
            estado_novo,
        )

    def excluir_anuncio(self, cpf_cnpj):
        self.listar_anuncios_vendedor_id_titulo(cpf_cnpj)

        id_anuncio = input("Digite o ID do anúncio que deseja excluir: ")
        self.database.excluir_anuncio(id_anuncio)

    def formatar_estado_novo_string(self, estado_novo):
        if estado_novo == 1:
            return "Novo"
        else:
            return "Usado"

    def buscar_anuncios(self, palavra_chave=""):
        if palavra_chave == "":
            comando = "SELECT * FROM anuncio"
        else:
            comando = (
                f'SELECT * FROM anuncio WHERE titulo_anuncio LIKE "%{palavra_chave}%"'
            )

        self.cursor.execute(comando)
        anuncios = self.cursor.fetchall()
        for anuncio in anuncios:
            print(
                f"ID: {anuncio[0]}\nTítulo: {anuncio[2]}\nPreço: {anuncio[4]}\nQuantidade: {anuncio[7]}"
            )
            print(f"Estado: {self.formatar_estado_novo_string(anuncio[9])}")
            print("\n\n\n")
        return

    def listar_anuncios_vendedor(self, cpf_cnpj):
        print("Seus anúncios:\n")
        lista_anuncios = self.database.listar_anuncios_vendedor(cpf_cnpj)

        for anuncio in lista_anuncios:
            print(
                f"ID: {anuncio[0]}\nTítulo: {anuncio[2]}\nPreço: {anuncio[4]}\nQuantidade: {anuncio[7]}"
            )
            print(f"Estado: {self.formatar_estado_novo_string(anuncio[9])}")
            print("\n\n\n")

    def listar_anuncios_vendedor_id_titulo(self, cpf_cnpj):
        print("Seus anúncios:\n")
        lista_anuncios = self.database.listar_anuncios_vendedor(cpf_cnpj)

        for anuncio in lista_anuncios:
            print(f"ID: {anuncio[0]}\nTítulo: {anuncio[2]}")
            print("\n\n")
