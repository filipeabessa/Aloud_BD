from database import Database


class Compras:
    def __init__(self, cursor, conexao, carrinho_compras):
        self.cursor = cursor
        self.conexao = conexao
        self.database = Database(cursor, conexao)

        self.carrinho_compras = carrinho_compras

    def __str__(self):
        return "Compras"

    def comprar(
        self,
        id_usuario,
        id_endereco,
        carrinho_compras,
        data_compra,
        forma_pagamento,
        modo_envio,
    ):
        valor_total = carrinho_compras.receber_valor_total_carrinho()
        self.database.comprar(
            id_usuario,
            id_endereco,
            carrinho_compras.ID_carrinho,
            valor_total,
            data_compra,
            forma_pagamento,
            modo_envio,
        )

    def listar_compras_usuario(self, id_usuario):
        self.database.listar_compras_usuario(id_usuario)

    def cancelar_compra(self):
        pass
