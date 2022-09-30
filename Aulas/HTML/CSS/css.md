CSS
---

- CSS significa Cascading Style Sheets
- CSS é a linguagem utilizada para mudar o estilo de documentos HTML
- CSS controla características como posição, cor, estilo, etc.
- CSS se preocupa em **como** os elementos serão apresentados, enquanto que o HTML se preocupa **em o que** será apresentado.
- Pode ser utilizado em múltiplas páginas de uma vez
- Sintaxe seleção de tag
```css
tag_html{
    chave1: valor1;
    chave2: valor2;
}
```

- Sintaxe seleção de id
```css
#tag_id{
    chave1: valor1;
    chave2: valor2;
}
```

- Sintaxe seleção de classe
```css
.tag_class{
    chave1: valor1;
    chave2: valor2;
}
```

- Sintaxe seleção de elemento e classe
```css
tag_html.tag_class{
    chave1: valor1;
    chave2: valor2;
}
```
- Sintaxe seleção de todos os elementos
```css
*{
    chave1: valor1;
    chave2: valor2;
}
```
- Sintaxe seleção de lista de elementos
```css
tag_html1, tag_html2, tag_html3{
    chave1: valor1;
    chave2: valor2;
}
```
- Elementos html podem receber mais de uma classe
```html
<tag_html class="class1 classe2">
```
Tipos de inclusão de CSS
- CSS Externo
```css
/* comentários */
/* arquivo style.css */
*{
    chave1: valor1;
    chave2: valor2;
}
```
```html
<!-- arquivo style.css-->
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="style.css">
    </head>
</html>
```
- CSS Interno
```html
<!DOCTYPE html>
<html>
    <head>
    <style>
    * {
        chave1: valor1;
        chave2: valor2;
    }
    </style>
    </head>
</html>
```
- CSS direto no elemento (inline)
```html
<!DOCTYPE html>
<html>
    <head>
    </head>
    <body>
        <p style="chave:valor;"> parágrafo </p>
    </body>
</html>
```
- No caso de mais de uma especificação o navegador utiliza o que aparece por último
- é possível utilizar a propriedade !important para ignorar a ordem de especificação
- Falar sobre herança

# Background

```
background-color: Define uma cor como fundo
background-image: Define a imagem de fundo
    - url("caminho_da_imagem")
background-repeat: Controla a repetição da imagem
    - Apenas horizontal-> repeat-x
    - Apenas vertical-> repeat-y
    - Sem repetição-> no-repeat
background-attachment: Define se a imagem vai seguir a rolagem da página ou não
    - Segue a rolagem -> fixed
    - Não segue a rolagem -> scroll
background-position:
    - right, top, left, bottom
```

# Display

```
display: block, inline, inline-block, none
    - block: um bloco em baixo do outro
    - inline: um do lado do outro, ocupa apenas o espaço necessário
    - inline-block: um do lado do outro, porém permite especificar altura e largura
    - none: Geralmente utilizado por funções javascript para remover ou mostrar elementos na tela.
position: static, relative, fixed, absolute, sticky
    - static: posicionamento padrão
    - relative: posicionamento relativo a posição padrão
    - fixed: posicionamento relativo a tela
    - absolute: posicionamento relacionado ao elemento mais próximo, geralmente utilizado para sobreposição
    - sticky: se mover junto a barra de rolagem quando chegar a determinada posição.
    - left, top, bottom, right
float: left, right, none, inherit
    - left: se posiciona na direta do container
    - right: se posiciona na esquerda do container
    - none: comportamento padrão
    - inherit: herda o valor do parent
visibility: hidden, visible
overflow: visible, hidden, scroll, auto
    - visible: renderiza para fora do elemento
    - hidden: esconde o que foi renderizado
    - scroll: cria barra de rolagem
    - auto: cria barra de rolagem quando necessário

- display none vs visibility hidden
- float left vs display inline-block
  - display: tem sua altura alterada pelos irmãos
```

# Texto

```
color:
    - RGB -> rgb(0-255, 0-255, 0-255, 0-1)
    - Hexadecimal -> #ffffff
    - Pré-definidas -> https://www.w3schools.com/colors/colors_names.asp
opacity: 0-1
text-align: right, left, center, justify
font-family: nome_da_fonte
font-size: tamanho
```

# Links

```
/* essa ordem tem que ser respeitada */
a:link -> link não visitado, padrão
a:visited -> link visitado
a:hover -> quando o mouse passa por cima
a:active -> no momento do clique
color: cor
background-color: cor
text-decoration: none, underline
padding:
text-align:
```

# box Model

```
height: tamanho ou porcentagem
width: tamanho ou porcentagem
padding: tamanho ou porcentagemfont-size:
border: https://www.w3schools.com/css/css_border.asp
border-style: top, right, bottom, left
border-width: px, cm, thin, medium, thick
border-color:
border-radius: xp
margin: tamanho ou auto(centraliza o container horizontalmente)
max-width: tamanho ou porcentagem
```

# Listas

```
list-style-type:
    - ol -> upper-roman, lower-alpha, none
    - ul -> circle, square, none
list-style-image: url('caminho_do_ícone')
list-style-position: inside, outside
```

# Tabelas

```
border:
width:
height:
text-align:
vertical-align: top, bottom, middle
padding:
```

Referência
---

https://www.w3schools.com/cssref/default.asp
