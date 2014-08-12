---
remark: metadados para a ser usado pelo parser de conversão para pdf
date: 29 de abril de 2014
tipo_artigo: Artigo técnico de Infraestrutura de TIC
title: Weblogic e JRockit JVM Tuning
abstract: Este artigo apresenta uma introdução ao tuning da JVM JRockit em conjunto como o servidor de aplicação Oracle Weblogic, apresentando uma visão básica da JVM, os parâmetros necessários para um tuning inicial e as maneiras de configuração destes parâmetros no Weblogic.
author:
- affiliation: DSAA
  name: Erivelto Cássio de Oliveira
responsibility:
- affiliation: DSAA
  name: Claudio Yuassa Tokoro
diretoria: 'Diretoria de Infraestrutura de TIC - DIT'
superintendencia: 'Superintendência de Planejamento e Suporte de TIC - SUPS'
departamento: 'Departamento de Suporte de TIC - DEST'
tags:
- Weblogic
- JRockit
- Java
- JVM
- Tuning

---

Desafios
========

Apresentar as configurações necessárias para realização do tuning inicial do servidor de aplicação Weblogic em conjunto com a JVM JRockit.

Benefícios e/ou recomendações
=============================

Este artigo apresenta um ponto de partida para o tuning do servidor de aplicação Weblogic em conjunto com a JVM JRocit.

Introdução
==========

O servidor de aplicação Oracle Weblogic juntamente com a JVM JRockit proveem recursos para ambientes robustos, de alto desempenho e alta disponibilidade. Mas para tanto, depende de uma correta configuração e ajuste dos mais diversos parâmetros, tais como tuning da JVM, pool de data-sources, pool de threads, etc. Este artigo apresenta uma introdução ao tuning da JVM, fator fundamental para uma boa performance - segundo @Vijayaraghavan2014 e @Savija2011 e @Savija2013.


Organização dos espaços de memória da JVM JRockit
=================================================

A JVM JRocki possui duas áreas principais de memória:

- Memoria Nativa: área de memória não configurável onde são alocados elementos estáticos, como arquivos de biblioteca, classes java e objetos internos da própria JVM.
- Memória Heap: área de memória configurável onde os objetos java são criados e eliminados de forma dinâmica. É dividido em duas outras áreas: 
- Nursery: onde são alocados os objetos de curta duração ou recém criados.
- Old Space: onde são alocados os objetos de longa duração.

![Memória heap JRockit](imagens/heap.jpg)


Onde configurar os parâmetros de JVM no Weblogic?
=================================================

Caso o ambiente esteja sendo gerenciado pelo Node Manager, os parâmetros de JVM podem ser configurados diretamente no Console de Administração conforme caminho abaixo:

~~~
AdminConsole->Environments->Servers->YourManagedServer->Configuration (TAB)->
   ServerStart (SubTab)-> Arguments:(TextArea)
~~~

Caso não esteja sendo usado o Node Manager, os parâmetros podem ser configurados na variável de ambiente USER_MEM_ARGS antes de rodar o script de inicialização.

Exemplo:

~~~ {.bash}
export USER_MEM_ARGS="-Xms512m –Xmx1g"
$DOMAIN_HOME/bin/startManagedWebLogic.sh
~~~

Outra opção é editar o scrip de inicialização e incluir no inicio do arquivo a variável ```USER_MEM_ARGS```.


Efetuando o Tuning da JVM
=========================
 
Cada aplicação Java tem seu próprio comportamento e as suas próprias necessidades. A JVM JRockit pode ajustar-se a muitas delas automaticamente, mas para conseguir uma boa performance, deve-se ajustar pelo menos alguns parâmetros básicos.


Tamanho total de memória Heap
-----------------------------

Uma heap muito grande diminui a frequência de GC, mas pode demorar mais para completar os ciclos de GC. Deve-se definir o tamanho da heap em pelo menos duas vezes o tamanho dos objetos vivos na heap, o que significa que pelo menos metade da pilha deve ser liberada a cada ciclo de full GC.
 
Pode-se usar as seguintes opções de linha de comando para definir o tamanho de heap: 

```bash
 -Xms:<size>: Para definir o tamanho inicial e mínimo de heap. 
 -Xmx:<size>: Para definir o tamanho máximo de heap. 
```

Exemplo: 

```bash
java -Xms800m -Xmx2g MyServerApp 
```

Este comando inicia a JVM com uma heap de 800 MB e permite o seu crescimento até 2 GB.


Tamanho do Nursery
------------------

O tamanho ideal do Nursery depende da característica de cada aplicação. Se a aplicação cria muitos objetos temporários e de curta duração, o Nursery deve ser grande o suficiente para acomodar todos esses objetos, de forma que eles possam ser removidos com maior frequência pelas coletas menores do GC. Se a aplicação cria muitos objetos de longa duração, o Nursery deve ser pequeno, pois os objetos deverão ser movidos para o Old Space, onde a frequência dos ciclos de GC são bem menores. O tamanho do Nursery é definido pela opção ```-Xns:<size>```.

Exemplo:

```bash
java -Xms:1g -Xmx:1g -Xns:100m myApp
```

Se a opção ```-Xns``` for omitida, o valor será automaticamente definido com base no modo de GC escolhido, tamanho de heap e quantidade de processadores lógicos conforme tabela abaixo:

Options used             Default value
------------------       --------------------------------------------
-server (default)        50% of free heap
-client                  None; nursery does not exist
-Xgc:pausetime           10 MB per logical processor (maximum 80 MB)
-Xgc:throughput          50% of free heap


Garbage Collection (GC)
-----------------------

Selecione o modo de GC, usando uma das seguintes opções de -Xgc: 

- -Xgc:throughput: Define que a coleta de lixo deve ser otimizada para maior rendimento. Resulta em uma maior quantidade de memória livre a cada ciclo de GC, porém provoca pausas maiores na aplicação. Este é o modo padrão de coleta de lixo da JVM JRockit. 
- -Xgc:pausetime: Define que a coleta de lixo deve ser otimizada para pausas curtas. Resulta em pausas menores na aplicação a cada ciclo de GC, porém as pausas são mais frequentes.
- -Xgc:deterministic: Define que a coleta de lixo deve ser otimizada para pausas muito curtas e pré determinadas a cada ciclo de GC. A duração de cada pausa é definida pela opção ```-XpauseTarget:<tempo>```. Se a opção -XpauseTarget for omitida, assume-se o valor default de 30 ms. Este modo de GC deve ser usado somente em em ambientes onde se tem uma clara noção do comportamento da aplicação em memória, caso contrário o resultado poderá ser desastroso.
 
Exemplo:

```bash
java -Xms:1g -Xmx:1g -Xns:100m -Xgc:throughput myApp
```

Boas Práticas
=============

- Antes de alterar quaisquer parâmetros, registre as estatísticas atuais de desempenho.
- Defina um tamanho de heap fixo definindo -Xms e -Xmx iguais. Isso reduz o overhead e a quantidade de pausas, pois uma pausa é gerada a cada realocação de memória.
- Se a aplicação cria muitos objetos temporários (de curta duração), definir o Xnx tão grande quanto possível.
- Desabilitar chamadas explicitas de GC. Algumas aplicações podem incluir no seu código chamadas explicitas de GC, o que não é uma boa pratica. Portanto desabilite chamadas explicitas de GC incluindo na JVM a opção -XX:+DisableExplicitGC.

Conclusão
=========

Basicamente as configurações apresentadas anteriormente são suficientes na maioria dos casos, todavia diversos outros parâmetros de tuning estão disponíveis para ajustes finos da JVM, porém devem ser usados com parcimônia e em casos específicos. Não deve-se tentar corrigir problemas de performance de aplicação ou de infra-estrutura alterando parâmetros da JVM.

Referências
===========

---
remark: metadados com alguns dados para listar referências bibliográficas. Use quantos identificadores (ID) necessitar para listar as diferentes referências usadas no artigo
references:
- id: Vijayaraghavan2014
  title: "Oracle® JRockit Command-Line Reference, Release R28"
  author:
  - family: Vijayaraghavan
    given: Savija
  container-title:
  URL: 'http://docs.oracle.com/cd/E15289_01/doc.40/e15062.pdf'
  accessed:
    day: 29
    month: 4
    year: 2014
  publisher: Oracle America, Inc.
  type: book
  issued:
    year: 2014
    month: 4

- id: Savija2011
  title: "Oracle® JRockit Performance Tuning Guide, Release R28"
  author:
  - family: T.V.
    given: Savija
  container-title:
  URL: 'http://docs.oracle.com/cd/E15289_01/doc.40/e15060.pdf'
  accessed:
    day: 29
    month: 4
    year: 2014
  publisher: Oracle America, Inc.
  type: book
  issued:
    year: 2011
    month: 12
	
- id: Savija2013
  title: "Oracle® Fusion Middleware Understanding Oracle WebLogic Server 12c Release 1"
  author:
  - family: T.V.
    given: Savija
  container-title:
  URL: 'http://docs.oracle.com/cd/E24329_01/web.1211/e24446.pdf'
  accessed:
    day: 29
    month: 04
    year: 2014
  publisher: Oracle America, Inc.
  type: book
  issued:
    year: 2013
    month: 11

...