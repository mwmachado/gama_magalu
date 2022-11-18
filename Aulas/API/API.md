---
marp: true
---

# API

---

# Lousa

---

# Componentes

- Cliente (Client, request)
- Garçon (API, response)
- Cozinha (back-end)
- Comida (recurso)
- Prato (front-end)

---

# API

- **API:** **Interface** de Programação de Aplicações (Application Programming Interface).
- Conjunto de rotinas e padrões estabelecidos por uma plicação, para que outras aplicações possam utilizar suas funcionalidades.
- Desenvolvedores expõem APIs das suas aplicações para que elas possam se comunicar com outras de maneira programática.
- Transferência de dados, geralmente, usando protocolo HTTP.
- APIs web podem ser vistas como meio de comunicação entre **clientes** e **servidores** para provimento de **recursos**.

---

# Conceitos

- **Interface:** é qualquer coisa entre um usuário e uma aplicação ou uma aplicação e outra, com o objetivo de fazer eles se comunicarem. Meio de campo (middleware) entre tecnologias. Intermediador para troca de informações.
- **Clientes:** São usuários que desejam acessar informações pela internet. O cliente pode ser uma pessoa ou um sistema capaz de utilizar a API.
- **Recursos:** São informações disponibilizadas por meio de uma aplicação, podem ser imagens, vídeos, texto, números, ou qualquer outro tipo de dado.
- **Servidor:** São máquinas que disponibilizam recurso para clientes, elas controlam acessos, segurança, e a forma como os recursos serão disponibilizados.

---

# REST

---

- **REST:** Transferência de estado representativo (**RE**presentational **S**tate **T**ransfer).
- Aplicações podem precisar se comunicar com outras para desenvolvimento de diversas tarefas.
- REST oferece padrões de segurança, confiança, e comunicação eficiente.
- Define padrões, boas práticas, obrigações para transferência de dados por meio de APIs.
- Os dados são representados como recursos (resources), entidade ou objeto
- Estabelece 6 restrições (constraints) para uma API ser considerada RESTful.

---

# RESTful API

---

- É uma interface utilizada por dois sistemas para trocar informações de modo seguro pela internet.
- É considerada RESTful uma API que aplica os 6 padrões REST.
- Tanto REST API quanto RESTful API podem ser utilizados para representar tais APIs.

---

# 6 Principios

---

# Princípio 1

1. **Interface uniforme (Uniform Interface):** Estabelece 4 padrões para o formato da transferência de recursos.
   1. **Identificação dos Recursos:** Recursos devem possuir um identificador único e uniforme.
   1. **Representação dos Recursos:** As respostas devem conter metadados para que o cliente consiga modificar ou deletar o recurso caso necessário.
   1. **Mensagens auto-descritivas:** As respostas devem possuir metadados e informações auto-descritivas sobre como o cliente pode utilizar ou processar essa informação.
   1. **Hypermedia:** As respostas podem conter links para que os clientes possam complementar as informações recebidas ou sobre outros recursos relacionados.

---

# Princípio 2-4

2. **Cliente-Servidor (Client-Server):** Cliente e servidor devem estar separados, provendo uma separação do cliente e do armazenamento de dados (servidor), e facilitando a portabiblidade e reutilização do servidor (e.g. mobile e web).
1. **Sem estado (Stateless):** Toda requisição (request) deverá conter todas as informações necessárias para o servidor processar e retornar uma resposta (response). (e.g. sessão do usuário não pode ser armazenada no servidor, deverá ser enviada com cada requisição).
1. **Cacheable:** Respostas devem dizer explicitamente se aquela requisição pode ser guardada (cacheada) pelo cliente ou não.

---

# Princípio 5-6

5. **Sistemas em camadas (Layered System):** O cliente deve sempre acessar um ponto de acesso(endpoint, URI), sem precisar saber da complexidade ou quais outras camadas o serviço vai precisar utilizar para responder à requisição.
1. **Código sobre demanda (Code on demand)** - Opicional: O servidor pode opcionalmente enviar para o cliente algum script para que ele execute (e.g. Javascript).

---

# Boas Práticas

- Antigamente utilizava-se XML, porém hoje o padrão é JSON.
- Utilize verbos HTTP corretos nas requisições.
- Nomeie os pontos de acessos com substantivos em vez de verbo.
- Decida se os pontos de acesso serão escritos no plural ou singular, e mantenha o padrão.
- Sempre envie uma resposta para o cliente (JSON).
- Sempre envie status HTTPs no retorno da requisição.

---

# Referencias

https://restfulapi.net/
https://aws.amazon.com/what-is/restful-api/