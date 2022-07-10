class Interacoes:
    def __init__(self, usuarios, anuncios):
        self.usuarios = usuarios
        self.anuncios = anuncios

    def chamar_boas_vindas(self):
        print("Bem-vindo à Aloud! O que você deseja fazer? \n")

    def chamar_despedida(self):
        print("\nObrigado por usar a Aloud!")

    def chamar_menu_inicial(self):
        resposta = input(
            "1 - Cadastrar usuário\n2 - Login\n3 - Buscar produtos/serviços\n"
        )
        if resposta == "1":
            self.usuarios.cadastrar_usuario()

        elif resposta == "2":
            self.usuarios.login()

        elif resposta == "3":
            self.anuncios.buscar_anuncios()

    def chamar_interacaos_vendedor(self):
        resposta = input(
            "1 - Criar anuncio\n2 - Editar Anuncio\n3 - Buscar produtos/serviços\n4 - Visualizar meus anuncios\nExcluir anuncio\n"
        )
        if resposta == "1":
            self.anuncios.criar_anuncio()

        elif resposta == "2":
            self.anuncios.usuarios.editar_anuncio()

        elif resposta == "3":
            self.anuncios.buscar_anuncios()

        elif resposta == "4":
            self.anuncios.listar_anuncios_vendedor(self.usuarios.receber_cpf_cnpj())
