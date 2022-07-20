from database import Database


class Carrinho:
    def __init__(self, cursor, conexao, id_usuario):
        self.cursor = cursor
        self.conexao = conexao
        self.database = Database(self.cursor, self.conexao)

        self.valor_total = 0
        self.carrinho = []
        self.ID_usuario = id_usuario

    def __str__(self):
        return "Carrinho"

    def adicionar_item_carrinho(self, id_anuncio, quantidade, id_carrinho):
        # TODO receber preco anuncio do banco
        preco_anuncio = 0
        valor_total_item = preco_anuncio * int(quantidade)
        self.carrinho.append((id_anuncio, quantidade, preco_anuncio))
        self.valor_total += valor_total_item

        self.database.adicionar_item_carrinho(
            id_anuncio=id_anuncio,
            id_carrinho=id_carrinho,
            quantidade=quantidade,
            valor_total_item=valor_total_item,
        )

    def criar_carrinho(self):
        id_carrinho_criado = self.database.criar_carrinho(self.ID_usuario)
        return id_carrinho_criado[0][0]

    def receber_valor_total(self):
        return self.valor_total
