---
marp: true
---

NoSQL
===

---

# Contexto (Lousa)

- Banco de dados Relacional
- ACID
- OLAP vs OLTP
- Cópia somente leitura
- Limitações do banco de dados relacional
- Schema rígido vs flexível
- Sistemas de banco de dados distribuídos
- Alta disponibilidade vs Tolerancia a falhas (HA vs FT)

---

# Contexto (Lousa)

- dados estruturados vs não estruturados
- 3Vs do big data
- Teorema CAP
- CAP vs ACID
- Escalabilidade horizontal vs vertical
- Modelos de banco de dados NoSQL
  - Colunar
  - Grafo
  - Chave-valor
  - Documento

---

# NoSQL

- O termo “NoSQL’’ é utilizado para designar os banco de dados não relacionais
- Podemos entender como bancos de dados NoSQL (Not Only SQL) simplesmente aqueles que não usam somente o SQL em suas estruturas.
- Temos BDs NoSQL de várias formas e arquiteturas diferentes, não significando, obviamente, que todos eles possuem arquiteturas similares, como é o caso dos BDs relacionais SQL.
- Principal diferença entre os bancos de dados relacionais e NoSQL é que o segundo permite maior **velocidade, flexibilidade e escalabilidade ao armazenar e acessar dados não estruturados**.
---

# Relacional vs NoSQL

- Determinados tipos de problemas são melhor resolvidos com BD relacional, enquanto outros tipos de problemas são melhor resolvidos com BD NoSQL.
- **BD Relacional:** Dados bem estruturados e amarrados (aplicações gerenciais)
- **BD NoSQL:** Documentos com todas as informações correlacionadas à principal (Estruturas de LOGs, aplicações analíticas, para construções de modelos de inteligência de negócio).
- Não veio para substituir o relacional. Veio para ser uma alternativa

---

# Tipos de NoSQL

- Os bancos de dados NoSQL são divididos em 4 tipos:
  - Colunar
  - Grafo
  - Chave-valor
  - Documento

---

### Colunar

- **Modelo Colunas:** Banco de dados faz armazenamento em colunas de uma tabela. Esse esquema é o perfeito oposto dos bancos relacionais, que armazenam conjuntos de dados em uma única linha
- **Exemplos:** Hbase e Cassandra

---

### Grafo

- **Modelo Grafos:** Armazena dados na forma de grafo. Isto é, aqui os dados são dispostos no formato de arcos conectados por arestas. Podemos definir como um conjunto de linhas conectadas por vértices também. 
- **Exemplos:** Neo4J

---

### Chave-Valor

- **Modelo Chave-Valor:** Temos um banco que é formado por conjuntos de chaves, que por sua vez são acompanhados de valores como tabelas hash. A estrutura chave-valor também é bem flexível e própria para armazenamento de big data.
- **Exemplos:** REDIS e MemcacheD

---

### Documento

- **Modelo Documento:** Dados são “documentos”. É o esquema de armazenamento do MongoDB, por exemplo. Esse modelo é altamente flexível e não carece de colunas pré montadas, como é o caso do Cassandra.
- Especialmente eficiente para tratar dados não estruturados, já que uma única coleção pode contar com grupos de dados (documentos) de diversos formatos diferentes.
- **Exemplo:** MongoDB

---

# Teorema CAP

- Quando começamos a estudar aplicações escaláveis e sistemas distribuídos, um dos tópicos que mais aparece é sobre o Teorema CAP (ou Teorema de Brewer), que fala basicamente sobre as escolhas que você precisa tomar para obter um determinado resultado no seu sistema, olhando para consistência, disponibilidade e partições tolerantes a falha.
- Vem do inglês: Consistency (Consistência), Availability (Disponibilidade) e Partition Tolerance (Partição tolerante a falhas)
- Afirma que, em um sistema com distribuição de dados, é impossível obter simultaneamente mais de duas das três garantias

---

## CAP

- **Consistência:** A ideia da consistência é que todos as partições do sistema tenham a informação mais atualizada possível. (todos estão vendo a mesma informação?)
- **Disponibilidade:** Garantir que as partições do sistema estejam sempre o mais acessíveis possível. (Todos estão conseguindo acessar?)
- **Tolerância à Falhas:** Sistemas distribuídos não estão protegidos contra falhas de rede, portanto, a partição sempre deve ser tolerada. (Caso ocorra uma falha continua funcionando?)

---

## Consistência vs Disponibilidade

- Ao escolher consistência em relação à disponibilidade, o sistema retornará um erro ou um tempo limite se informações específicas não puderem ser necessariamente atualizadas devido à sua partilha na rede.
- Ao escolher disponibilidade sobre consistência, o sistema sempre processará a consulta e tentará retornar a versão disponível mais recente da informação, mesmo que não possa garantir que ela esteja atualizada devido às partições.

---

# Bancos NoSQL

https://db-engines.com/en/ranking

---

## Mongo DB

- Líder de mercado dos bancos de dados NoSQL.
- Possui features muito úteis para produção, como: 
  - Replicação
  - Indexação
  - Balanceamento de carga.
- Armazena dados em formato JSON (JavaScript Object Notation)
- É Open Source, o que contribui muito para a evolução da tecnologia.

---

## Amazon DynamoDB

- Disponível na AWS (Amazon Web Services)
- Totalmente cloud
- Viabilização de grande desempenho confiável e em escala

- Amazon confirma que a latência e fica sempre abaixo de 10 milissegundos.
- Possui recursos valiosos de segurança, baseados em cache de memória, backup e restauração de dados

---

## Cassandra

- Originalmente desenvolvido no Facebook
- Atualmente mantido pela Apache Foundation, assim como o HBase.

- Muito otimizado para clusters, especialmente por funcionar sem mestres.
- Possui mecanismos distribuídos, o que otimiza ainda mais a operação com clusters.
- Orientação por coluna, o que torna a latência bem menor em algumas pesquisas.

---

## Redis

- Dados são armazenados na forma de chave-valor e na memória do Redis, o que o torna rápido e flexível
- Banco NoSQL mais famoso do tipo chave-valor
- Possui baixíssima latência. 
- Fácil de usar e muito rápido

---

## HBase

- Banco de dados open source, orientado a colunas e distribuído.
- Atualmente, Spotify e Facebook são algumas das grandes corporações que utilizam esse modelo de armazenamento
- Foi formatado a partir do BigTable do Google e também é escrito em Java.
- Fácil integração com o MapReduce (Hadoop)
- MapReduce é uma ferramenta do framework Apache Hadoop, uma das principais plataformas para tratamento de big data
- Pesquisa de dados que oferece uma resposta rápida. Transforma terabytes em milissegundos

---