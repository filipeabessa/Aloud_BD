class Interacoes:
    def __init__(self, usuarios):
        self.usuarios = usuarios

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
