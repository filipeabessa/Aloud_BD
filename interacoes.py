from anuncios import Anuncios
from compras import Compras
from endereco import Endereco
from carrinho import Carrinho

import datetime


class Interacoes:
    def __init__(self, cursor, conexao, usuario):
        self.usuario = usuario
        self.anuncios = Anuncios(cursor, conexao, usuario)
        self.carrinho = Carrinho(cursor, conexao)
        self.compras = Compras(cursor, conexao, self.carrinho)
        self.endereco = Endereco(cursor, conexao)
        self.sistema_finalizado = False

    def chamar_boas_vindas(self):
        print("Bem-vindo à Aloud! O que você deseja fazer? \n")

    def chamar_despedida(self):
        print("\nObrigado por usar a Aloud!")

    def chamar_menu_inicial(self):
        resposta = input(
            "1 - Cadastrar usuário\n2 - Login\n3 - Buscar produtos/serviços\n"
        )
        if resposta == "1":
            self.usuario.cadastrar_usuario()

        elif resposta == "2":
            self.usuario.login()
            self.carrinho.definir_id_usuario(self.usuario.ID_usuario)

        elif resposta == "3":
            self.anuncios.buscar_anuncios()

    def chamar_menu_vendedor(self):
        resposta = input(
            "1 - Criar anuncio\n2 - Editar Anuncio\n3 - Buscar produtos/serviços\n4 - Visualizar meus anuncios\n5 - Excluir anuncio\n6 - Editar endereco\n7 - Editar usuário\n8 - Visualizar informações de perfil\n9 - Sair\n"
        )
        if resposta == "1":
            self.anuncios.criar_anuncio()

        elif resposta == "2":
            self.anuncios.editar_anuncio(self.usuario.receber_cpf_cnpj())

        elif resposta == "3":
            self.anuncios.buscar_anuncios()
            self.perguntar_quer_adicionar_carrinho()
            self.perguntar_quer_finalizar_compra()

        elif resposta == "4":
            self.anuncios.listar_anuncios_vendedor(self.usuario.receber_cpf_cnpj())

        elif resposta == "5":
            self.anuncios.excluir_anuncio(self.usuario.receber_cpf_cnpj())

        elif resposta == "6":
            self.usuario.editar_endereco()

        elif resposta == "7":
            self.usuario.editar_usuario_vendedor()

        elif resposta == "8":
            self.usuario.visualizar_informacoes_perfil()

        elif resposta == "9":
            self.finalizar_sistema()

    def chamar_menu_usuario_comum(self):
        resposta = input(
            "1 - Buscar produtos/serviços\n2 - Editar usuário\n3 - Visualizar informações de perfil\n4 - Sair\n"
        )
        if resposta == "1":
            self.anuncios.buscar_anuncios()
            self.perguntar_quer_adicionar_carrinho()
            self.perguntar_quer_finalizar_compra()

        elif resposta == "2":
            self.usuario.editar_usuario_comum()

        elif resposta == "3":
            self.usuario.visualizar_informacoes_perfil()

        elif resposta == "4":
            self.finalizar_sistema()

    def perguntar_quer_adicionar_carrinho(self):
        resposta = input("Deseja adicionar algum produto ao carrinho? (s/n) ")
        if resposta == "s":
            id_anuncio = input("Digite o ID do anúncio que deseja comprar: ")
            qtd_produtos = input(
                "Digite a quantidade de produtos do anúncio que deseja comprar: "
            )
            self.carrinho.adicionar_item_carrinho(
                id_anuncio=id_anuncio,
                quantidade=qtd_produtos,
            )

        elif resposta == "n":
            self.chamar_menu_usuario_comum()

    def perguntar_quer_finalizar_compra(self):
        forma_pagamento = input(
            "Digite a forma de pagamento ('p' para paypal e 'm' para mercadopago): "
        )
        if forma_pagamento == "p":
            forma_pagamento = "paypal"
        elif forma_pagamento == "m":
            forma_pagamento = "mercadopago"
        modo_envio = input(
            "Digite o modo de envio ('c' para Correios e 'r' para Rapidão Cometa): "
        )
        if modo_envio == "c":
            modo_envio = "correios"
        elif modo_envio == "r":
            modo_envio = "rapidao"
        self.endereco.cadastrar_endereco()
        id_endereco = self.endereco.receber_id_endereco()
        data_compra = datetime.datetime.now()

        self.compras.comprar(
            id_usuario=self.usuario.ID_usuario,
            carrinho_compras=self.carrinho,
            data_compra=data_compra,
            forma_pagamento=forma_pagamento,
            id_endereco=id_endereco,
            modo_envio=modo_envio,
        )

    def finalizar_sistema(self):
        print("\nObrigado por usar a Aloud!")
        self.sistema_finalizado = True
