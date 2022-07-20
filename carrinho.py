from database import Database


class Carrinho:
    def __init__(self, cursor, conexao):
        self.cursor = cursor
        self.conexao = conexao
        self.database = Database(self.cursor, self.conexao)

        self.ID_usuario = 0
        self.ID_carrinho = 0

    def __str__(self):
        return "Carrinho"

    def adicionar_item_carrinho(self, id_anuncio, quantidade):
        ID_carrinho = self.receber_id_carrinho()
        preco_anuncio = float(self.database.pegar_preco_anuncio(id_anuncio))
        valor_total_item = preco_anuncio * int(quantidade)

        self.atualizar_valor_total_carrinho(ID_carrinho, valor_total_item)

        self.database.adicionar_item_carrinho(
            id_anuncio=id_anuncio,
            id_carrinho=ID_carrinho,
            quantidade=quantidade,
            valor_total_item=valor_total_item,
        )

    def criar_carrinho(self):
        self.database.criar_carrinho(self.ID_usuario)

    def receber_valor_total_carrinho(self):
        valor_total = self.database.pegar_valor_total_carrinho(self.ID_usuario)
        return valor_total

    def receber_id_carrinho(self):
        self.id_carrinho = self.database.pegar_id_carrinho(self.ID_usuario)
        return self.id_carrinho

    def atualizar_valor_total_carrinho(self, ID_carrinho, valor_a_atualizar):
        valor_total_atual_carrinho = self.receber_valor_total_carrinho()

        valor_atualizado_carrinho = valor_total_atual_carrinho + valor_a_atualizar
        self.database.atualizar_valor_total_carrinho(
            ID_carrinho, valor_atualizado_carrinho
        )

    def definir_id_usuario(self, id_usuario):
        self.ID_usuario = id_usuario
