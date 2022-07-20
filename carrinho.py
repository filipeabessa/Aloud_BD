from database import Database


class Carrinho:
    def __init__(self, cursor, conexao, usuario):
        self.database = Database(self.usuario.cursor, self.usuario.conexao)
        self.cursor = cursor
        self.conexao = conexao

        self.valor_total = 0
        self.carrinho = []
        self.usuario = usuario

    def __str__(self):
        return "Carrinho"

    def adicionar_produto(self, id_anuncio, preco_anuncio, quantidade, id_carrinho):
        valor_total_item = preco_anuncio * quantidade
        self.carrinho.append((id_anuncio, quantidade, preco_anuncio))
        self.valor_total += valor_total_item

        self.database.adicionar_item_carrinho(
            id_anuncio, id_carrinho, quantidade, valor_total_item
        )

    def receber_valor_total(self):
        return self.valor_total
