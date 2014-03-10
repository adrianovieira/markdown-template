---
date: 10 de março de 2014
tipo_artigo: Artigo técnico de Infraestrutura de TIC
title: Crie Conteúdo; não leiaute
abstract: Esse artigo busca mostrar um método prático para que autor atente-se basicamente ao conteúdo (texto) de sua obra, usando padrões sintáticos de formatação em ***markdown* estendido** para escreve-lo e deixando as tarefas de criar apresentação ou formatação de leiaute e conversão para PDF ou ODT por exemplo automatizadas com ferramentas especialistas como a ***pandoc*** descrita aqui.
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

Descrever as básicas dentre as diversificadas formatações sintáticas de textos em ***markdown* estendido** [@wikipediaMarkdown] e converter o conteúdo para diversos formatos como por exemplo PDF, ODT e HTML usando a ferramenta especialista ***Pandoc*** [@pandocDocConv2014].

Benefícios e/ou recomendações
=============================

Esse poderá ser considerado como uma refeência rápida aos alguns recursos que a ferramenta de conversão *Pandoc* possui para se escrever conteúdos de textos como relatórios, artigos ou apresentações (*slides*).

A *Pandoc* possui sintaxe específica para algumas formatações, sendo necessário possuir instalada essa ferramenta para realizar a conversão para os diversos formatos pretendidos.

Introdução
==========

Existem hoje em dia diversas soluções que o mercado nomeia como ferramentas de produtividade de escritório em que o usuário (autor) precisará, na maioria das vezes, preocupar-se com a apresentação final de seu relatório, memorando, ofício, artigo, livro etc.

Formatações Sintáticas de Textos
================================

Apresenta tópicos com uso de textos com marcação “*markdown* estendido e *Pandoc*”.

Formatações Básicas
-------------------

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

Outro exemplo:

~~~ {.markdown}
	Lorem ipsum^[Filler text (<http://en.wikipedia.org/wiki/Lorem_ipsum>)]
~~~
Resultado: Lorem ipsum^[Filler text (<http://en.wikipedia.org/wiki/Lorem_ipsum>)]

Inserir e destacar código fonte
-------------------------------

Para inserir código ou bloco pré formatado usar ```~~~```, como a seguir:

~~~ {.markdown}
   ~~~ 
   Bloco inserido sem formatação usando `~~~`
   ~~~
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


Fórmulas matemáticas
--------------------
Recurso que poderá ser obtido usando LaTeX^[LaTeX – A document preparation system (<http://www.latex-project.org>)]

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

	[^1]: (texto aparece na nota de rodapé, mas sem efeitro final) [@Herrero2013]
	[^2]: [@daringfireballMDBasics]

~~~




Conclusão
=========

Apresenta a conclusão do artigo.

Referências
===========

[^1]: (texto aparece na nota de rodapé, mas sem efeitro final) [@Herrero2013]
[^2]: [@daringfireballMDBasics]

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
  URL: 'http://johnmacfarlane.net/pandoc/getting-started.html'
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

- id: Herrero2013
  title: "Instant Markdown"
  author:
  - family: Herrero
    given: Arturo
  container-title: Text formatting
  volume: 1
  URL: 'http://johnmacfarlane.net/pandoc/getting-started.html'
  publisher: Packt Publishing
  page: 16, 26
  translator:
  - family: Knows (?)
    given: Who
  type: book
  issued:
    year: 2013
    month: 8

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
