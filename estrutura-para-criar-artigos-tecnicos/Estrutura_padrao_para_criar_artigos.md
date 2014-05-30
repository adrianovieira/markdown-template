---
remark: metadados para a ser usado pelo parser de conversão para pdf
date: 28 de fevereiro de 2014
tipo_artigo: Artigo técnico de Infraestrutura de TIC
title: Estrutura padrão para criar artigos técnicos
abstract: 'Apresenta a estrutura padrão para artigos a serem produzidos para publicação interna com uso de textos com marcação “*Markdown/Pandoc*”.'
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
- Git
- SCM
- Template
...
 
Introdução
==========

O desenvolvimento de artigos tem buscado valorizar o conhecimento das equipes nas tecnologias, processos e serviços gerenciados pela DIT. Além disso, também visa a divulgação dos trabalhos realizados, implantação de novas funcionalidades ou tecnologias etc. 

Assim, o que tem acontecido (desde fevereiro/2014) é que na SUPS se tem produzido um conjunto de artigos. Foi proposto e cada departamento tem publicado mensalmente dois ou três artigos técnicos.

Desafios
========

Haver uma forma padronizada para a estrutura e leiaute dos artigos a serem produzidos.

Benefícios e/ou recomendações
=============================

Considera-se que uma estrutura padrão facilite a autoria do artigo, bem como a leitura por oferecer a identificação dos elementos e tópicos do corpo do texto.

Estrutura padrão para criar artigos
===================================

\setstretch{1}
```texinfo
---
remark: metadados para a ser usado pelo parser de conversão para pdf
date: 28 de fevereiro de 2014
tipo_artigo: Artigo técnico de Infraestrutura de TIC
title: Estrutura padrão para criar artigos técnicos
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
- Pandoc
- Markdown
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
produzidos com uso de textos com marcação “Markdown/Pandoc”.

Conclusão
=========

Apresente a conclusão do artigo.

Referências
===========

Lista referências bibliográficas, matérias na intranet, ferramentas
internas etc.

Caso no desenvolvimento do texto tenha sido usado o recurso de "citações"
(ex: @IDCitacao ou variações) não será necessário listar, pois o "Pandoc"
identificará e listará com base nos metadados de referências criados no 
fim do arquivo.

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

>*"Também está disponível na **Ond@**^[***Ond@*** (<http://onda.dataprev.gov.br>)] e, por ser mais dinâmica, deve ser a referência mais atual de estrutura a ser usada."* - @ID-estruturaVieira.

Métodos para construção até a publicação
========================================

O leitor irá encontrar nos artigos alguns tópicos base e uma apresentação final que será comum a todos os artigos produzidos. Para alcançar essa homogeneidade os artigos são produzidos com técnicas e tecnologias simplificadas. Sendo que arte final é produzida por processo automatizado. 

Para tanto, é sugerido ao autor que preocupe-se em criar o conteúdo de seu artigo escrevendo-o em "texto puro" com uso algumas técnicas de marcação para estruturar e destacar o texto escrito. Nesse sentido, usaria padrões sintáticos de formatação em "*markdown estendido*"^[*Pandoc* (<http://johnmacfarlane.net/pandoc>)], evitando uso de ferramentas de escritório (ex: MS Word&trade;/LibreOffice&trade;). 

Use *Markdown* estendido
------------------------

Na comunidade "Portal de Tecnologia" na ***Ond@*** há artigo como referência inicial para uso de técnicas em *Markdown/Pandoc*^[@ID-pandocRefVieira] que é a ferramenta atualmente utilizada para conversão de conteúdos nesse padrão para outros (aqui utilizamos *PDF*).

Use Git-SCM
-----------

Com o intuito de agilizar, facilitar contribuições na criação do artigo e o processo automatizado para gerar a arte final é indicado que o conteúdo e respectivas imagens sejam mantidos no *Git*^[*Git* institucional (<http://www-git/>)] institucional.

Esse ambiente usa o sistema de controle de fontes *Git-SCM*^[Git-SCM (<http://www.git-scm.com/>)] e com camada *web Gitlab*^[Gitlab (<https://www.gitlab.com/>)].

*Template* para a arte final
----------------------------

O uso de *template* busca facilitar a conversão de textos escritos em *Markdown/Pandoc* (arquivo salvo com extenção: ***.md***) para outros formatos (*PDF*, *ODT* etc). Inicialmente está previsto e funcional a conversão apenas para *PDF*.

No *Git* institucional há o repositório *markdown-template*^[*markdown-template* (<http://www-git/documentos/markdown-template/>)] que contem o *template* e rotinas (*scripts*) que automatizam a conversão e geração da arte final em *PDF*.

Nesse repositório também há um descritivo^[*Wiki* (<http://www-git/documentos/markdown-template/wikis/home>)] que mostra como esse *template* pode ser usado.

Publique artigos
----------------

Os artigos são escritos por funcionários da Dataprev e podem ser realizados por um ou mais autores, conforme tema e abordagem definidos. O processo de aprovação passa pelo chefe imediato na área de lotação do autor e, ainda, por revisão final pela assessoria SUPS ou DIT.

O tema e/ou assunto dos artigos a serem escritos podem ser propostos voluntariamente e aquele que sentir-se motivado manifesta-se ao chefe imediato que define quando os artigos serão publicados. Outro viés é o chefe definir o assunto de interesse conforme planejamento interno do setor, o plano de ações, PDTI ou visão para onde a empresa está caminhando.

### A ***Ond@***

Considerando um canal para troca de experiências, a publicação na rede social ***Ond@*** facilita o acesso ao artigo pelos técnicos da área especialista do assunto, bem como alcançar um público que se interessa e/ou domine o tema tratado.

Nessa linha tem-se percebido a facilidade de disseminação dos trabalhos realizados e ainda um local de fácil acesso e publicação das atividades desenvolvidas na empresa. Com isso, mais contribuições podem ser dadas e melhorias podem ser implementadas ao dia a dia de trabalho.

Conclusão
=========



Referências
===========

---
remark: referências usadas nesse artigo
references:
- id: ID-estruturaVieira
  title: "Estrutura padrão para criar artigos técnicos"
  author:
  - family: Vieira
    given: Adriano dos Santos
  URL: 'https://onda.byyou.com/artigos?1=1&space=portaldetecnologia-community&app_ByYouSocialArticle_articleId=1608757133'
  accessed:
    month: 05
    year: 2014
  publisher: Dataprev
  type: webpage
  issued:
    year: 2014
    month: 02
- id: ID-pandocRefVieira
  title: "Crie Conteúdo, não leiaute; padrões sintáticos de formatação *markdown* estendido & *Pandoc*"
  author:
  - family: Vieira
    given: Adriano dos Santos
  URL: 'https://onda.byyou.com/artigos?app_ByYouSocialArticle_articleId=1644605620&space=portaldetecnologia-community'
  accessed:
    month: 5
    year: 2014
  publisher: Dataprev
  type: article
  issued:
    year: 2014
    month: 3
...
