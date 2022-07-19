from database import Database


class Compras:
    def __init__(self, cursor, conexao):
        self.cursor = cursor
        self.conexao = conexao
        self.database = Database(cursor, conexao)

    def __str__(self):
        return "Compras"

    def listar_compras(self):
        pass

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
        self.database.comprar(
            id_anuncio,
            id_usuario,
            id_endereco,
            carrinho_compras,
            data_compra,
            forma_pagamento,
            modo_envio,
        )

    def listar_compras_usuario(self, id_usuario):
        self.database.listar_compras_usuario(id_usuario)

    def cancelar_compra(self):
        pass
