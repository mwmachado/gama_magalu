Exercício de RESTful API
---

1. Crie uma aplicação
1. Conecte com um banco de dados
1. Garantir que todo registro possua um id relacionado.
1. Crie pontos de acesso para cada um dos itens abaixo, elas devem responder com JSON e estado HTTP.
   1. Adicionar um item na tabela [POST]
   1. Retornar todos os itens de uma tabela [GET]
   1. Retornar apenas um item pelo id [GET <id>]
   1. Retornar apenas um item pelo nome [POST] {"nome": "nome do item"}
   1. Atualizar um item pelo id [PUT] {"nome": "novo_nome", ...}
   1. Deletar um item pelo id [DELETE <id>]