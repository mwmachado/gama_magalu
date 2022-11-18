Documentação e Testes
===

Documentação
---

Docstrings
---


Flask-autodoc
---

- É uma extensão que cria documentação automaticamente para os pontos de acessos.
- A extensão se baseia em rotas, argumentos das funções e docstrings

Passo a passo
---

1. Basta importar o módulo Autodoc "from flask.ext.autodoc import Autodoc"

```python
from flask import Flask
from flask.ext.autodoc import Autodoc
```

1. Criar uma instância utilizando o app flask "auto = Autodoc(app)"

```python
app = Flask(__name__)
auto = Autodoc(app)
```

1. E decorar as funções que deseja documentar com "@auto.doc()"

```python
@app.route('/read/<int:id>')
@auto.doc()
def consulta(id):
    return user_from_database(id)
```

1. Após decorar todas as funções desejadas basta criar uma rota e gerar a documentação
```python
@app.route('/doc')
def documentacao():
	return auto.html()
```

Templates
---

- Caso queira utilizar um template para a documentação, basta passar o argumento template para o método html.

```python
@app.route('/doc')
def documentation():
	return auto.html(
		template="doc_template.html",
		title="título",
		...
	)
```
```html
<html>
	...
	{% if title is defined %}
		{{title}}
	{% endif %}
</html>
```

Generate
---

- Caso queira retornar a documentação em formato json basta utilizar o método "generate" em vez do "html".
- Tal método retorna uma lista de regras em formato de dicionário contendo:
  - **methods:** lista de métodos permitidos.
  - **rule:** url relativa (e.g. /read/int:id).
  - **endpoint:** nome da função (e.g. consulta).
  - **doc:** docstring da função.
  - **args:** argumentos da função (e.g. id).
  - **defaults:** valores padrão para os argumentos.

```python
@app.route('/doc')
def documentation():
	return auto.generate()
```

Conjuntos de documentação
---

- As rotas podem ser separadas em grupos.
- Assim é possível separar documentação pública e privada, externa e interna, etc.
- Também é possível gerar uma parte da documentação em uma rota e outra parte em outra rota.
- Para atribuir a documentação a um conjunto basta adicionar o nome do conjunto como parâmetro ao decorador

```python
@app.route('/admin')
@auto.doc('privado')
def login(usuario, senha):
	...

@app.route('/doc/privado')
def doc_privado():
	return auto.html('privado') 
```

---

Testes
---

- Testes são considerados boas práticas no desenvolvimento de software.
- Testes ajudam a garantir que o programa vai funcionar conforme esperado.
- Testes melhoram a manutenibilidade do código.
- Testes são um bom indicador de qualidade de software.
- Códigos Testáveis são um bom indicador de qualidade de arquitetura de software.


Benefícios
---

- **Mais robustos:** testes ajudam a evitar bugs no aplicativo
- **Debug mais rápido:** com diversos testes unitários fica mais fácil identificar qual parte do código está falhando.
- **Mais profissional:** testes evitam a utilização de prints desnecessário para o programa.
- **Documentação complementar:** alguns testes podem complementar a documentação do seu projeto. Já que o usuário pode verificar os testes e ver quais são as entradas e saídas esperadas.
- **Confiança:** testes podem mostrar quais versões do código funcionam e quais não funcionam.
- **Liberdade para experimentação:** com testes fica mais seguro experimentar novas funcionalidades e ver se elas estão interferindo em alguma outra funcionalidade já testada.

Tipos
---

- Existem 3 tipos de testes: Unitário, teste de integração, teste fim-a-fim.
- Teste Unitários: Testam um funcionalidade (unit) ou parte pequena do programa de maneira isolada.
- Teste de integração: Testam partes grandes do programa, geralmente composto por de várias unidades.
- Teste fim-a-fim: Testa o funcionamento do programa como um todo, geralmente utilizando automatização de clicks e teclados (RPA).
- Para essa aula focaremos nos testes de unidades.
![piramide de testes](https://global-uploads.webflow.com/619e15d781b21202de206fb5/628b0dca3e6eda9219d40a6a_The-Testing-Pyramid-Simplified-for-One-and-All-1280X720%20(1).jpg)

Testes Unitários
---

- Testes unitários utilizam uma abordagem mais simplistas, focando em testar apenas uma funcionalidade por teste em vez de testar o programa todo de uma vez.
- É uma abordagem otimista e com certeza não vai livrar nossos programas de bugs.
- Porém funciona muito bem para garantir que cada funcionalidade está performando conforme esperado mesmo que de maneira isolada.


Flask
---

- flask provê recursos para testar as aplicações.
- O framework utiliza a biblioteca pytest.
- Testes geralmente ficam localizados na pasta "tests"
- Os testes geralmente são funções que começam com o prefixo "test_" em módulos python que com o prefixo "test_"
- Em linhas gerais, tente testar as funções que você escreve e não as bibliotecas que você utiliza, já que geralmente elas já possuem seus próprios testes.

Pytest
---

- Pytest fixtures permite a escrita de código reutilizável entre os testes.
- fixtures transformam um app Flask em um objeto python, onde é possível rodar testes.
- fixtures podem retornar valores e realizar configurações (setup).
- Recomenda-se começar os teste criando um fixture para:
  - app: 
  - cliente: 
![exemplo de código](https://flask.palletsprojects.com/en/2.2.x/testing/#fixtures)

Requisições
---

- Geralmente utilizamos a biblioteca "requests" para testar as rotas da aplicação
- O fixture de cliente pode realizar requests(pedidos) para a aplicação sem a necessidade de possuir um server em andamento.
- O cliente possui os métodos http mais comuns: POST, GET, DELETE, UPDATE, etc.
- Para realizar uma requisição basta chmar o método e a rota a ser testada
- Geralmente utilizamos "response.text" para validar o retorno da rota.
- É possível passar parâmetros para a requisição utilizando o argumento "query_string={...}"
- É possível passar dados de formulário utilizando o argumento "data={...}"
- É possível passar json no corpo da requisição utilizando o argumento "json={...}".
![exemplo de teste de requisição](https://flask.palletsprojects.com/en/2.2.x/testing/#sending-requests-with-the-test-client)


Redirecionamentos
---

- Por padrão, o cliente não segue redirecionamentos.
- Adicionando follow_redirects = True para o request/pedido, o cliente vai continuar até achar uma resposta sem redirecionamento.
- O objeto response.history é uma tupla com todas as respostas recebidas até chegar à última requisição.
- Cada reposta tem um atributo request que contém as informações de cadas pedido utilizado.
![exemplo de teste de redirecionamento](https://flask.palletsprojects.com/en/2.2.x/testing/#following-redirects)

Dicas
---

- assert response.status_code == 200
- assert response.data == html
- assert html in request.data.decode()
- assert response.args.to_dict() == form_get
- assert response.form == form_json
- assert response.json == json
- assert len(response.history) = n_redirects
- assert len(response.request.path) = last_redirect

- Rotas
  - Status 200 para todas as rotas
	- Status 405 para métodos não permitidos
	- Quantidade de redirecionamentos
	- Caminho do último redirecionamento
	- Conteúdo
- Formulários
  - Dados de fomulários via GET
  - Dados de formulários via POST
- APIs
  - Status HTTP
  - Corpo do response
	- Tipos de dados inválidos
- Banco de dados
  - Teste de conexão
	- Teste de cursor
	- Criação de base de testes
	- Existência de tabelas
	- Inserção de dados
	- Consulta de dados
	- Atualização de dados
	- Deleção de dados

Rodando testes
---

- Pytest idenfica nossos testes procurando por arquivos e funções com o prefixo test.
- Pytest espera que estruturas com assert estejam presente nos testes.
- A estrutura assert vai testar uma expressão que retorna verdadeiro ou falso.
- Caso todos os asserts retornem verdadeiro, o teste passa com sucesso.
- Caso algum assert retorne falso, o teste inteiro falha
- Para rodar o pytest na pasta do projeto (e não na pasta teste) basta rodar o comando "python -m pytest"
- Rodar o pytest na pasta do projeto evita que apareçam erros caso o pytest não encontre algum objeto que precise para rodar os testes.
- Para rodar o teste com mais detalhes pode-se utilizar o comando "python -m pytest -v"
- É possível rodar apenas os testes que não rodaram na última vez, basta utilizar o comando "python -m pytest --last-failed"


Referências
---

- https://flask.palletsprojects.com/en/2.2.x/testing/
- https://codethechange.stanford.edu/guides/guide_flask_unit_testing.html

???
---

- Swagger
- OpenAPI
- Code coverage
- Documentação de funções de teste (GIVEN...WHEN...THEN)
  - GIVEN: what are the initial conditions for the test?
	- WHEN: what is ocurring that needs to be tested?
	- THEN: what is the expected response?
	- reference: martin flower