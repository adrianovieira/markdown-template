---
remark: metadados para a ser usado pelo parser de conversão para pdf ou odt
date: 04 de Agosto de 2014
tipo_artigo: Artigo técnico de Infraestrutura de TIC
title: Anatomia das Transações JAVA - Uso de Memória em Aplicações JAVA
abstract: O presente artigo tem como objetivo principal analisar os modelos de memória existentes na Java Virtual Machine Hotspot destacando a importância da definição das configurações de gerência de memória.
author:
- affiliation: DIED - DEQI
  name: Guilherme Namen Pimenta
responsibility:
- affiliation: SUPS
  name: Anderson Gourlart
diretoria: 'Diretoria de Infraestrutura de TIC - DIT'
superintendencia: 'Superintendência de Planejamento e Suporte de TIC - SUPS'
departamento: 'Departamento de Qualidade da Infraestrutura de TIC - DEQI'
tags:
- Java,
- Hotspot,
- Coletor de Lixo,
- Gerência de Memória,
- Garbage Collector,
- JVM
...

Introdução
==========
Um dos grandes avanços que a linguagem Java possui é a gerência de alocação de memória dinâmica. Por meio dela o programador não se preocupa mais com a alocação e remoção de objetos da memória principal, sendo que todo esse trabalho fica a cargo do modulo de coleta de lixo, que é parte integrante da Máquina Virtual Java. Para que os sistemas Java utilizem esta ferramenta da melhor forma possível, faz-se necessário a correta compreensão do seu funcionamento.

Desafios
========

Este artigo aborda como a memória é gerenciada pela Máquina Virtual Java Hotspot, e tem como maior desafio descrever todo o seu processo de gerência de memória.

Benefícios e/ou recomendações
=============================

O principal benefício deste artigo é informar para os desenvolvedores como os objetos Java são criados e destruídos durante a execução de um sistema.


Visão Geral da JVM Hotspot
=================

A tecnologia Java evoluiu muito desde seu lançamento em 1995. Novas tecnologias foram incluídas na máquina virtual para que o desempenho de sistemas Java deixasse de ser um problema. Atualmente, a JVM Hotspot da Oracle possui três grandes módulos: o Java Virtual Machine Runtime responsável pela execução do código java; o Just In Time Compiler (JIT) que realiza a compilação de código Java em tempo de execução e o Memory Manager que gerencia a memória. Esta arquitetura suporta a execução de sistemas de alto desempenho e o crescimento massivo de carga. Um bom exemplo disto é o compilador JIT, que é capaz de gerar código otimizado durante a execução dos sistemas Java.

\pagebreak
![Módulos da JVM Hotspot](imagens/jvm.jpg)

A figura acima mostra os módulos da JVM Hotspot da Oracle, como eles estão organizados e as suas interações.

As versões iniciais da JVM possuíam 32 bits de endereçamento de memória, limitando a mesma a endereçar no máximo quatro gigabytes de memória, sendo que este valor variar dependendo do sistema operacional. Atualmente, o endereçamento de memória de 64 bits permite alocar muito mais memória. Este crescimento do tamanho da memória administrada pela JVM fez com que os algorítimos de coleta de lixo fossem cada vez mais exigidos a vasculhar grandes áreas de memórias não contínuas em busca de objetos aptos a serem removidos.

A tarefa de coleta de lixo pode consumir todos os recursos de máquina, fazendo com que os sistemas Java fiquem inoperantes por intervalos de tempo significativos, criando assim quebra de regras de contrato de disponibilidade e tempo de resposta. Desta forma a tarefa de configurar corretamente a JVM para a execução de sistemas Java torna-se extremamente crucial para empresas de processamento de dados.

O novo endereçamento de 64 bits também acarreta algumas penalidades de desempenho por aumentar o tamanho da representação interna dos objetos Java, chamados ordinary objects pointers (oops), de 32 bits para 64 bits, fazendo com que existam poucos objetos na memória cache do processador. Este problema pode acarretar de 8% a 15% de perda de desempenho ao se comparar com o mesmo sistema Java executando com endereçamento de 32 bits. Para solucionar esta perda de desempenho a partir da JVM versão 6 os oops podem ser compactados ao se executar a JVM com a opção -XX:+UseCompressedOops. Esta compactação melhora o desempenho e consegue superar o desempenho das JVM com endereçamento de 32 bits. Algumas arquiteturas de CPU de 64 bits como Intel e AMD, ainda permitem que a JVM utilize recursos de registradores extras conhecidos como register spilling, o que permite um desempenho ainda melhor.

Arquitetura da Memória Java
=================

Uma das grandes vantagens da linguagem de programação Java é que os desenvolvedores não precisam gerenciar diretamente o ciclo de vida dos objetos. Para isto a JVM utiliza algoritmos que analisam a memória em busca de objetos que não são mais necessários e os eliminam, liberando espaço para alocação de novos objetos. O processo de gerenciamento da memória pode ser configurado de diversas formas, inclusive o próprio algoritmo de coleta de lixo pode ser trocado, por isto seria de extrema importância o conhecimento da arquitetura de memória da JVM pelos administradores de infraestrutura e desenvolvedores.

Este capítulo somente tratará da implementação da JVM Hotspot da Oracle. Essa JVM possui o algoritmo de coleta de lixo chamado geracional, do inglês generational garbage collector, que se baseá nas seguintes observações:

*  A maioria dos objetos perdem rapidamente sua  referência .
*  Existem poucas referências aos objetos mais velhos.

Estas observações baseiam-se na hipótese geracional fraca, do inglês weak generational hypothesis, que pode ser empregada para a grande maioria das aplicações Java. No intuito de otimizar as vantagens desta hipótese a JVM Hotspot dividiu o heap (área de alocação de memória dinâmica) nas seguintes áreas físicas:

*  Young Generation - Abriga os objetos que foram alocados recentemente. Geralmente os objetos nesta área de memória são pequenos e alocados em alta frequência, sendo liberados rapidamente pelas coletas de lixo pequena, do inglês minor gc, que são executadas mais frequentemente.
*  Old Generation - Abriga os objetos que foram alocados há muito tempoe que foram promovidos da Young Generation. Esta área de memória é a maior de todas e tende a crescer de forma mais lenta. Sendo assim, sua limpeza de memória é menos frequente e  seu custo computacional maior.
*  Permanent Generation[^1] - Abriga metadados como estruturas de classes, interned strings e etc. Ela não é uma área de memória geracional.

A vantagem de se utilizar esta arquitetura é a de que cada área de memória pode ter seu gerenciamento independente das demais e ainda empregar algoritmos de coleta de lixo diferentes.

Existem dois tipos de coleta de lixo, a pequena, que varre apenas a área de memória young e  por isto ela é mais rápida e a completa, que varre toda a área de memória e consequentemente é mais lenta e em alguns casos bloqueia a execução de aplicações Java.

A JVM quando redimensiona o tamanho do heap necessita previamente de uma coleta completa, por isto aconselha-se executá-la com os tamanhos máximo e mínimo do heap iguais.

![Arquitetura da memória da JVM Hotspot](imagens/heap.jpg)

Young Generation
-----------------

A área de memória young é dividida por sua vez da seguinte maneira:

*   Eden - Abriga a maioria dos objetos novos que são alocados (não todos, já que grandes objetos podem ser alocados diretamente na área de memória old). O eden estará sempre vazio após pequenas limpezas de memória.
*   Survivor space - São dois espaços de memória que abrigam os objetos que sobrevivem a pelo menos uma limpeza de lixo pequena. Ela é utilizada para evitar promoções de objetos de meia vida para a área de memória Old.

O processo de copiar um objeto de uma área de memória para outra pelas pequenas coletas de lixo é denominado copying garbage collector. É importante salientar que as áreas de memória podem não ter espaço suficiente para armazenar os objetos, neste caso o objeto será diretamente alocado na área de memória Old e ocorrerá o fenômeno chamado promoção prematura. Este procedimento pode acarretar sérios problemas de desempenho. Além disto, existe a possibilidade da área de memória Old estar repleta de objetos durante a pequena coleta de lixo; neste caso será automaticamente executada uma coleta de lixo completa com o objetivo de liberar espaço, caracterizando uma falha de promoção.

A alocação de memória na JVM Hotspot é rápida pelo fato de que sempre após uma pequena coleta de lixo a área de Eden estará vazia pelos processos de copying garbage collector e de limpeza.

As aplicações multitarefas na JVM Hotspot utilizam um recurso chamado Thread-Local Allocation Buffers (TLABs) para evitar a utilização de barreiras e por consequência aumentar o desempenho. Os TLABs cedem a cada thread um espaço de memória dedicado localizado em qualquer área de memória.

Tipos de algorítmos de coleta de lixo
---------------

A máquina virtual Hotspot possui três tipos diferentes de coletores de lixo padrão e um ainda experimental[^2]. Cada coletor possui suas peculiaridades e servem para diversos tipos de aplicações Java. 

*   Coletor de Lixo Serial (Serial GC) - Este coletor interrompe a aplicação Java durante as coletas de lixo pequena e completa (stop the world). Ele é destinado a aplicações que não possuem tempos de resposta muito rígido e que são executadas nas máquinas dos usuários. Este algorítimo é o padrão para a JVM Hotspot.
*   Coletor de Lixo Paralelo (Parallel GC) - Este coletor tira vantagens de ambientes multiprocessados e possui pequenos tempos de pausa de execução de aplicações, porém durante a coleta poderá apresentar, no pior caso uma pausa total da aplicação. Ele coleta o lixo em paralelo tanto na área de memória Young quanto na Old, sendo ideal para servidores que necessitam de muito rendimento e vazão. 
*   Concurrent Mark-Sweep GC (CMS) - Este coletor prioriza o tempo de resposta. Ele gerencia a área de memória Young da mesma forma do que o coletor de lixo paralelo, porém a área de memória Old é limpa de forma concorrente gerando assim apenas duas pequenas pausas durante o processo de coleta. Por ser executado de forma concorrente as áreas de memória podem sofrer problemas de fragmentação e neste caso poderá haver pausa completa da aplicação. Comparado com o coletor paralelo ele seria mais rápido por diminuir as pausas, mas a aplicação pode sofrer redução da sua vazão pelo fato do processo de coleta consumir recursos computacionais junto com a mesma. As principais aplicações que utilizam este tipo de coletor são servidores data-tracking, servidores Web e etc.
*   Garbage-First GC (G1) - Este coletor ainda experimental em algumas versões da Hotspot é ao mesmo tempo paralelo, concorrente e incremental compactado e pretende substituir o CMS. Ele divide toda a memória em pedaços de tamanho iguais, sendo que cada pedaço pode pertencer a uma área geracional diferente, ou seja, as áreas de memória não são contínuas. A figura abaixo evidencia isto claramente. As aplicações que se aproveitarão das  vantagens deste coletor são as mesmas do coletor CMS.

![Divisão da memória em blocos pelo algoritmo G1](imagens/cms.jpg)

A tabela abaixo mostra as principais diferenças entres os algoritmos de coleta de lixo.

|               | Coletor Serial|Coletor Paralelo|CMS                     | G1                     |
| ------------- |:--------------|:---------------|------------------------|------------------------|
| Paralelismo   | Não           | Sim            | Sim                    | Sim                    |
| Concorrência  | Não           | Não            | Sim                    | Sim                    |
| Young GC      | Serial        | Paralelo       | Paralelo e Concorrente | Paralelo e Concorrente |
| Old GC        | Serial        | Paralelo       | Paralelo e Concorrente | Paralelo e Concorrente |


Configurações de memória java
-----------------------------

A JVM Hotspot possui vários parâmetros de configuração, sendo seus valores padrões dependentes da arquitetura de hardware e sistema operacional. Entre eles podemos citar as seguintes configurações:


JVM

*  -Xms<n>[g|m|k] - Tamnho mínimo de memória do heap da JVM.
*  -Xmx<n>[g|m|k] - Tamanho máximo de memória do heap da JVM.

Young

*   -XX:NewSize=<n>[g|m|k] - Tamanho mínimo e inicial da área de memória young.
*   -XX:MaxNewSize=<n>[g|m|k] -Tamanho máximo da área de memória young.
*   -Xmn<n>[g|m|k] - Tamanho mínimo e máximo da área de memória young.X
*   -XX:SurvivorRatio=<n> - Define a taxa de espaço entre o eden e o survivor que pode ser calculada da seguinte forma: tamanho do survivor = -Xmn<value>/(-XX:SurvivorRatio=<ratio> + 2)
*   -XX:TargetSurvivorRatio=<percent> - Define a porcentagem do survivor que disparará uma coleta de lixo pequena.

Permanente

*   -XX:PermSize=<n>[g|m|k] - Tamanho inicial e mínimo da área de memória permanente.
*   -XX:MaxPermSize=<n>[g|m|k] - Tamanho máximo da área de memória permanente.

Limpeza de lixo

*   -XX:-ScavengeBeforeFullGC - Desabilita a limpeza da área de memória young durante a limpeza de lixo total.
*   -XX:MaxTenuringThreshold=<n> - Determina o número de vezes que o objeto passará pelas pequenas coletas de lixo antes de ser promovido.

Monitorando a memória
---------------------

O monitoramento das tarefas do coletor de lixo tem por objetivo avaliar os seguintes aspectos da aplicação:

*  O funcionamento do coletor de lixo.
*  O consumo de memória do heap.
*  O tamanho das áreas de memória Old e Young.
*  O tamanho da área de armazenamento permanente.
*  O tempo gasto em pequenas coletas de lixo.
*  A frequência da execução dos pequenos coletores de lixo.
*  Quantidade de espaço coletado nas pequenas coletas de lixo. 
*  O tempo gasto na coleta de lixo completa.
*  A frequência da execução da coleta de lixo completa.
*  A quantidade de lixo coletada pelas coletas de lixo paralelas.
*  Quantidade de memória livre antes e depois da coleta de lixo.
*  A quantidade de memória alocada nas áreas de memoria old e young antes de depois das coletas de lixo.
*  O consumo de memória da área permanente.
*  Análise da quantidade de memória nas áreas permanentes e old que dispara uma coleta de lixo completa.
*  Execução direta do comando System.gc()

Para avaliar estes aspectos a JVM Hotspot gera log das atividades do coletor de lixo. Para configurá-lo são utilizados os seguintes comandos:

*  -XX:+PrintGCDetails - Imprime as atividades do coletor de lixo.
*  -XX:+PrintGCTimeStamps - Imprime o tempo no log do coletor de lixo.
*  -XX:+PrintGCDateStamps - Imprime a data no log do coletor de lixo.
*  -Xloggc - Determina o nome do arquivo que armazenará os logs do coletor de lixo.
*  -XX:+PrintGCApplicationConcurrentTime e -XX:+PrintGCApplicationStoppedTime - Imprime o tempo de início e fim da coleta de lixo.
*  -XX:-UseGCLogFileRotation - Utiliza log rotativo.
*  -XX:GCLogFileSize=<n>K - Determina o tamanho do arquivo de log que será rotacionado.

Boas práticas
----------------

Conforme mencionado anteriormente, existem diversas configurações de memória que podem melhorar o desempenho das aplicações, porém, a melhor forma de otimizar o desempenho consiste em evitar más práticas de programação. O uso de pool de objetos, por exemplo, deve sempre que possível ser evitado, pois eles acabam referenciando outros objetos na área de memória young, resultando em um aumento de consumo de memória da área old, que possui por sua vez,  um processo de limpeza de lixo mais demorado. Em casos em que o usuo de pools são necessários, como o pool de conecções com o banco de dados, deve-se diminuir o número de objetos permanetes no pool. Outra má prática que devem ser  evitadas é a utilização, pela mesma razão, de muitos objetos Singletons. No emprego de ArrayLists, quando for possível, evitar o seu redimensionamento e por último, o uso de objetos extremamente grandes uma vez que a sua alocação pode ser realizado diretamente na memória Old. Estas e outras práticas estão em @livro.

É importante salientar que não existe formula mágica, ou configuração \"ideais\" de GC para todos os casos. As configurações costumam beneficiar algumas aplicações, enquanto prejudicam outras. Desta forma, cada caso deve ser analisado, e monitoramento, em um cenário mais realístico possível, para definir qual fornece o melhor comportamento.



[^1]: Na versão 8 da JVM a área de memória permanente não existe mais.
[^2]: Na versão 8 da JVM o algorítimo de coleta de lixo G1 está estável.

Conclusão
=========

A gerência de memória Java deve ser corretamente configurada para obter o máximo de desempenho, isso depende da correta compreensão e de boas práticas de programação.

Referências
===========

---
remark: metadados com alguns dados para listar referências bibliográficas. Use quantos identificadores (ID) necessitar para listar as diferentes referências usadas no artigo
references:
- id: livro
  title: "Java Performance"
  author:
  - family: "HUNT"
    given: "CHARLIE"
  - family: "JOHN"
    given: "BINU"
  container-title: "Java Performance"
  publisher: "Addison-Wesly"
  page: 699
  type: book
  volume: 1
  issue: 1
  issued:
    year: 2011
    month: Setembro

...
