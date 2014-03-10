---
date: 10 de março de 2014
tipo_artigo: Artigo técnico de Infraestrutura de TIC
title: Crie Conteúdo; não leiaute
abstract: Esse artigo busca mostrar um método prático para que autores atentem-se basicamente ao desenvolvimento do conteúdo (texto) de sua obra. Para tanto, usaria padrões sintáticos de formatação em ***markdown* estendido** para escreve-lo e deixaria tarefas de criar apresentação final ou formatação de leiaute e conversão, para PDF ou ODT por exemplo, automatizadas com ferramentas especialistas como a ***pandoc*** descrita aqui.
author:
- affiliation: SUPS
  name: Adriano dos Santos Vieira
responsibility:
- affiliation: SUPS
  name: Anderson Gourlart
diretoria: 'Diretoria de Infraestrutura de TIC - DIT'
superintendencia: 'Superintendência de Planejamento e Suporte de TIC - SUPS'
tags:
- Markdown
- Pandoc
- Padrões
- Textos
- Produtividade
- Escritório
...

Desafios
========
Descrever as básicas dentre as diversificadas formatações sintáticas de textos em ***markdown* estendido** [@wikipediaMarkdown] e converter o conteúdo de artigos para  formatos como por exemplo PDF^[Portable Document Format (<http://en.wikipedia.org/wiki/Portable_Document_Format>)] e ODF^[OpenDocument (<http://en.wikipedia.org/wiki/Odf>)] usando a ferramenta especialista ***Pandoc*** [@pandocDocConv2014].

Benefícios e/ou recomendações
=============================
Esse artigo poderá ser considerado como uma referência rápida a alguns dos recursos que a ferramenta de conversão multidirecional *Pandoc* implementa, para o que podemos chamar de ***markdown* estendido**, e possibilita a conversão do conteúdo em relatórios, artigos ou apresentações (*slides*).

A *Pandoc* possui sintaxe específica para algumas formatações, sendo necessário possuir instalada essa ferramenta para realizar a conversão, a partir de ***markdown* estendido**, para os diversos formatos pretendidos e suportados.

Introdução
==========
Existem hoje em dia diversas soluções que o mercado nomeia como ferramentas de produtividade de escritório em que o usuário (autor) precisará, na maioria das vezes, preocupar-se com a apresentação final de seu relatório, memorando, ofício, artigo, livro etc.

Boa parte destas ferramentas implementam um modo visual de escrever e ver o resultado imediatamente. Entretanto, é necessário que o autor (ou redator) preocupe-se com regras de formatação de parágrafos, títulos, leiaute, posicionamento de images e vários outros detalhes do tipo. Esse tipo de situação muitas vezes faz com que se perca muito tempo acertando estes detalhes e prejudicando o desenvolvimento do conteúdo.

Com vistas a facilitar o autor a se preocupar basicamente com o conteúdo no desenvolvimento de documentos técnicos com uso sintaxe básica de formatações e simples de ser usada foi criada a especificação *Markdown*^[@daringfireballMDBasics]. Por ser uma especificação simplificada e devido a necessidades de recursos de formatações mais avançadas foram surgindo outras nomeadas como "*markdown* estendido"^[@wikipediaMarkdown] e implementadas por diversos fornecedores/implementadores, sendo os mais conhecidos GFM^[GitHub Flavored Markdown (<https://help.github.com/articles/github-flavored-markdown>)], MultiMarkdown^[MultiMarkdown (<http://en.wikipedia.org/wiki/MultiMarkdown>)], Pandoc’s markdown^[Pandoc’s markdown (<http://johnmacfarlane.net/pandoc/README.html#pandocs-markdown>)]. Esse último (*Pandoc*) denomina-se como:

>*"uma biblioteca *Haskell*^[Haskell (<http://www.haskell.org>)] para conversão de uma formatação de marcação para outra, bem como uma ferramenta que usa essa bibliblioteca"*.
- @pandocDocConv2014
  
É a *Pandoc* que esse artigo irá tratar e apresentar alguns de seus recursos para construção e formatação sintática textos, facilitando gerar o documento e sua arte ou apresentação final considerando também padrões reconhecidos de mercado como a norma ABNT NBR 6023:2002^[@NBR-6023_2002].

Esse documento foi totalmente escrito e formatado usando  marcação *markdown* estendido e *Pandoc*.

Formatações Sintáticas de Textos
================================
Apresenta tópicos com uso de textos com marcação “*markdown* estendido e *Pandoc*”.

Formatações Básicas
-------------------

### Estilos de tópicos

Os estilos de tópicos são como os usados nesse artigo com em:

~~~ {.markdown}
Introdução
==========
~~~
Resultado: Título de nível "0".

~~~ {.markdown}
Formatações Básicas
-------------------
~~~
Resultado: Título de nível "1".

~~~ {.markdown}
### Estilos de tópicos
~~~
Resultado: Título de nível "2".

Observação: Níveis acima de "2" são desaconcelhados para conversões para PDF devido a limitações do LaTeX^[LaTeX – A document preparation system (<http://www.latex-project.org>)]

### Listas com marcadores ou numeração

Lista com marcadores

~~~ {.markdown}
- Item 1
    - Item 1.1
        - Item 1.1.1
        - Item 1.1.2
            - Item 1.1.2.1
- Item 2
- Item 3
~~~
Resultado:  

- Item 1
    - Item 1.1
        - Item 1.1.1
        - Item 1.1.2
            - Item 1.1.2.1
- Item 2
- Item 3

Exemplo para criar lista numerada:

~~~ {.markdown}
1. Item 1
    - item não numerado
        - item não numerado
2. Item 2
3. Item 3
~~~
Resultado:

1. Item 1
    - item não numerado
        - item não numerado
2. Item 2
3. Item 3


### Formatação de fonte

- Negrito: uso do símbolo "**"  no início e fim do texto

~~~ {.markdown}
	Lorem **ipsum dolor** sit amet
~~~
Resultado: Lorem **ipsum dolor** sit amet

- Itálico: uso do símbolo "*"  no início e fim do texto

~~~ {.markdown}
	Lorem *ipsum dolor* sit amet
~~~
Resultado: Lorem *ipsum dolor* sit amet

- tachado: uso do símbolo "~~" no início e fim do texto

~~~ {.markdown}
	Lorem ipsum ~~dolor~~ sit amet
~~~
Resultado: Lorem ipsum ~~dolor~~ sit amet


- Combinados: os símbolos podem ser combinados de diferentes maneiras

~~~ {.markdown}
	Lorem ***ipsum ~~dolor~~*** sit amet
~~~
Resultado: Lorem ***ipsum ~~dolor~~*** sit amet

Outro exemplo:

~~~ {.markdown}
	*L*orem **I**psum dolor sit a***me***t
~~~

Resultado: *L*orem **I**psum dolor sit a***me***t

- Formatação incorreta

~~~ {.markdown}
	Lorem ***ipsum ~~dolor*** sit~~ amet
~~~
Resultado inesperado: Lorem ***ipsum ~~dolor*** sit~~ amet

### Notas de rodapé

Notas de rodapé são numeradas automáticamente e também poderão conter referências a sites/páginas de internet. 

Exemplo:

~~~ {.markdown}
	Lorem ipsum^[Filler text]
~~~
Resultado: Lorem ipsum^[Filler text]

Exemplo com link para web:

~~~ {.markdown}
	Lorem ipsum^[Filler text (<http://en.wikipedia.org/wiki/Lorem_ipsum>)]
~~~
Resultado: Lorem ipsum^[Filler text (<http://en.wikipedia.org/wiki/Lorem_ipsum>)]

Inserir tabelas
---------------

Tabelas simples com linhas únicas

~~~ {.markdown}
ID  material            Cab N
--- ------------------- ------------
1   Lorem ipsum         Filler text
2   Duis aute           Filler text
3   Conteúdo da Célula  Outro conteúdo
~~~
Resultado:

ID  material            Cab N
--- ------------------- ------------
1   Lorem ipsum         Filler text
2   Duis aute           Filler text
3   Conteúdo da Célula  Outro conteúdo

Forma para inserir tabelas com múltiplas linhas numa mesma célula

~~~ {.markdown}
+----------------+--------------------------------+---------------------------+
|**Cab 1**       |**Cab 2**                       |**Cab N**                  |
+================+================================+===========================+
|Conetúdo celula |Conetúdo celula                 |Conetúdo celula            |
+----------------+--------------------------------+---------------------------+
|Lorem ipsum     |Lorem ipsum dolor sit amet,     |Conetúdo celula            |
|                |consectetur adipisicing elit,   |                           |
|                |sed do eiusmod tempor incididunt|                           |
|                |ut labore et dolore magna       |                           |
|                |aliqua.                         |                           |
+----------------+--------------------------------+---------------------------+
~~~

+----------------+--------------------------------+---------------------------+
|**Cab 1**       |**Cab 2**                       |**Cab N **                 |
+================+================================+===========================+
|Conetúdo celula |Conetúdo celula                 |Conetúdo celula            |
+----------------+--------------------------------+---------------------------+
|Lorem ipsum     |Lorem ipsum dolor sit amet,     |Conetúdo celula            |
|                |consectetur adipisicing elit,   |                           |
|                |sed do eiusmod tempor incididunt|                           |
|                |ut labore et dolore magna       |                           |
|                |aliqua.                         |                           |
+----------------+--------------------------------+---------------------------+

Inserir imagens
---------------

A inserção de imagem segue a seguinte sintaxe:

~~~ {.markdown}
![Legenda da imagem](path/para/imagem.jpg|png)
~~~

Exemplo:

~~~ {.markdown}
![Revista Dataprev Resultados nº9, ano 5](imagens/revista_resultados_ano5_n9.jpg)
~~~
Resultado:

![Revista Dataprev Resultados nº9, ano 5](imagens/revista_resultados_ano5_n9.jpg)

Inserir endereços internet
--------------------------

A inserção de endereços internet segue a seguinte sintaxe:

~~~ {.markdown}
[Nome do site](http://www.enderecodosite.br)
~~~

Exemplo para link web:

~~~ {.markdown}
[ProjectLibre community](http://www.projectlibre.org)
~~~
Resultado:

[ProjectLibre community](http://www.projectlibre.org)

Inserir e destacar código fonte
-------------------------------

Para inserir código ou bloco pré formatado usar o delimitador ```~~~``` ou \```, como a seguir:

~~~ {.markdown}
   Usando o delimitador ~~~ como nesse bloco
~~~

e em conjunto com esse inserção, para destacar o código fonte ou blocos deve-se especificar o tipo do texto a ser destacado.

Por exemplo, para destacar código python, com linhas numeradas:

~~~ {.markdown}
   ~~~ {.python .numberLines}
   import random   
   number = random.randint(1, 20)
   def greet(name):
       print 'Hello,', name, '!'
   print greet('World')
   print (number)
   ~~~
~~~

Resultado:

~~~ {.python .numberLines}
import random   
number = random.randint(1, 20)
def greet(name):
    print 'Hello,', name, '!'
print greet('World')
print (number)
~~~

ou 

```markdown
   Usando o delimitador ``` como nesse bloco
```

~~~ {.markdown}
   ```python
   import random   
   number = random.randint(1, 20)
   def greet(name):
       print 'Hello,', name, '!'
   print greet('World')
   print (number)
   ```
~~~

Resultado:

```python
import random   
number = random.randint(1, 20)
def greet(name):
    print 'Hello,', name, '!'
print greet('World')
print (number)
```



Fórmulas matemáticas
--------------------
Recurso que poderá ser obtido usando LaTeX^[LaTeX – A document preparation system (<http://www.latex-project.org>)]

Fórmulas na mesma linha do texto:

~~~ {.markdown}
 a equação deverá estar entre "$" como em $\omega = d\phi / dt$.
~~~
Resultado: a equação deverá estar entre "\$" como em $\omega = d\phi / dt$.

Fórmulas em sua própria linha, a equação deverá estar entre dois "\$":

~~~ {.markdown}
$$CCA = \frac{((PRA * ICRA) + (PAA * ICAA) + (PS * ICS))}{PRA + PAA + PS}$$
~~~
Resultado:
$$CCA = \frac{((PRA * ICRA) + (PAA * ICAA) + (PS * ICS))}{PRA + PAA + PS}$$

Referências a tópicos
---------------------

São permitidas referências a tópicos (ou subtópicos) do próprio texto.

~~~ {.markdown}
	vá para [Duis aute irure](#duis-aute-irure)
~~~

Resultado: vá para [Duis aute irure](#duis-aute-irure)

#### Lorem ipsum

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

#### Duis aute irure

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.

~~~ {.markdown}
	volte para [Lorem ipsum](#lorem-ipsum)
~~~
Resultado: volte para [Lorem ipsum](#lorem-ipsum)


Citações
--------

### Citações de textos de outros autores

Para realizar citações uso o símbolo ">", repetindo-o ">>" para fique mais "compatado" no parágrafo.

~~~ {.markdown}
>*"Lorem ipsum dolor sit amet, consectetur adipisicing elit, 
 sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
 Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
 nisi ut aliquip ex ea commodo consequat".* 
 
>>*"Duis aute irure dolor in 
 reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
 pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
 culpa qui officia deserunt mollit anim id est laborum".* 
~~~

Resultado:

>*"Lorem ipsum dolor sit amet, consectetur adipisicing elit, 
 sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
 Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
 nisi ut aliquip ex ea commodo consequat".* 
 
>>*"Duis aute irure dolor in 
 reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
 pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
 culpa qui officia deserunt mollit anim id est laborum".* 

### Citações de autores/referências bibliográficas

É recomendado que as citações sigam as instruções da norma ABNT NBR 6023:2002 [@NBR-6023_2002] que trata como realizar e elaborar referências bibliográficas.

As citações poderão ser realizadas de diferentes formas:

~~~ {.markdown}
-   [@inexistente] incorre em resultado com "(???)"
-   @inexistente também incorre em resultado com "(???)"
-   Em uma nota de rodapé.[^1]
-   Outra nota de rodapé.[^2]
-   *"Lorem ipsum dolor sit amet, consectetur adipisicing elit, 
 sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
 Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
 nisi ut aliquip ex ea commodo consequat".* - @Loremipsum1960
-   Há ainda várias outras formas que poderão ser consultadas em
    [@pandocDocConv2014 Citations ou pandoc-citeproc].

~~~

Resultado:

-   [@inexistente] incorre em resultado com "(???)"
-   @inexistente também incorre em resultado com "(???)"
-   Em uma nota de rodapé.[^1]
-   Outra nota de rodapé.[^2]
-   *"Lorem ipsum dolor sit amet, consectetur adipisicing elit, 
 sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
 Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
 nisi ut aliquip ex ea commodo consequat".* - @Loremipsum1960
-   Há ainda várias outras formas que poderão ser consultadas em [@pandocDocConv2014 Citations ou pandoc-citeproc].

---


### Citações realizadas no tópico "Referências"

Recursos para que se faça citações como notas de rodapé e listas de referências (ver [Referências](#referências))

~~~ {.markdown}
Referências
===========
[^1]: (texto aparece na nota de rodapé, mas sem efeito final) [@pandocDocConv2014]
[^2]: [@daringfireballMDBasics]
~~~

[^3]: [@QuickMarkdownExample2013]



Conclusão
=========

Apresenta a conclusão do artigo.

Referências
===========
[^1]: (texto aparece na nota de rodapé, mas sem efeito final) [@pandocDocConv2014]
[^2]: [@QuickMarkdownExample2013]

---
references:
- id: wikipediaMarkdown
  title: "Markdown extensions"
  translator: S.l.
  booktitle: "Wikipedia: The Free Encyclopedia"
  container-title: Text formatting
  URL: 'http://en.wikipedia.org/wiki/Markdown_extensions'
  accessed:
    day: 22
    month: 2
    year: 2014
  publisher: Wikimedia
  type: entry-encyclopedia
  year: 2014

- id: pandocDocConv2014
  title: "Pandoc a universal document converter"
  translator: S.l.
  author:
  - family: MacFarlane
    given: John
  container-title: Text converter
  URL: 'http://johnmacfarlane.net/pandoc/index.html'
  accessed:
    day: 22
    month: 2
    year: 2014
  publisher: Wikipedia
  type: webpage
  issued:
    year: 2014
    month: 2

- id: Loremipsum1960
  title: "Lorem ipsum"
  translator: S.l.
  author:
  - family: Community
    given: Wikipedia
  container-title: Filler text
  URL: 'http://en.wikipedia.org/wiki/Lorem_ipsum'
  accessed:
    day: 22
    month: 2
    year: 2014
  publisher: Wikipedia 
  type: entry-encyclopedia
  issued:
    year: 1960

- id: daringfireballMDBasics
  title: "Getting the gist of Markdown's formatting syntax"
  author:
  - family: Gruber
    given: John
  container-title: Text formatting
  URL: 'https://daringfireball.net/projects/markdown/basics'
  accessed:
    day: 22
    month: 2
    year: 2014
  issue: 4
  publisher: The Daring Fireball Company LLC.
  type: article
  issued:
    year: 2004
    month: 12

- id: QuickMarkdownExample2013
  title: "Quick Markdown Example"
  translator: S.l.
  author:
  - family: Gabriele
    given: John
  container-title: Text converter
  URL: 'http://www.unexpected-vortices.com/sw/gouda/quick-markdown-example.html'
  accessed:
    day: 22
    month: 2
    year: 2014
  publisher: Unexpected Vortices 
  type: webpage
  issued:
    year: 2013

- id: NBR-6023_2002
  title: "Informação e documentação - Referências - Elaboração"
  volume: "ABNT NBR 6023:2002"
  publisher: ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS
  history: ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS
  locators: Rio de Janeiro
  extra: Rio de Janeiro
  type: book
  year: 2002
  issue: ABNT

...
