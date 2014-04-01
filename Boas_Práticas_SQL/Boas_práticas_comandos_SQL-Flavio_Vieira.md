---
date: 31 de março de 2014
tipo_artigo: Artigo técnico de Infraestrutura de TIC
title: Boas práticas na construção de comandos SQL
abstract: Neste artigo, serão destacadas um grupo de boas práticas na escrita de comandos SQL em SGBD Oracle&trade;.
author:
- affiliation: DEST/DSBD
  name: Flávio Vieira
responsibility:
- affiliation: DEST
  name: Diogo Costa Martins Pizaneschi
diretoria: 'Diretoria de Infraestrutura de TIC - DIT'
superintendencia: 'Superintendência de Planejamento e Suporte de TIC - SUPS'
departamento: 'Departamento de Suporte de TIC - DEST'
tags:
- SQL
- 'SGBD *Oracle*'
- Desempenho
...

Desafios
========

Uma das possíveis causas de lentidão no acesso aos bancos Oracle&trade; é a má utilização dos comandos SQL, principalmente em sua escrita.

Benefícios e/ou recomendações
=============================

Este artigo visa mostrar alguns cuidados que podem ser tomados para evitar a construção de SQLs que possam vir a se tornar problemas em ambientes de SGBD Oracle.


Introdução
==========

Podemos dividir a execução de um comando SQL no SGBD Oracle basicamente em quatro fases:

* **Parse**: Durante esta fase o Oracle verifica a se o comando está escrito corretamente seguindo as regras de semântica do SQL e se os objetos envolvidos no comando existem e estão disponíveis. No final desta fase, o Oracle verifica se esta consulta já possui um plano de execução criado, caso não possua o plano é criado e armazenado na memória do Oracle visando futuro reaproveitamento.
* **Bind**: Assim que o plano é criado ou reaproveitado o Oracle recebe do programa cliente o conteúdo dos valores das variáveis "bind" ( normalmente representadas por :1,:2 ou ? ) para que o comando possa ser executado.
* **Execute**: Nesta fase, o Oracle executa o comando utilizando o plano escolhido com os valores informados, retornando erros se ocorrer. Caso tudo esteja de acordo, o SGBD constrói o "Result Set". Caso o comando executado não seja um SELECT a execução termina nesta fase.
* **Fetch** - Nesta fase o SGBD retorna os resultados da consulta para o solicitante.
 
O texto do SQL pode influenciar positivamente ou negativamente as fases  todas estas quatro fases.

Práticas que afetam a fase de Parse
===================================

Conforme dito anteriormente, durante a fase de "Parse" o SGBD Oracle cria o plano de execução dos SQLs. Como esta tarefa é muito complexa, pode se tornar muito lenta e o SGBD tenta reaproveitar planos já existentes, visando agilizar a execução das consultas. Os planos de execução já executados são guardados em memória e a identificação dos planos que podem ser reaproveitados é realizada por comparação do texto do SQL a ser executado.

Na primeira vez que um SQL é submetido ao banco é atribuído um valor HASH criado a partir de seu texto, (Ou seja, comandos idênticos tem o mesmo identificador HASH.) seu plano é criado e armazenado junto com seu identificador HASH.

A partir daí cada novo SQL submetido ao banco tem seu código HASH calculado e comparado com os valores armazenados em memória. Caso esta busca retorne algum plano este é reaproveitado evitando a criação de um novo.

Utilização de variáveis bind (comandos idênticos)
-------------------------------------------------

Para que o banco possa aumentar o reaproveitamento de planos de execução a utilização de variáveis de ligação (bind) no texto dos SQLs é imprescindível. 

Abaixo segue um exemplo.

Os comandos abaixo são diferentes, gerando planos com  IDs diferentes:

```sql
 SELECT ID FROM TABELA WHERE ID = 1;

 SELECT ID FROM TABELA WHERE ID = 2;
```

Eles poderiam ser reconstruidos da forma abaixo:

```sql
 SELECT ID FROM TABELA WHERE ID = ?; 
```

Este último comando, uma vez executado teria seu plano reaproveitado a cada nova execução, mesmo com o conteúdo da variável ? diferente.

Além das vantagens da fase de Parse, variáveis de ligação facilitam a validação de tipo de dados dos valores de entrada fornecidos dinamicamente e evitam os riscos de vulnerabilidade de segurança e integridade existentes quando se constrói uma instrução SQL por concatenação de strings (Select Dinâmico).

Práticas que afetam a fase de Execute
=====================================

O tempo da fase de "execute" pode ser influenciado principalmente pos SQLs que forcem o Oracle a tomar decisões erradas durante a fase anterior, quando ele escolhe o plano de execução da consulta.

Evite a utilização da tática "Balão" na codificação de SQL
----------------------------------------------------------

A tática balão ocorre quando o desenvolvedor escolhe escrever um único SQL complexo que contem toda ou a maior parte da regra de negócio em seu texto, no lugar de quebrar a consulta em consultas menores. Além do texto complexo dificultar o processo de otimização, a regra de negócio  deve ser tratado na camada de aplicação. 

Operadores
----------


Alguns operadores são mais performáticos do que outros. Segue uma pequena listagem por ordem crescente de performance de alguns operadores:
```sql
    =
    >, >=, <, <=
    LIKE
    <>
```

Ou seja, utilizar o operador “ = “ é mais performático do que usar o operador “ <> “.

Evite Utilizar o Operador NOT
-----------------------------

Em vez de utilizarmos a querie:
```sql
    WHERE NOT column_name > 5
```
Podemos reescrever a mesma da seguinte forma::
```sql
    WHERE column_name <= 5
```
Ambas produzirão o mesmo resultado, mas o segundo exemplo produzirá um resultado bem mais performático.



Uso de LIKE
-----------

O operador LIKE é utilizado normalmente em  SQLs para realizar buscas em campos alfanuméricos procurando por trechos de caracteres.
```sql
    1: SELECT ID FROM PESSOAS WHERE NOME LIKE '%JOAO DA SILVA%';
```
Este tipo de operador deve ser evitado, mas quando for necessário deve-se dar preferência a utilização do % somente no meio ou no final da string de comparação:
```sql
    2: SELECT ID FROM PESSOAS WHERE NOME LIKE 'JOAO DA SILVA%';
```
Nos exemplos acima `2` tem probabilidade maior de executar mais rápido, pois se o campo NOME possuir índice, provavelmente este será utilizado pelo banco para executar o comando. No caso de `1` o SGBD não consegue utilizar nenhum índice criado em NOME para executar a consulta.

Uso de funções na cláusula WHERE de uma consulta
------------------------------------------------

No momento em que decidir como resolver uma consulta, o otimizador do Oracle tenta utilizar índices já existentes nas tabelas envolvidas desde que certas condições sejam seguidas. Uma delas é a não utilização de funções sobre os campos da tabela na cláusula WHERE de um comando SQL. 

Por exemplo:

Dado a tabela A que possui os campos ID NUMBER(5), NOME VARCHAR2(30), STATUS NUMBER(1), NASC DATE e que possui um índice no campo STATUS. Se realizarmos a consulta abaixo provavelmente este índice não será utilizado provocando varredura total na tabela e tempo de resposta alto.
```sql
    Select ID,NOME from A where to_char(STATUS) = '1';
```
Podemos reescrever a consulta para:
```sql
    Select ID,NOME from A where STATUS = TO_NUMBER('1');
```
>"Ou seja, tente sempre utilizar a conversão no valor de teste e não na coluna com a qual ele será comparado."


COUNT x EXISTS
--------------

Para testes de existência é sempre mais eficiente utilizar EXISTS do que COUNT. Quando se utiliza o COUNT o banco de dados não sabe que se está fazendo um teste de existência e continua pesquisando todas as linhas qualificadas. Já utilizando EXISTS, o banco de dados sabe que é um teste de existência e interrompe a pesquisa quando encontra a primeira linha qualificada.

Este mesmo raciocínio é válido quando se utiliza COUNT no lugar de IN ou ANY.

OR x UNION
----------

Em alguns casos, o banco de dados não consegue otimizar cláusulas de join ligadas por OR. Neste caso é mais eficiente ligar os
conjuntos de resultados por UNION.

Por exemplo :
```sql
    select a from tab1, tab2 where tab1.a = tab2.a OR tab1.x = tab2.x
```
pode ser reescrito como :
```sql
    select a from tab1, tab2 where tab1.a = tab2.a
    UNION
    select a from tab1, tab2 where tab1.x = tab2.x
```
A diferença é que na segunda forma, são eliminadas as linhas duplicadas, o que pode ser contornado com
UNION ALL.

MAX e MIN Agregados
-------------------

O banco de dados utiliza uma otimização especial para MAX e MIN quando há um índice na coluna agregada.
Para o MIN a pesquisa é interrompida quando encontra a primeira linha qualificada.
Para o MAX, o banco de dados vai diretamente para o final do índice e pega a última linha.

Os casos onde estas otimizações especiais não são utilizadas:

* a expressão do MAX ou MIN não é uma coluna.
* a coluna do MAX ou MIN não é a primeira do índice
* existe outro comando agregado na query.
* existe uma cláusula de GROUP BY.
* se existe cláusula WHERE, a otimização especial de MAX não é utilizada.
Se houver possibilidade de se conseguir otimização especial, vale a pena separar em várias queries. É mais
eficiente utilizar o índice várias vêzes, do que fazer scan table uma única vez.
Em alguns casos, pode ser mais eficiente não utilizar a otimização especial do MIN. Por exemplo, se há uma
cláusula where em outro índice, quanto mais restritivo for o WHERE, menos eficiente fica a otimização especial do MIN.

A solução é convencer o otimizador a não utilizar a otimização especial do MIN, colocando, por exemplo, duas
agregações na query.

Por exemplo :
```sql
    select MIN(coluna1)
    from tab
    where coluna2 = <valor encontrado só no final do índice da coluna1>
```
O banco de dados utilizará aqui a otimização especial do MIN, e fará um scan em quase todo o índice, pois a
qualificação na cláusula WHERE força esta situação. Se colocarmos mais um aggregate, convenceremos o otimizador a
utilizar o processo normal, criando um plano de acesso pelo índice da coluna2, neste caso, mais eficiente que a
otimização especial do MIN.
```sql
    select MIN(coluna1), MAX[coluna2)
    from tab
    where coluna2 = <valor encontrado só no final do índice da coluna1>
```

Joins e Datatypes
-----------------

Se a cláusula join utiliza datatypes diferentes, um deles será convertido para o outro. O datatype convertido é o
hierarquicamente inferior. O otimizador não consegue escolher um índice na coluna que é convertida.
O ideal é evitar este tipo de join, mas se não for possível, pode-se explicitamente converter o lado do join que
tem o menor custo de não utilização do índice.

Por exemplo :

```sql
    select c1, c2
    from tab1, tab2
    where tab1.col_char_75 = to_char(tab2.col_integer_75)
```

Utilização de BETWEEN na cláusula WHERE de uma consulta
-------------------------------------------------------

Na comparação de intervalo entre datas temos o SQL abaixo:
```sql
    Select ID,NOME from A where NASC > DATA1 and NASC < DATA2;
```
Normalmente a consulta abaixo terá um plano de execução melhor, resultando em tempo de resposta mais rápido.

```sql
    Select ID,NOME from A where NASC BETWEEN DATA1 and DATA2;
```

Evite a utilização de IN na cláusula WHERE de uma consulta
----------------------------------------------------------

Evite a utilização de IN na cláusula WHERE de um comando SQL. Esta construção tende a ser execução custosa para o Oracle. Abaixo seguem exemplos:

```sql
    1) Select ID,NOME from A where STATUS IN (1,2,3,4);
```

A consulta pode ser rescrita da forma abaixo que terá uma performance bem melhor..

```sql
    Select ID,NOME from A where STATUS BETWEEN 1 AND 4;
```

```sql
    2) Select ID,NOME from A where STATUS IN (1,2,4);
```

Neste caso a consulta pode ser rescrita da forma abaixo que na maior parte dos casos terá uma performance bem melhor..

```sql
    Select ID,NOME from A where STATUS BETWEEN 1 AND 2
    UNION ALL
    Select ID,NOME from A where STATUS=4;
```

Use o WHERE ao invés de HAVING para filtrar linhas
--------------------------------------------------

Evite o uso da clausula HAVING junto com GROUP BY em uma coluna indexada. Neste caso o índice não é
utilizado. Além disso, exclua as linhas indesejadas na sua consulta utilizando a clausula WHERE ao invés do HAVING. Se
a tabela possuir um índice na coluna.

Evite o operador DISTINCT
-------------------------

Evite incluir desnecessariamente a cláusula DISTINCT dentro de uma declaração SELECT. Distinct gera o método de acesso “SORT”.


Subqueries com cláusula de outer-join restritiva
------------------------------------------------

```sql
    select w from outer where y = 1 and x = (select sum(a) from inner where
    inner.b = outer.z )
```

Será quebrada pelo banco de dados nos seguintes passos

```sql
    select outer.z, summ = sum(inner.a)
    into #work from outer, inner
    where inner.b = outer.z and outer.y = 1
    group by outer.z

    select outer.w
    from outer, #work
    where outer.z = #work.z and outer.y = 1 and outer.x = #work.summ
```

O banco de dados copia a cláusula search ( y = 1 ) para a subquery, mas não copia cláusula join. Isto porque copiando a cláusula search, sempre tornará a query mais eficiente, mas copiando a cláusula join pode em muitos casos tornar a query mais lenta. A cópia da cláusula join só é eficiente quando ela é extremamente restritiva, mas o banco de dados faz a quebra antes do otimizador atuar. Então, para tornar a query mais eficiente, conhecendo previamente a alta restritividade da cláusula join, pode-se copiar a cláusula join para a subquery como no exemplo abaixo :

```sql
    tab_x -> tabela grande
    tab_y -> tabela pequena
    select a
    from tab_x, tab_y where tab_x.coluna_valor_unico = tab_y.a
    and tab_x.b = ( select sum(c) from tabela_interna
    where from tabela_interna
    where tab_x.d = tabela_interna.e
    and tab_x.coluna_valor_unico = tab_y.a)
```

Operador AND
------------


Se você deseja aumentar a performance de uma consulta que inclui o operador AND em uma cláusula WHERE, você deve considerar o seguinte:


1) No critério de consulta da cláusula where, pelo menos um dos critérios têm que estar baseado em uma coluna altamente seletiva e que contenha um índice.

2) Se nenhum dos critérios na cláusula WHERE for altamente seletivo, considere adicionar índices para todas as colunas envolvidas na cláusula where.



Operador OR
-----------

Haverá sempre uma busca completa na tabela (full table scan) se uma cláusula where de uma consulta conter um operador OR que referencie colunas que não tenham índices utilizáveis, ou seja, se você utiliza muitas consultas com a cláusula OR, você precisa ter certeza que cada uma das colunas referenciadas na cláusula where possui índices utilizáveis.

Mesmo que existam índices para a coluna utilizada, existem casos em que o banco não consegue utilizar os índices.

Evite as construções do tipo abaixo pois evitam que o banco utilize os índices das colunas:

~~~sql

    1 SELECT ID, NOME, ENDERECO FROM PESSOAS WHERE (:1 = 1 OR NOME=:1);

    2 SELECT ID, NOME, ENDERECO FROM PESSOAS WHERE (ID IS NULL OR NOME=:1);
~~~

Práticas que afetam a fase de Fetch
===================================

## Uso do Select *

Evite o envio de mais dados que o necessário para camada cliente. A utlização constante da cláusula SELECT * pode onerar a transmissão da resposta do SQL devido ao envio de dados desnecessários para o solicitante.  Sempre que possível é recomendável discriminar o que será retornado para evitar este tipo de situação.


Conclusão
=========

A escrita de SQLs pode impactar positivamente ou negativamente o tempo de resposta da uma aplicação. As dicas aqui publicadas auxiliam e evitar grande parte dos problemas de lentidão dos SQLs. Contudo, sempre podem existir exceções a regra.

Nestes casos, a correta homologação dos comandos SQL por meio de simulação em ambiente de testes, incluindo a verificação do plano de execução é uma boa prática que pode nos auxiliar a reduzir a probabilidade de um comando não se comportar adequadamente em ambiente de Produção.