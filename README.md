# Projeto BD

#### Grupo:
* Emanuely Lima;
* Filipe Bessa;
* Mariana Loreto;
* Juscelino Alves;

#### Minimundo:
A ALOUD é uma plataforma de compra e venda de instrumentos musicais, e equipamentos relacionados à música e áudio. Ao entrar no site ALOUD, um Usuário pode buscar vários produtos por meio dos Anúncios.

Cada Anúncio é criado por um "Usuário Vendedor", que é referenciado por uma chave estrangeira (cpf_cnpj) e possui um Código único (ID_Anuncio), Título, Descrição, Foto, Preço, Fabricante, Quantidade em Estoque, Estado (novo/usado) e Status de aprovação (pendente, aprovado e negado). Não há limite de anúncios, mas dois anúncios não podem ter o mesmo código. 
Após a inserção na plataforma, o anúncio passará por uma avaliação dos administradores da plataforma, para posterior publicação em caso de aprovação (status_aprovacao = "aprovado"). 

Um Usuário é armazenado por um Código único (ID_Usuario), Nome, Sobrenome, Email e Senha. Sendo um "Usuário Vendedor" uma generalização do Usuário, com necessária inclusão de CPF/CNPJ como chave primária, Data de Nascimento, Endereço e Foto de Perfil.
Cada "Usuário Vendedor" é identificado por um CPF/CNPJ. Não existem dois usuários com o mesmo email, nem com o mesmo CPF/CNPJ, assim como também não existem dois produtos com o mesmo código. Um usuário pode comprar vários produtos.

O processo de Compra é armazenado com um Código único (ID_Compra), o Código do usuário (ID_Usuario), a Forma de Pagamento selecionada (Intermediários), o Valor Total da Compra, o Endereço de Entrega (ID_Endereco), Data da Compra, e Modo de Envio (serviço de entrega). Cada pedido recebe um código de identificação único e uma data é registrada quando a compra é confirmada pelo Intermediário.


#### TODO:

* Compras:
  * Listar compras;
  * Comprar;
  * Cancelar compra;
* Loop do menu:
* INNER JOIN:
  * Criar função de visualizar perfil, que juntaria as tabelas de usuário e usuário vendedor;
