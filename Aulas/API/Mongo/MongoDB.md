---
marp: true
---

MongoDB
===

---

# MongoDB

- É um banco de dados NoSQL orientado a documentos de código aberto e multiplataforma (Windows, Linux, Mac, Cloud)
- É popular na criação de aplicativos rápidos e escaláveis que lidam com grandes quantidades de dados.
- Permite que o usuário armazene dados em um formato não relacional

---

# Documentos 

- Ao contrário dos bancos de dados relacionais tradicionais, onde os dados são armazenados em tabelas, o MongoDB usa o formato JSON para armazenar dados em documentos.
- No formato JSON, os dados são formatados em pares de valores-chave, nos quais os nomes e valores dos campos são separados por dois pontos e encapsulados entre chaves.
- Devido ao seu esquema flexível, o MongoDB é uma escolha natural para desenvolvedores que precisam construir aplicativos rápidos e altamente escaláveis que podem processar grandes volumes de dados.
- Faz uso de coleções (tabelas), cada uma com vários documentos (registro).

---

# Instalando MongoDB

- MongoDB não está nos repositórios oficiais do ubuntu 22.04 até o momento, para evitar problemas de instalação utilizaremos o mongodb na nuvem (Atlas)

---

## Atlas (Cloud)

1. https://www.mongodb.<colecao>.com/cloud/atlas/register
1. Sign up with google
1. Projects > new project > create project
1. Database > build a database > free Shared > Google Cloud (SP) > Cluster Name > Create Cluster
1. Security Quickstart > Username and Password > My Local Environment > Add My Current IP Address > Finish and Close
1. Deployment Database > database connect > Connect using VS Code > copiar string de conexão
1. VS Code > Database Client > NoSQL > connect > Use connection string > colar string de conexão > + Connect

---

# Comandos

---

# Apresentar

- show dbs: Apresenta todas as bases de dados existentes no servidor
- use <database>: Cria um novo banco de dados e aponta a conexão para ele. Porém, só o armazena efetivamente se houver dados dentro dele.

---

# Criar (CREATE)

- db.createCollection("<colecao>"): Criação uma coleção no BD Selecionado
- db.getCollectionNames(): retorna o nome de todas as coleções da base

---

# Apagar (DROP)

- db.dropDatabase(): Apaga a base selecionada.
- db.drop("<colecao>"): Apaga uma determinada coleção da base selecionada.

---

# Inserir (INSERT)
- db.<colecao>.insertOne(<registro>): Insere documento dentro de uma coleção no MongoDB
- db.<colecao>.insertMany([<registro>, <registro>,...]): Insere vários documentos em uma única coleção

---

# Consultar (SELECT)

- db.<colecao>.findOne(): retorna o primeiro documento encontrado na coleção.
- db.<colecao>.find(): retorna todos os documentos de uma coleção.
- <consulta>.pretty(): Ajusta a saída de uma consulta para facilitar a leitura

---

# Atualizar (UPDATE)

```mongodb
db.<colecao>.updateOne(
    <condição>,
    {$set:
        {"<campo1>":<valor1>},
        {"<campo2>":<valor2>},
        ...
    }
)
```
ou

```mongodb
db.<colecao>.updateOne(
    <condição>,
    {$set:
        {"<campo1>":<valor1>},
        {"<campo2>":<valor2>},
        ...
    }
)
```

---

# Deletar (DELETE)

```mongodb
db.<colecao>.deleteOne("<objectId>")
db.<colecao>.deleteMany("<objectId>")
```

ou 

```mongodb
db.<colecao>.deleteOne(<condição>)
db.<colecao>.deleteMany(<condição>)
```

---

# Operadores

---

## Relacionais

|Operador SQL|Operador Mongo|Nome|Operação|
|:---:|:---:|---|---|
|=|$eq|**Eq**uals|É igual a|
|>|$gt|**G**reater **T**han|É maior que|
|>=|$gte|**G**reater **T**han or **E**qual|É maior ou igual a|
|<|$lt|**L**ess **T**han|É menor que|
|<=|$lte|**L**ess **T**han or **E**qual|É menor ou igual a|
|!=/<>|$ne|**N**ot **E**qual|É diferente de|

---

### Exemplo

db.<colecao>.find({"<campo>": {<operador>: "<valor>"}}):   Resgata documentos da <colecao> que respeitem a condição informada.

---

# Lógicos

- AND
```mongodb
db.<colecao>.find({
    $and:[
        "<campo1>":<operador1>,
        "<campo2>":<operador2>
    ]
})
```

- OR

```mongodb
db.<colecao>.find({
    $or:[
        "<campo1>":<operador1>,
        "<campo2>":<operador2>
    ]
})
```

---

# Pesquisa Textual

db.<colecao>.createIndex({"<campo>": "<tipo_index>"}): criar um índice de texto no campo que se deseja realizar a busca textual.
db.<colecao>.find({\$text:{$search: "<termo>"}}):Realiza busca em todos os documentos que possuírem o termo buscado.

---

# Pesquisa Textual

```
db.<colecao>.createIndex({"<campo>": "<tipo_index>"})

db.<colecao>.find({$text:{$search: "<termo>"}})
```

---

# Ordenação (ORDER BY)

Ordem crescente
```mongodb
<consulta>.sort({"<coluna>": 1})
```

ou

Ordem decrescente
```mongodb
<consulta>.sort({"<coluna>": -1})
```

---

# References

https://www.cherryservers.com/blog/
https://hevodata.com/blog/