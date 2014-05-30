---
remark: metadados para a ser usado pelo parser de conversão para pdf
date: 28 de fevereiro de 2014
tipo_artigo: Artigo técnico de Infraestrutura de TIC
title: Estrutura padrão para criar artigos
abstract: 'Apresenta a estrutura padrão para artigos a serem produzidos para publicação interna com uso de textos com marcação “Markdown/Pandoc” (arquivo salvo com extenção: .md).'
author:
- affiliation: SUPS
  name: Adriano dos Santos Vieira
responsibility:
- affiliation: SUPS
  name: Anderson Gourlart
diretoria: 'Diretoria de Infraestrutura de TIC - DIT'
superintendencia: 'Superintendência de Planejamento e Suporte de TIC - SUPS'
tags:
- Tech0xA
- Markdown
- Pandoc
- Artigos
...
 
Introdução
==========

Desafios
========

Haver uma forma padronizada para a estrutura dos artigos a serem produzidos.

Benefícios e/ou recomendações
=============================



Estrutura padrão para criar artigos
===================================

\setstretch{1}
```texinfo
---
remark: metadados para a ser usado pelo parser de conversão para pdf
date: 28 de fevereiro de 2014
tipo_artigo: Artigo técnico de Infraestrutura de TIC
title: Estrutura padrão para artigos
abstract: Resumo identificando ou destacando ponto importantes do artigo. 
Traz o pontencial leitor a se sentir atraído a ler o todo.
author:
- affiliation: SUPS
  name: Adriano dos Santos Vieira
- affiliation: NNN
  name: Autor NNN
responsibility:
- affiliation: SUPS
  name: Anderson Gourlart
diretoria: 'Diretoria de Infraestrutura de TIC - DIT'
superintendencia: 'Superintendência de Planejamento e Suporte de TIC - SUPS'
departamento: 'Departamento NNN - SIGLA'
tags:
- Tech0xA      <= sempre colocar essa!
- Markdown
- Pandoc
- Artigos
...

Introdução
==========

Descreve e contextualiza o leitor do problema que o artigo irá abordar e 
buscar resolver.

Desafios
========

Descreve desafios e/ou problemas que o artigo irá abordar e buscar
resolver.

Benefícios e/ou recomendações
=============================

Descreva os principais ganhos propostos pelo artigo, como melhoria de 
indicadores, processo de trabalho, etc.

Tópicos do artigo
=================

…. desenvolvimento do texto do artigo …

Subtópicos do artigo
--------------------

…. desenvolvimento do texto do subtópico do artigo …

### Subtópicos do artigo

…. desenvolvimento do texto do subtópico do artigo …

#### Subtópicos do artigo

…. desenvolvimento do texto do subtópico do artigo …

##### Subtópicos do artigo

Apresenta sub(sub)tópicos de estrutura padrão para artigos a serem 
produzidos com uso de textos com marcação “markdown/pandoc”.

Conclusão
=========

Apresente a conclusão do artigo.

Referências
===========

Lista referências bibliográficas, matérias na intranet, ferramentas
internas etc.

Caso tenha sido usado o recurso de "citações" (ex: @IDCitacao ou variações)
não será necessário listar, pois o "Pandoc" identificará e listará.

---
remark: metadados com alguns dados para listar referências bibliográficas.
Use quantos identificadores (ID) necessitar para listar as diferentes
referências usadas no artigo
references:
- id: ID-Citação
  title: "Título da referência usada"
  author:
  - family: Sobrenome
    given: Nome parcial (sem o Sobrenome)
  container-title: area de conhecimento ou assunto
  URL: 'http://www.endereço-na-web.com'
  accessed:
    day: dia de acesso
    month: mês de acesso
    year: ano de acesso
  publisher: Editor responsável
  page: páginas usadas
  type: tipo de referencia usada (book, article, article-newspaper,
  webpage, thesis etc)
  volume: volume da referência usada
  issue: número da edição ou tiragem
  issued:
    year: ano publicação
    month: mês de publicação
- id: IDCitacao
  title: "Estrutura para criar artigos técnicos"
  author:
  - family: Vieira
    given: Adriano dos Santos
  URL: 'https://onda.byyou.com/artigos?1=1&space=portaldetecnologia-commun
  ity&app_ByYouSocialArticle_articleId=1608757133'
  accessed:
    month: 02
    year: 2014
  publisher: Dataprev
  type: webpage
  issued:
    year: 2014
    month: 02
...
```
\setstretch{1.5}

>*"Também está disponível na Ond@ e, por ser mais dinâmica, deve ser a referência mais atual de estrutura a ser usada."* - @ID-ondaVieira.

Conclusão
=========



Referências
===========

---
remark: referências usadas no artigo
references:
- id: ID-ondaVieira
  title: "Estrutura para criar artigos técnicos"
  author:
  - family: Vieira
    given: Adriano dos Santos
  URL: 'https://onda.byyou.com/artigos?1=1&space=portaldetecnologia-community&app_ByYouSocialArticle_articleId=1608757133'
  accessed:
    month: 02
    year: 2014
  publisher: Dataprev
  type: webpage
  issued:
    year: 2014
    month: 02
...
