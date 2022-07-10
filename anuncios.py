class Anuncio:
    def __init__(self, cursor, conexao):
        self.cursor = cursor
        self.conexao = conexao

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

        comando = f'UPDATE anuncio SET "titulo_anuncio = "{titulo_anuncio}", descricao = "{descricao}", preco = "{preco}", foto_produto = "{foto_produto}", fabricante = "{fabricante}", quantidade_produto = "{quantidade_produto}", status_aprovacao = "{status_aprovacao}", estado_novo = "{estado_novo}" WHERE id_anuncio = "{id_anuncio}"'

        self.cursor.execute(comando)
        self.conexao.commit()
