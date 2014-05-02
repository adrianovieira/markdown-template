![Logomarca da DATAPREV](http://www-dtpnet/sites/default/files/images/logomarca-para-assinatura-de-email.gif)
#### [Diretoria de Infraestrutura de TIC - DIT]
##### [Superintendência de Planejamento e Suporte de TIC - SUPS]
###### [Departamento de Arquitetura Técnica - DEAT]

---  

# Artigo Técnico de Infraestrutura de TIC

->**Bancos de Dados NoSQL - Aplicações com Persistência Poliglota**<-

**Autor(es):**  José Guilherme Macedo Vieira  
**Responsável:** Cícero Vieira  

## Sumário

Os banco de dados relacionais tem sido usado intensivamente como forma de armazenamento de dados de uma grande quantidade de sistemas de informação. Entretanto, algumas empresas começaram a ter dificuldades em gerenciar uma grande quantidade de dados, uma vez que o modelo de armazenamento em tabelas tem certas limitações, como por exemplo a escalabilidade horizontal, a qual é menos custosa que a escalabilidade vertical. Com o intuito de sanar as limitações impostas pelo modelo relacional, uma nova geração de banco de dados - conhecidos como NoSQL - foram desenvolvidos e têm sido bastante adotados por empresas conhecidas, tais quais Facebook, Twitter, Google e Amazon. Dessa forma, esse artigo apresenta uma visão geral acerca dos bancos de dados NoSQL, os conceitos do desenvolvimento de aplicações com persistência poliglota e como podemos aplicar o conhecimento obtido para ajudar a solucionar desafios atualmente enfrentados no contexto de grandes organizações como a DATAPREV.

## Desafios

O principal desafio desse artigo é apresentar formas de se projetar aplicações altamente escaláveis, ótima performance e com um custo extremamente baixo, considerando os custos que se teria hoje para fornecer a mesma capacidade planejada. Esse artigo foi motivado pela necessidade de melhorar o desempenho das aplicações utilizadas na DATAPREV que fazem uso massivo de dados, como por exemplo, ferramentas de Bussines Intelligence (BI), Big Data, entre outras ferramentas que encontram o maior gargalo de performance os bancos de dados relacionais.


## Benefícios e/ou recomendações

<descreva os principais ganhos propostos pelo artigo, como melhoria de indicadores, processo de trabalho, etc>

### 1. Introdução

No desenvolvimento de aplicações, os arquitetos de software ao projetar a estrutura da aplicação precisam se preocupar com o armazenamento de dados de forma que contemplem os requisitos nâo funcionais. No entanto, é fácil perceber que a escolha padrão tem sido a utilização de bancos de dados relacionais. Isso se deve, entre outros motivos, à facilidade de se desenvolver aplicações utilizando bancos de dados relacionais (principalmente com o surgimento de frameworks ORM) e à segurança de um sistema de armazenamento que fornece atomicidade, consistência, isolamento e durabilidade (<a href="http://en.wikipedia.org/wiki/ACID"><b>ACID</b></a>). Como se não bastasse, utilizar bancos relacionais provê outros benefícios, como por exemplo: suporte à concorrência (utilizando transações) e o modelo relacional padrão (possibilidade de adotar o mesmo modelo em vários bancos de dados diferentes, através da linguagem <a href="http://en.wikipedia.org/wiki/SQL"><b>SQL</b></a>).

Os bancos de dados relacionais, ficaram famosos e viraram padrão na indústria de desenvolvimento de software por todas as facilidades já mencionadas, principalmente levando em considerações o rico ecossistema onde temos vários aplicativos, construídos por equipes diferentes. Em um ambiente como esse, aplicativos muitas vezes precisam utilizar os mesmos dados, de forma compartilhada, permitindo a utilização de um mesmo banco de dados por vários aplicativos, de tal forma que uma atualização realizada por um seja acessível a todos os outros, para manter a consistência de dados entre os aplicativos.

### 1.1 Dificuldade no Desenvolvimento

Entretanto, apesar de proverem grandes benefícios, os bancos de dados relacionais possuem suas limitações. Na visão de desenvolvedores de software, o maior problema na utilização de bancos de dados relacionais é a falta de casamento entre a forma que os dados são representados em memória pela linguagem de programação e a forma em que esses dados estão armazenados em bancos de dados relacionais, necessitando assim, de uma conversão entre os dois modelos, para que o software funcione . A literatura chama essa diferença de modelos de <b><a href="http://en.wikipedia.org/wiki/Object-relational_impedance_mismatch">incompatibilidade de impendância</a></b> ou <b><a href="http://en.wikipedia.org/wiki/Object-relational_impedance_mismatch">diferença de impendância</a></b>. Para exemplificar, os bancos de dados relacionais armazenam os dados na forma de tabelas, onde cada tabela possui linhas e colunas. Cada linha numa tabela é um registro e as colunas são os diversos dados que se pode haver nesse registro. Ocorre que alguns dados são muito complexos para serem armazenados nesse formato de grade bidimensional, culminando na necessidade de criar outras tabelas para armazenar as informações relacionadas àqueles registros. Nesse caso, cada registro na tabela conterá alguns, mas nâo todos os dados para uma grande quantidade de registros.

Dito isso, pode-se observar que os modelos relacionais sâo fáceis de serem compreendidos e de certa forma elegantes, uma vez que solucionam um problema complexo na forma de simples grades bidimensionais. No entanto, o modelo relacional tem seus problemas, principalmente quando se observa que os dados armazenados em um registro/linha/tupla precisam ser idealmente simples, uma vez que nâo podem conter nenhum conteúdo mais complexo, como um registro aninhado ou uma lista, senâo por meio de relações. Para o programador, isso é frustrante, pois a estrutura de dados em memória permite esse tipo de estrutura rica, com aninhamento de registros e listas, forçando ao programador a traduzir as representações no momento de armazenar ou obter dados de um banco relacional. Por conta disso, houve uma descrença muito grande nos anos 90 nos bancos relacionais, quando muitas pessoas acreditavam eles seriam substituídos por bancos de dados com estrutura similar às estruturas de memória. 

Ao mesmo tempo em que havia uma grande descrença no modelo relacional, havia o crescimento das linguagens orientadas a objetos e por tabela, o surgimento de bancos orientados a objetos. A ideia era substituir o desenvolvimento de linguagem estruturada e bancos de dados relacionais por linguagens orientadas a objetos e bancos de dados orientados a objetos. Apesar disso, o sucesso foi parcial. As linguagens orientadas a objetos vingaram e se tornaram o padrão da indústria de desenvolvimento de software, enquanto os bancos orientados a objetos foram relegados, nâo tiveram mais tanta atenção e os bancos relacionais triunfaram.

Com o triunfo dos bancos relacionais e a frequente reclamação dos desenvolvedores de software acerca da incompatibilidade de impendância, surgiram frameworks de mapeamento objeto-relacional, como o Hibernate, iBATIS, NHibernate, que diminuíram a frustação dos desenvolvedores, ainda que seja uma solução controversa. Enquanto esses frameworks facilitam o desenvolvimento, podem tornar os desenvolvedores alheios às questões de banco de dados, comprometendo o desempenho das consultas realizadas.

### 1.2 Surgimento da Arquitetura Orientada a Serviços

Durante muito tempo, os bancos de dados relacionais dominaram como escolha de armazenamento de dados. Entretanto, com o passar do tempo e o aumento na quantidade de dados que precisavam ser manipulados, esses bancos terminaram por nâo conseguir operar de forma satisfatória. Em vista disso, outras tecnologias começaram a ser experimentadas para sanar os problemas encontrados com a utilização de bancos relacionais nessas ocasiões. Um dos principais problemas que ocorriam é que vários aplicativos compartilhavam o mesmo banco de dados, uma vez que precisavam acessar os mesmos dados. Entretanto, como cada aplicativo tem suas necessidades específicas, principalmente no que diz respeito a desempenho, pode ocasionar alterações no modelo de dados ou na criação de índices, acabando por prejudicar o desempenho de outros aplicativos.

Percebendo esses problemas, surgiram formas diferentes de resolvê-los, entre elas a utilização de uma arquitetura orientada a serviços (SOA - Service Oriented Architecture), na qual cada aplicativo tem a função de fornecer um serviço específico, utilizando um banco de dados não compartilhado. Dessa forma, aplicativos comunicavam-se com os outros através de interfaces web bem definidas, fazendo uso do protocolo HTTP. Dessa forma, a integração de dados passou do domínio de banco de dados para a web, facilitando a comunicação, uma vez que poderiam ser utilizadas várias estruturas de dados mais ricas que o SQL permitia, como por exemplo, listas, matrizes, filas, entre outras. Essas estruturas de dados poderiam ser colocadas no formato JSON ou em documento XML, em um simples arquivo.

### 1.3 Utilização de Infraestrutura em Cluster

Nos anos 90, houve uma bolha especulativa de empresas de Internet, com forte aumento das ações dessas empresas nas bolsas de valores. Essa bolha ficou conhecida como <a href="http://pt.wikipedia.org/wiki/Bolha_da_Internet"><b>Bolha da Internet</b></a> ou bolha das empresas .com. Essas empresas tiveram grande acesso a capital de risco e cresceram a formar grandes empresas web. Com o crescimento dessas empresas na Internet, veio o aumento do volume de dados armazenados em suas sistemas de informação, com a coleta de grandes conjuntos de dados, como links, redes sociais, logs de aplicação, mapeamento. Esse aumento absurdo no volume de dados foi oriundo da grande quantidade de usuários desses sistemas.

Nesse momento, com a forte ascensão no volume de dados, essas empresas começaram a ter problemas no armazenamento e na manipulação desse volume. Obviamente, lidar com tantos dados e tráfegos de usuários requer mais poder computacional e a tendência, com o crescimento rápido das empresas era aumentar cada vez mais. Dito isso, havia duas abordagens possíveis para suportar essa demanda: escalar verticalmente ou horizontalmente. Escalar verticalmente, significa adquirir máquinas mais poderosas e maiores, com mais processadores, memória e capacidade de armazenamento numa única máquina. Entretanto, máquinas maiores são mais caras à medida que vai aumentando de tamanho. Para piorar, havia a questão de limite de espaço físico nas instalação das empresas, que não teria como comportar máquinas tão grandes. A outra abordagem seria comprar máquinas comuns, as quais são conhecidamente muito mais baratas, interligá-las em rede e fazê-las funcionar como se fosse uma única máquina. Essa interligação e funcionamento como uma única máquina é chamada de <a href="http://pt.wikipedia.org/wiki/Cluster"><b>cluster</b></a>. Essa estratégia em cluster terminou sendo a mais adotada, muito por conta do custo mais acessível, como também pelo fato de ser mais resiliente, uma vez que ainda que algumas máquinas do cluster falhem, o cluster como um todo continua a funcionar.<br/><br/>


<center>
![Escalabilidade Horizontal vs Vertical](http://3.bp.blogspot.com/-ydOvsdaSJ_M/UYndNnzibAI/AAAAAAAAAbI/gnZLGtE0ny0/s1600/Untitled.png)</center>

<br/>
Com a utilização cada vez mais frequente de clusters de máquinas, novos problemas apareceram. Os bancos de dados relacionais não foram projetados para serem executados em clusters. Alguns bancos relacionais ofereciam algum suporte à utilização em cluster, fazendo uso de subsistemas de discos ou fragmentando o banco de dados. Entretanto, nenhuma das abordagens parece satisfatória, uma vez que a primeira ainda possui o subsistema como SPOF (Single Point of Failure ou Único Ponto de Falha) e a segunda faz com que a aplicação tenha que lidar com a complexidade de fragmentação do banco.

Com toda essa problemática em torno da utilização de bancos relacionais em clusters e devido à necessidade de se escalar horizontalmente, dado o custo benefício, as empresas se viram obrigadas a encontrar uma maneira para armazenar o grande volume de dados que detinham. Eis que surge nesse cenário duas empresas de grande influência: Google e Amazon. Essas empresas começaram a investir em pesquisas e experimentos com grande volumes de dados armazenados em clusters. Como resultado, a Google publicou o artigo "BigTable: A Distributed Storage System for Structured Data", no qual relata a criação do banco de dados distribuído chamado BigTable, seu modelo de dados, como também sua arquitetura e implementação. A Amazon trouxe resultados em 2007 com o sistema de armazenamento Dynamo.



### 2 NoSQL

O termo NoSQL foi cunhado no final dos anos 90, quando Carlo Strozzi lançou o seu banco de dados relacional Strozzi NoSQL para ambientes Unix. O Strozzi possui uma forma de operação baseada no paradigma de operadores de streams (stream-operators), em detrimento do SQL (Structured Query Language). Esse banco relacional era manipulado através de shell scripts encadeados (pipelines) e as suas tabelas eram armazenadas em arquivos ASCII. 

No entanto, o termo "NoSQL" tal qual utilizamos hoje tem uma origem um tanto curiosa. John Oskarsson, desenvolvedor de software do Last.fm, queria conhecer mais sobre os tipos de armazenamento de dados que estavam sendo apresentados num evento sobre o Hadoop em São Francisco, Estados Unidos. O tempo era muito curto para conhecer todas as iniciativas e John teve uma ideia de fazer encontro para envolver todos os interessados em conhecê-lo. John precisava de um nome para a reunião e pediu sugestões no canal #cassandra no IRC. Eric Evans, blogueiro de tecnologia e funcionário da Rackspace Hosting na época, sugeriu "NoSQL". Oskarsson gostou da sugestão e realizou o primeiro encontro "NoSQL", no qual vários sistemas de armazenamento de arquivos que não faziam uso da linguagem SQL foram apresentados, como Cassandra, Voldemort, HBase, Dynomite, Hypertable, CouchDB e MongoDB entre outros. 

NoSQL não é um nome ou padrão imposto por alguma empresa ou autoridade da área de tecnologia. É apenas um acrônimo interessante que é muito frequentemente escolhido para designar bancos de dados que não fazem uso da linguagem SQL como um todo. Entretanto, há sim, características em bancos de dados, além da ausência do SQL, que podem os caracterizar como bancos NoSQL, como por exemplo: código aberto, projetado para execução em clusters, entre outros atributos. Porém, é importante salientar que essas características não fazem de um banco de dados, um banco NoSQL, mas que bancos de dados com essas características tendem a ser chamados de bancos NoSQL.

Dessa forma, o significado do NoSQL hoje é extremamente confuso, no sentido de que não há uma definição formal e por isso uma miríade de bancos de dados com as mais diversas características são chamados dessa forma. Assim, o mais importante é compreender de forma geral, abstraindo uma série de fatores. É interessante entender o termo NoSQL como um movimento para prover armazenamento altamente escalável horizontalmente, a fim de solucionar os desafios enfrentados por aplicações que fazem uso de um grande volume de dados.

[colocar foto aqui]

### 2.1 Modelo de Dados baseado em Agregados

Um modelo de dados é uma representação de como percebemos os nossos dados e como os utilizamos para atingir objetivos do mundo real. Esse modelo nos ajuda a entender como o sistema deve armazenar as informações, através da descrição dos dados e suas relações no formato de objetos. Esses objetos são geralmente abstrações de algo do mundo real, como por exemplo, produtos, professores, alunos, entre outros.

Entretanto, para fins de melhor entendimento desse artigo, modelo de dados se refere à forma que um banco de dados organiza seus dados. Dito isso, como observado anteriormente, o modelo de dados mais utilizado até hoje é o modelo de dados relacional, o qual retrata a forma que banco de dados relacionais organizam seus dados por meio de tuplas e tabelas. Todavia, como a intenção dos bancos de dados NoSQL é solucionar problemas encontrados nos bancos relacionais na execução em clusters, é natural que tenham sido projetados com modelos de dados diferentes do relacional. Os modelos de dados NoSQL podem ser aglomerados em 4 categorias distintas: chave-valor, documento, família de colunas e grafos. As três primeiras categorias utilizam o conceito de orientação agregada.


### 2.1.1  Orientação Agregada

A orientação agregada é um conceito que parte do princípio que frequentemente temos a necessidade de trabalhar com dados com estrutura mais complexas do que simples tuplas de dados, como por exemplo, dados aninhados. Essas estruturas de dados mais complexas está muito presente nas soluções NoSQL como um todo e por falta de um nome formalmente definido, para este artigo será chamada de "agregado". A ideia de agregado é oriunda dos conceitos de DDD - Domain Driven Design, propostos por Eric Evans. Segundo o DDD, um agregado é um conjunto de objetos relacionados que tratamos como uma unidade, ou seja, como se fosse um único objeto. Esse conceito é importante, pois com frequência queremos manipular essas estruturas complexas de forma atômica, a fim de manter a consistência dos dados.

A organização de banco de dados NoSQL no geral, se encaixa muito bem com a noção de agregado, motivo pelo qual esses bancos de dados são conhecidos por funcionarem muito bem em ambientes clusterizados, já que o agregado é uma unidade de fácil replicação e fragmentação. É importante mencionar, que em geral, os agregados são mais fáceis de serem manipulados por programadores, uma vez que já estão habituados a trabalhar com estruturas agregadas.

Para entender melhor a noção de agregados na prática, suponha que seja necessário criar um site de comércio eletrônico e que nesse site ites serão vendidos diretamente aos que clientes. É factível que teremos que armazenar informações sobre usuários, produtos, pedidos, envios, endereço de cobrança, os dados para pagamento, entre outros. Esse contexto poderia ser modelado para um sistema de banco de dados relacional da seguinte forma:
<br/><br/>
<center>![Modelo de Dados Relacional](https://dl.dropboxusercontent.com/u/33955026/ImagensArtigo/diagrama1.jpg)</center>
<br/><br/>
No banco de dados os dados ficariam da seguinte forma:
<br/><br/>
<center>![Exemplo de Dados Relacionais](https://dl.dropboxusercontent.com/u/33955026/ImagensArtigo/1exemplodadosrelacionaisartigo1.png)</center>
<br/><br/>
Ao transformamos esse modelo seguindo a orientação agregada, o modelo poderia ficar da seguinte maneira:
<br/><br/>
<center>![Modelo de Dados Agregados](https://dl.dropboxusercontent.com/u/33955026/ImagensArtigo/diagramaagregado1.jpg)</center>
<br/><br/>
Podemos observar que ficou um pouco diferente no modelo de dados agregados, uma vez que devemos valorizar a unidade (agregado) que queremos manipular na nossa aplicação. É fácil perceber que nesse modelo, existem dois agregados principais, os quais são cliente e pedido. O cliente possui uma lista de endereços para cobrança, enquanto o pedido possui uma lista de itens solicitados, uma lista de endereços para envio e pagamentos. Se observarmos bem, o agregado pagamento também possui um endereço para cobrança. Agora observemos como ficariam os dados representados em JSON:

    {
    
      "clientes":[
      {
          "id":1,
          "nome": "Guilherme",
          "enderecoCobranca":[{"cidade":"Recife"}]
      },
      {
          "id":2,
          "nome": "Tiago",
          "enderecoCobranca":[{"cidade":"Salvador"}]
      },
      {
          "id":3,
          "nome": "João",
          "enderecoCobranca":[{"cidade":"Salvador"}]
      }      
      ],
      "pedidos":[
          {
              "id":1,
              "cliente_id":1,
              "itens":[
                  {
                   "id_produto":1,
                   "preco":300,
                   "nome":"Violão"
                  }
                  ],
              "enderecoEnvio":[{"cidade":"Recife"}],
              "pagamento":[
                  {
                      "infoCartao":"7845756214532550",
                      "enderecoCobranca":{"cidade":"Recife"}
                  }
                ]
                  
              
          },
          {
              "id":2,
              "cliente_id":2,
              "itens":[
                  {
                   "id_produto":2,
                   "preco":1500,
                   "nome":"iPad"
                  }
                  ],
              "enderecoEnvio":[{"cidade":"Salvador"}],
              "pagamento":[
                  {
                      "infoCartao":"2145652389541260",
                      "enderecoCobranca":{"cidade":"Salvador"}
                  }
                ] 
              
          },
          {
              "id":3,
              "cliente_id":3,
              "itens":[
                  {
                   "id_produto":3,
                   "preco":2500,
                   "nome":"Notebook Dell"
                  }
                  ],
              "endereçoEnvio":[{"cidade":"Natal"}],
              "pagamento":[
                  {
                      "infoCartao":"7958451269541250",
                      "enderecoCobranca":{"cidade":"Natal"}
                  }
                ] 
                  
              
          }
       ]      
    }

É importante observar que na implementação agregada temos a repetição de muitos dados, em especial no registro de endereço. Se observarmos da perspectiva de negócio, esse modelo se ajusta bem à noção de que não é desejável para o sistema a ser implementado, que o endereço de envio ou de cobrança sejam alterados.

A repetição se deve ao fato de que a orientação agregado desnormaliza o modelo relacional colocando todas as informações referentes a um agregado dentro dele próprio. Dessa forma, é comum dizer que um modelo de dados agregados não suporta relações e que por ser um modelo desnormalizado perde-se a consistência dos dados. Entretanto, é errôneo pensar dessa maneira, uma vez que a relação está implícita entre os agregados.

Esse modelo proposto é apenas um exemplo e existem inúmeras maneiras de se modelar esse contexto de negócio. É importante observar, que no modelo orientado a agregados depende muito de como se deseja manipular os dados, ao contrário da abordagem relacional, na qual se tem um modelo padrão para toda e qualquer situação, fazendo uso de normalização dos dados nas tabelas. Para ilustrar essa forma de modelagem instrisicamente ligada à implementação, tomemos que a intenção seja acessar todos os pedidos de um cliente ao mesmo tempo. Para que o dado seja recuperado de forma mais rápida, é mais interessante que coloquemos os pedidos dentro do agregado cliente, optando assim por um único agregado. Por outro lado, se quisermos acessar pedido a pedido, a separação se faz necessária, visto que não queremos manipular cliente por cliente e em cada cliente procurar por seus pedidos até encontrar o pedido que queremos manipular. Em algumas situações de negócio é interessante que se tenha as duas abordagens e devido a isso, muitas pessoas decidem por ignorar a modelagem a agregados.

### 2.1.1.1 Lições da Orientação a Agregados

Os bancos de dados relacionais, como já mencionado anteriormente, não possuem o conceito de entidade agregada no seu modelo de dados. Entretanto, a questão da utilização do agregado na modelagem de dados é a facilidade da execução em um cluster. Embora em alguns contextos seja difícil estabelecer o limite de agregação de entidades, é importante fazer uso desses conceitos para tornar as aplicações mais rápidas. Isso acontece porque os bancos de dados relacionais suportam quaisquer operações em quaisquer tabelas (mesmo aquelas que estão distribuídas em vários nós) em uma única transação ACID. Pesquisar por dados em diferentes nós de um cluster é muito custoso, uma vez que será preciso computar a pesquisa em cada nó separadamente e depois aglomerar o resultado para dar a resposta. Esse problema ficará mais evidente mais à frente, quando serão abordados os modelos de distribuição de dados em cluster.

Faz-se necessário ressalvar que a utilização de agregado não é boa em todas as ocasiões e que devemos modelar tendo em mente os tipos de manipulações que desejamos fazer com os dados. Imaginemos que um determinado varejista deseje analisar as vendas de seus produtos num determinado período. Um agregado de pedidos será um problema para a performance da consulta uma vez que ele terá que percorrer toda a estrutura de cada pedido para obter informação de pedidos que tenham aquele produto, para enfim verificar se o produto foi vendido naquele período. Entretanto, se essa operação não for necessária, um agregado de pedidos é excelente para aumentar a velocidade da aplicação, do contrário uma abordagem não-agregada é mais indicada.

Uma outra questão é que muito se diz que bancos de dados NoSQL não suportam transações ACID e devido a isso não possuem consistência. Apesar desses bancos não possuírem transações ACID, promovem a manipulação atômica de um agregado por vez, o que às vezes é suficiente para manter a consistência se o modelo de dados for corretamente elaborado. Se for necessário manipular mais de um agregado de uma vez de forma atômica, por exemplo, clientes e pedidos, os desenvolvedores terão que gerenciar a consistência no código da aplicação. Dessa forma, cada caso é um caso e o importante é decidir quando usar ou não a orientação agregada de forma a beneficiar a performance da aplicação como um todo.

### 2.2 Modelos de Distribuição

Foi dito anteriormente que os bancos de dados NoSQL são conhecidos por sua capacidade de executar em um grande cluster de máquinas, escaladas horizontalmente. Dentro desse cenário, o agregado é excelente para operar num ambiente distribuído (e.g um agregado por máquina), em vez das custosas tabelas particionadas. Entretanto, existem várias formas de se distribuir os dados em cluster e essas maneiras de se distribuir dados em máquinas chamamos de "modelos de distribuição".

No geral, existem basicamente dois modelos de distribuição de dados: a replicação e a fragmentação. A replicação consiste em replicar os mesmos dados em vários nós do cluster, enquanto a fragmentação divide os dados em nós diferentes. Essas técnicas não se excluem, de forma que ao projetar o cluster, pode-se utilizar uma ou ambas. Existem duas topologias de replicação de dados: mestre-escravo e ponto-a-ponto. A seguir, serão demonstradas as situações de utilização dessas técnicas, começando da mais simples para a mais complexa.

### 2.2.1 Fragmentação

Com muita frequência as pessoas acessam partes diferentes de um mesmo conjunto de dados, fazendo com que o banco de dados fique extremamente ocupado. Em tais situações, faz sentido colocar partes dos dados em servidores diferentes, o que é comumente chamado de <b>fragmentação</b> (sharding). <br/><br/>

<center>![Sharding](http://www.cubrid.org/manual/91/en/_images/image39.png)</center>

<br/><br/>
No mundo ideal, usuários diferentes conversariam com servidores diferentes obtendo respostas rápidas. Esse cenário é praticamente impossível de ser atingido, tendo em vista que as aplicações só fazem sentido quando utilizadas por mais de um usuário. Entretanto, é possível direcionar os esforços para que a carga esteja bem balanceada entre os servidores no contexto da fragamentação. Para atingir tal objetivo, é preciso aglomerar em cada fragmento, em um servidor, dados que são acessados ao mesmo tempo.

É importante saber como fragmentar os dados de forma que o usuário possa obter senão todos, mas a maioria dos dados que acessa, de um único servidor, potencializando dessa maneira, a rapidez da consulta. O conceito de orientação a agregados ajuda muito nesse sentido, uma vez que ao modelar agregados, projetamos de forma a colocar os dados acessados ao mesmo tempo em um mesmo conjunto chamado agregado, de tal forma que um agregado é o candidato perfeito para ser distribuído em nós de um cluster.

Todavia, para organizar os dados em diversos nós, é preciso olhar para o contexto geral e analisar uma série de fatores que podem auxiliar a projetar essa distribuição para um melhor desempenho. Um exemplo simples, é colocar os agregados em um servidor localizado fisicamente perto de onde os usuários fazem acesso. É preciso analisar o contexto que a aplicação vai funcionar e determinar quais os possíveis impactos no desempenho que poderiam ser minimizados, adequando a distribuição dos dados a esse contexto.

A fragmentação dos dados é muito importante para a performance dos aplicativos, uma vez que pode melhorar consideravelmente o desempenho de leitura e gravação. Fragmentar os dados é uma ótima maneira de escalar horizontalmente as gravações dos dados. Entretanto, utilizada sozinha a fragamentação não ajuda às aplicações a tornarem-se mais resilientes, ou seja, tolerante a falhas. Se um nó falhar, todos os dados do fragmento daquele nós ficam inacessíveis, apesar de apenas os usuários que acessam daquele fragmento específico que sofrerão, o que na prática, não nos deixa confortáveis. Na prática, utilizada sozinha, a fragmentação será um problema pois introduzirá pontos únicos de falha, diminuindo a resiliência da aplicação.

Apesar de todos os benefícios, utilizar a fragmentação pode ser muito caro se utilizada tardiamente. A experiência nos diz que é sábio utilizar a fragmentação dos dados desde o início do desenvolvimento da aplicação se quisermos tirar proveito de seus benefícios sem grandes problemas no ambiente de produção. Em um projeto que trabalhei há alguns anos atrás, decidimos fragmentar os dados depois que a aplicação estava em produção e as consultas ao banco de dados estavam muito lentas. Ocorre que a essa altura, não era mais possível modelar os dados com o conceito de agregação fragmentá-los, uma vez que já haviam grandes tabelas modeladas seguindo a orientação relacional. Dessa forma, a fragmentação não foi realizada da forma desejada, ocasionando grandes problemas de refatoração de código. No fim das contas, o problema foi parcialmente resolvido através do uso da próxima técnica que descreverei aqui: replicação mestre-escravo.

### 2.2.2 Replicação Mestre-Escravo

Na replicação mestre-escravo, os dado são replicados em vários nós do cluester. No geral, um nó do cluster é escolhido como o mestre (controlador). O nó mestre é a principal fonte dos dados e é reponsável por processar atualizações nos dados do cluster. Os nós restantes são escravos e fazem somente replicar os dados que o mestre possui. Dessa forma, toda e qualquer inserção ou atualização de dados que houver no mestre será replicada em alguns ou todos os escravos de acordo com o fator de replicação configurado no banco de dados.
<br/><br/>
<center>![Replicação Mestre-Escravo](http://www.netexpertise.eu/images/Replication.png)</center>
<br/><br/>
Essa configuração é muito interessante quando se tem um número muito grande de leituras no banco de dados, uma vez que é possível distribuir a carga entre os nós do cluster. Entretanto, como antes de chegar aos nós escravos, toda e qualquer operação de atualização é processada pelo mestre, ficamos dependentes da capacidade do mestre de processar o volume total de atualizações. É interessante observar, que essa técnica embora aumente consideravelmente a velocidade de leitura dos dados, não é muito boa quando se deseja fazer muitas gravações, uma vez que a replicação dos dados faz com que a gravação dos dados em todos os nós do cluster seja demorada.

Se o mestre falhar, as solicitações de leitura ainda podem ser direcionadas para os escravos. Por outro lado, como as gravações precisam que a primeira gravação seja realizada no mestre, como não há mestre, o cluster fica impossibilitado de realizar gravações até que um novo mestre seja estabelecido. Estabelecer um novo mestre é fácil e rápido. Atualmente já existem sistemas que estabelecem um novo mestre em caso de falha do anterior de forma automática, não sendo mais necessário configurar o novo mestre manualmente. Dessa forma, podemos observar que essa topologia de distribuição torna o sistema bastante resiliente para leituras.

Todavia, todo sistema tem suas falhas e apesar dos grandes benefícios que essa topologia introduz, algumas falhas são evidentes, como por exemplo, a inconsistência. Quando um dado vai ser gravado, ele precisa ser replicado para todos os nós do cluster. Entretanto, se ocorrer uma leitura pelo dado em um nó do cluster e o dado não tiver sido replicado ainda, haverá inconsistência de leitura, ou seja, o último dado gravado não vai estar disponível para aquela consulta. Alguns sistemas não podem se dar ao luxo de operarem, mesmo que em pequena escala, com dados desatualizados. É o caso por exemplo, de alguns sistemas de saúde, em que um dado desatualizado pode ser o limiar entre a vida e a morte.

### 2.2.3 Replicação Ponto a Ponto

Na replicação ponto, diferentemente da mestre-escravo, não há um mestre. Todos os nós do cluster operam de forma igual, com leituras e gravações, de forma que ainda que alguns nós falhem nenhum dado é perdido. Essa forma de replicação numa rede ponto a ponto é interessante do ponto de vista da do desempenho, que em geral é maior que na replicação mestre-escravo, como também por retirar o ponto único de falha que era o mestre na topologia anterior.
<br/><br/>
<center>![P2P Replicação](http://docs.oracle.com/cd/B19306_01/server.102/b14226/repln001.gif)</center>
<br/><br/>
Todavia, essa forma de replicação também sofre com o problema de inconsistência dos dados em algumas situações, mas de uma maneira um pouco diferente. Se duas gravações de um mesmo dado forem realizadas em nós diferentes ao mesmo tempo, haverá um conflito de gravação. Enquanto na topologia anterior se tinha inconsistência na leitura, nesta topologia a inconsistência é de gravação. As inconsistências de leitura são temporárias, uma vez que os dados atualizados serão eventualmente replicados. As inconsistências de gravação são para sempre. Ambas inconsistências podem ser tratadas de forma satisfatória para a maioria dos casos. Esse tratamento será abordado mais à frente.

### 2.3 Lidando com a Consistência

Bancos de dados relacionais são fortemente consistentes, graças ao conceito de transações. Por outro lado, os bancos de dados NoSQL procuram pensar na consistência de forma um pouco diferente, permitindo que em algumas situações os dados não sejam totalmente consistentes. Dessa forma, quando se vai projetar um sistema com um banco de dados NoSQL é preciso pensar em quão consistente o seus sistema precisa ser e em que situações a consistência não pode ser relaxada. Nos tópicos a seguir, as formas de consistência serão descritas.

### 2.3.1 Consistência de Atualização

Nada melhor do que um exemplo para ilustrar a situação e compreendê-la melhor. Vamos ver a situação de um exame de sangue por exemplo. Dois funcionários de um hospital, ao verificar os dados dos exames de sangue do paciente, percebem que há um erro na taxa de glóbulos brancos. Cada funcionário verifica o último exame de sangue realizado pelo paciente e vai atualizar os bancos de dados. Acontece que um funcionário pega o último exame de fato e o outro pega o penúltimo exame. Cada funcionário vai atualizar os dados do paciente, cada um com seu exame, ao mesmo tempo. Ocorre que o banco de dados ao receber as atualizações precisa decidir qual realizar primeiro e a depender do critério que o banco de dados utiliza para escolher, os dados mais atualizados do funcionário que pegou realmente o último exame podem ser sobrescritos pelos dados do penúltimo exame. Esse tipo de situação é bastante conhecida como <b>conflito escrita-escrita</b>. Ao analisar o banco de dados do paciente, um médico com os dados errados pode dar um diagnóstico igualmente errado, o que pode afetar gravemente a saúde do paciente.

De forma a lidar com essas situações de conflito de escrita, existem dois tipos de abordagens possíveis: a pessimista e a positiva. A abordagem pessimista parte do princípio que antes de qualquer gravação, cada usuário tem que obter a permissão para gravar no banco de dados. Dessa forma, quando cada funcionário do hospital tentasse gravar, o banco tentaria dar a permissão para gravar. Quem obtiver a permissão primeiro, impede que qualquer outro funcionário manipule o dado até que a operação de gravação do anterior seja finalizada. No cenário aqui descrito, o funcionário que obteve a permissão de gravar, vai realizar a operação com sucesso, enquanto o outro ao tentar gravar vai ver o dado da última atualização e vai verificar se realmente deseja atualizar aquele dado. Podemos observar que ainda assim não impede de termos inconsistências nos nossos dados, uma vez que há ainda a possibilidade de uma pessoa mesmo que intencionalmente, sobrescrever um dado atualizado por um desatualizado. A abordagem otimista, por outro lado, verificaria o dado a ser gravado foi alterado desde a sua última leitura e se sim, informaria ao funcionário da situação e que ele deveria analisar o valor antes de realmente atualizar.

Como se pode observar, cada abordagem tem seus prós e contras. É preciso entretanto, analisar o contexto da aplicação que está sendo projetada, levando em consideração principalmente a topologia de rede, no caso de umcluster de máquinas. Em um único servidor é muito mais fácil de lidar com conflitos de gravação do que em um ambiente com replicação distribuída, como no caso da replicação ponto a ponto. Isso é pode ocorrer porque diferente nós podem ter os mesmos dados com valores diferentes e como nessa topologia de replicação não existem um nó master para organizar a sequência de atualizações, os dados terminam por ficarem inconsistentes. 

### 2.3.2 Consistência de Leitura

Consistência de leitura significa que toda vez que alguma consulta for realizada no sistema, os dados mais atualizados para aquela consulta serão retornados. Imagine a situação de um software hospitalar que monitora as medicações tomadas pelo paciente durante a internação. O paciente Sr. Sick tomou Xmg do antibiótico X para uma grave infecção, o qual está armazenado na tabela medicamentos. A enfermeira Cecília deu o remédio ao paciente às 19h. Uma hora depois é a hora do Sr. Sick tomar o medicamento novamente. Cecília e outra enfermeira do hospital chamada Márcia, vêem ao mesmo tempo que o Dr. Sick tem que tomar o remédio. Na retirada do medicamento do estoque, ambas atualizam o banco de dados com a informação que vão atendê-lo ao mesmo tempo. Acontece que Cecília foi mais rápida, retirou o remédio, injetou o remédio no Sr. Sick e atualizou o sistema. Entretanto, o banco de dados gravou a atualização da Márcia e não a da Cecília. Como a última informação fornecida a Márcia era de que o Sr. Sick ainda não havia tomado o remédio, ela aplica a injeção no Sr. Sick e o paciente morre de overdose devido à alta dosagem do remédio. Dessa forma, a leitura da Márcia foi uma <b>leitura inconsistente</b>, pois ela não estava com os dados atualizados no momento da sua consulta.

Os bancos relacionais, visando contornar esse tipo de problema, suportam transações. Dessa forma, se a liberação do remédio para retirada em estoque estivesse na mesma <b>transação</b> da atualização do atendimento no banco de dados, o paciente não haveria morrido, uma vez que uma das enfermeiras não conseguiria retirar o medicamento caso a outra já tivesse iniciado o processo de atualização do banco. Assim, apenas uma enfermeira teria o medicamento em mãos e o Sr. Sick só receberia uma única dosagem, não sofrendo overdose. Entretanto, as pessoas costumam afirmar que os bancos de dados NoSQL não suportam transações. Pelo menos não do jeito que os bancos relacionais suportam com as transações ACID. Pela lógica, como esses bancos não relacionais não possuem o conceito de transação, não conseguem garantir a consistência dos dados. Esse pensamento não está inteiramente correto, uma vez que os banco de dados NoSQL fornecem consistência sim, mas de uma maneira ligeiramente diferente. Se pensarmos nos bancos de dados orientados a agregados, por exemplo, eles não possuem transações entre agregados. Por outro lado, fornecem operações atômicas em cada agregado, o que signfica que a consistência é fornecida <b>POR AGREGADO</b>.

Um observador mais atento logo perceberia que nem todos os dados podem ser modelados em um único agregado para atender às necessidade do sistema, o que termina por provocar a necessidade de operações com múltiplos agregados e por sua vez uma inconsistência nos dados no período de tempo entre a atualização de um agregado e a do outro. Esse período é conhecido na literatura como <b>janela de inconsistência</b>. Existem bancos de dados que possuem uma janela de inconsistência muito pequena, tão pequena quanto o tempo que um banco relacional levaria entre a atualização em uma tabela e na outra. A diferença sutil é que no banco de dados relacional ou todas as atualizações ocorrem, ou nenhuma ocorre, enquanto nos bancos NoSQL é possível que a atualização de um agregado ocorra e no outro não. Pelo menos, não de forma imediata. Em bancos NoSQL as atualizações podem levar um tempo para serem replicadas em todos os nós de um cluster. Os dados de um agregado podem ser salvos em um nó, enquanto os de outro agregado em outro nó e ao atualizar cada agregado os outros nós são informados que precisam ser atualizados por algum mecanismo implementado pelo banco de dados. A questão aqui é que ainda que os dados não tenham sido replicados nos outros nós do cluster, os dados já estão disponíveis para leitura, uma vez que as operações atômicas foram realizadas em cada nó e finalizadas com sucesso. Em um banco relacional isso não ocorre. O banco relacional só torna o dado disponível para leitura após a replicação em todos os nós do cluster, assegurando que qualquer consulta sempre terá o último dado atualizado. Dessa forma, é justo dizer que os bancos de dados NoSQL oferecem consistência, mas não em 100% do tempo para todos os dados. Devido a isso, esses bancos são chamados de <b>eventualmente consistentes</b> pois sua consistência é <b>eventual</b>.

Observando o tipo de consistência de um banco de dados NoSQL, é preciso escolher o tipo de banco a ser utilizado com sabedoria, respeitando as limitações e durações das janelas de inconsistência. Conhecer como esses bancos operam em relação à essa janela é fundamental para a escolha adequada, uma vez que não são todas as aplicações que precisam ser 100% consistentes em todas as operações. É preciso observar em que situações a aplicação pode se dar ao luxo de não ter dados consistentes, ou pelo menos, por quanto tempo seria aceitável que a aplicação não tivesse o dado mais atualizado. Existem bancos da dados cujas janelas de inconsistência são tão pequenas que é possível substituir completamente um banco de dados relacional, mesmo para aplicações extremamente críticas. Nesses casos, a probabilidade de se obter um dado desatualizado é tão pequena, que os ganhos em performance e outros benefícios, tornam os riscos aceitáveis. A esse trabalho de usar probabilidades para aceitar a inconsistência em determinadas situações, podemos chamar de relaxamento de consistência.

### 2.4 Bancos de Dados Chave-Valor  

Bancos de dados Chave-Valor são também chamados de armazenamento chave-valor. Esses bancos de dados são simplesmente implementações de tabelas hash simples. Esse tipo de armazenamento é muito utilizado quando se faz consultas através de chave primária. Para este artigo vamos utilizar como exemplo o Riak, o qual é um banco de dados chave-valor que utiliza um modelo simples de estrutura de dados. Existem outros bancos de dados chave-valor disponíveis no mercado também, como o Redis, Memcached DB, Amazon Dynamo DB e o Voldemort.

No Riak, os dados são armazenados em buckets (baldes). Um bucket é uma estrutura de dados para separar as chaves dos objetos. De forma a facilitar o entendimento, imagine o bucket como uma URL ou um nome de pacote para uma classe. Dentro de um bucket é possível armazenar qualquer tipo de conteúdo. O Riak não faz distinção de tipo de dado armazenado, o que o torna um recurso poderoso. Quem deve saber ler o conteúdo é a aplicação que vai fazer uso dessa base de dados. Entretanto, cada bucket possui uma estrutura de dados bem definida, de forma bidimensional, com uma chave e um valor. Cada chave é uma identificação única que representa um determinado valor, como pode ser visto na figura abaixo:
<br/><br/>

<center>![Bucket do Riak](https://dl.dropboxusercontent.com/u/33955026/bucketRiak.png)</center>

<br/><br/>

Dessa forma, é fácil perceber que a estrutura de um bucket é como se fosse uma tabela do modelo relacional com apenas duas colunas, uma para a chave e a outra para o valor. A diferença aqui é que apesar de a chave se assemelhar a uma chave-primária no modelo relacional, a coluna do valor não possui uma restrição de tipo de dados como no modelo relacional. Dessa forma, o valor pode ser qualquer coisa, desde um XML, JSON até dados serializados. Para compreender melhor o funcionamento de uma estrutura de chave-valor, tomando como base o modelo do Riak, imaginemos que uma determinada aplicação deseja armazenar as informações da sessão do usuário em um armazenamento persistente (o que por sinal, é muito comum). Para essa situação seria possível armazenar todos os dados da sessão do usuário num bucket com uma chave e um único valor. Assim, teríamos um único objeto na base de dados que armazenaria todos os dados da sessão de um usuário. Um exemplo de como ficaria um bucket com os dados da sessão num único objeto, observe a figura abaixo:
<br/><br/>
<center>![Bucket Sessão Usuário](https://dl.dropboxusercontent.com/u/33955026/bucket.jpg)</center>
<br/><br/>

### 2.4.1 Consistência

No geral, a consistência dos bancos de dados chave-valor se aplica apenas às operações realizadas a nível de chave, ou seja, na inserção, remoção ou atualização de um único conjunto chave-valor (uma única chave e um único valor). Portanto, a consistência não é garantida caso se queira operar com múltiplas chaves e múltiplos valores. Essa proposição é especialmente verdade em armazenamentos chave-valor distribuídos, como no caso do Riak, em que temos a <b>consistência eventual implementada</b>. O Riak é bastante esperto no que diz respeito ao gerenciamento de conflitos de gravação, tratando de duas maneiras simples situações como essa. A primeira é aceitar toda gravação mais recente sobrescrever as mais antigas, enquanto a segunda é impedir a gravação e retornar os valores conflitantes para que o usuário/aplicação decida qual valor deseja gravar de fato no banco de dados. No geral, é adotada a primeira estratégia, porque lidar manualmente com cada conflito é bastante difícil, principalmente quando se trata de grandes volumes de dados manipulados.

Para melhor exemplificar como a consistência eventual funciona no Riak, utilizemos um exemplo da própria documentação do Riak. Suponha que um servidor num cluster que roda Riak se recuperou recentemente de uma falha. Esse servidor tem armazena uma chave "técnico-do-manchester-united", cujo valor é "Alex Ferguson". Entretanto, como os fãs do futebol devem saber, Alex Ferguson não é mais técnico do Manchester United, sendo substituído por David Moyes. Nos outros servidores do cluster, os dados estão corretos, com o valor para a chave "técnico-do-manchester-united" sendo "David Moyes". Dessa forma, temos 1 servidor com os dados antigos e os outros com os dados mais recentes no cluster Riak. Uma é então realizada, buscando pela chave "técnico-do-manchester-united". Entretanto, ao configurar um cluster Riak é preciso especificar quantos servidores no mínimo devem responder a uma solicitação de consulta e por padrão são 2 servidores. Esse número é oriundo do fator de replicação do cluster, o qual especifica em quantos servidores um mesmo dado deve ser gravado, de forma a garantir a disponibilidade. O fator de replicação padrão é 3, o que significa que cada dado deve ser gravado no mínimo em 3 servidores. Nesse cenário, quando se faz uma consulta pela chave, a solicitação é enviada para os 3 servidores e no mínimo 2 servidores dos 3 que possuem o dado gravado devem responder. Esse conceito é chamado de quórum, o qual especifica que cada solicitação deve ser respondida pela maioria simples mínima do número de servidores do fator de replicação.

Num cluster Riak, qualquer nó do cluster poder assumir o papel de um coordenador para os requests que recebe. O importante aqui é saber que sempre existe um nó do cluster que coordena uma solicitação. Continuando o cenário anterior, 2 dos 3 servidores irão responder à solicitação da chave buscada para o nó que está coordenando a solicitação. Não importa a ordem que o nó coordenador (master) recebe a solicitação, pois o Riak identifica valores novos e antigos através de um marcador de versão. Dessa forma, supondo que apenas 2 servidores respondam à solicitação, um com o valor "Alex Ferguson"e o outro com "David Moyes" para a chave informada, o valor retornado para a aplicação será sempre o "David Moyes" por ser o mais recente. É através do conceito de quórum que o Riak provê a consistência das informações de leitura, diminuindo bastante a probabilidade de ocorrência de uma leitura obsoleta.

### 2.4.2 Transações

O conceito de transação não é unanimidade entre os bancos de dadas NoSQL, uma vez que cada um busca implementar esse conceito de uma forma específica. No geral, as gravações não são garantidas. O Riak usa o conceito de quórum para garantir a gravação na maioria das situações. Dessa forma, suponhamos que temos um cluster Riak com o fator de replicação 5 e configuremos que no mínimo 3 servidores respondam à solicitação de gravação. Isso significa dizer que a gravação será disparada para 3 servidores e que pelo menos mais 2 servidores devem replicar a informação gravada nesses outros 3. A operação de gravação tem que ser bem sucedida nos 3 nós disparados (quórum mínimo) dos 5 que devem conter os dados. Dessa forma, o Riak pode tolerar que 2 nós falhem durante a gravação, uma vez que dos 5 que devem conter os dados, somente 3 (maioria simples) precisam ter a gravação bem sucedida para garantir a operação.

### 2.4.3 Consultas

No geral, os bancos de dados chave-valor só permitem a consulta dos valores através da chave. No entanto, existem situações em que se não conhece a chave e ainda assim é preciso consultar o valor. Uma possibilidade seria obter uma lista das chaves e depois pesquisar os valores um a um. Esse tipo de operação, entretanto, é muito complicada e custosa, principalmente se realizada por muitos usuários. Alguns bancos de dados, como o Riak, oferecem a possibilidade de consultar os valores através de índices. No Riak essa possibilidade é dada através do <b>Riak Search</b>.

### 2.4.5 Quando utilizar?

Os bancos de dados chave-valor são ótimos para armazenar informações de sessão web. Existem muitas aplicacoes que armazenam os dados da sessao em um banco de dados ou em arquivos. Um armazenamento chave-valor em geral é muito mais rápido que um banco relacional ou um arquivo de texto, pois toda a informação da sessão de um usuário pode ser obtida através de uma única operação. Existem muitas aplicações que armazenam os dados de sessão em memória, fazendo uso de estruturas de dados como o Memcached. Entretanto, estruturas em memórias são temporárias e não garantem a disponibilidade, principalmente no caso de falha de um nó do cluster. Dessa forma, quando for importante garantir a disponibilidade dos dados da sessão, o Riak é um ótimo aliado para essas situações.

Existem outros dados que muitas aplicações também armazenam em sessão, enquanto outras em bancos de dados relacionais, como por exemplo, informações de permissão de acesso e carrinhos de compras. Dessa forma, informações de permissão de um determinado usuário, preferências como idioma, cor, fuso horário, produtos no carrinho de compras, podem ser armazenadas em um único objeto num bucket, com uma chave identificando o usuário, sendo possível assim, obter todas essas informações numa única operação de consulta. Portanto, bancos de dados chave-valor são muito úteis para garantir a disponibilidade em um ambiente clusterizados de informações que possuem um único identificador e fazem sentido juntas.

Apesar de bancos chave-valor serem muito úteis e possuírem muitos benefícios, existem situações em que não é muito apropriado utilizar esse tipo de armazenamento. Situações como relacionamento entre dados, transações com múltiplas operações (operações com gravação em várias chaves), consulta por dados sem a chave do conjunto chave-valor e consulta por várias chaves ao mesmo tempo. Todas as outras ocasiões os bancos de dados chave-valor são interessantes, especialmente quando é possível colocar todos os dados vinculados a uma única chave, realizando a busca da informação numa única solicitação.

### 2.5 Bancos de Dados baseados em Documentos     

Banco de dados baseados em documentos armazenam documentos numa grande variedade de formatos. Os documentos armazenados nesses bancos de dados em geral possuem uma árvore hierárquica de elementos, possibilitando armazenar vários tipos de estruturas de dados encontradas em linguagens de programação, como coleções, mapas, conjuntos, hashes e até mesmo valores escalares. Apesar de os documentos armazenados no banco serem parecidos em sua estrutura, não necessariamente precisam ser iguais, uma vez que banco de dados orientados a documentos possuem uma estrutura parecida com a do chave-valor, com a diferença que é possível fazer buscas por conteúdo armazenados no valor.

Para melhor compreender o conceito de banco de dados de documentos, vamos examinar um documento:

	{ "nome": "Guilherme",
	  "curte": [ "Futebol", "Computadores" ],
        "cidade": "Natal",
        "ultimaCidadeVisitada":
	}

O documento acima poderia ser facilmente uma linha num banco de dados relacional comum, no qual nome, curte, cidade e ultimaCidadeVisitada seriam as colunas da tabela TURISTA, por exemplo. Agora vejamos um documento parecido, mas com algumas alterações na formatação do conteúdo:

	{
		"nome": "Pedro",
		"cidadesVisitadas": [ "Chicago", "London", "Pune", "Bangalore" ],
		"endereços": [
	{ 
		"estado": "RN",
		"cidade": "Mossoró",
		"tipo": "R"
	},
	{ 
		"estado": "PE",
		"cidade": "Escada",
		"tipo": "R" }
	],
		"cidade": "Natal"
	}

Como podemos observar, os documentos acima são parecidos na formatação, mas possuem conteúdos diferentes. Em bancos de dados de documentos é possível armazenar os dois documentos no mesmo banco e esses documentos pertencerem a um mesmo conjunto ou coleção. Essa abordagem é bem diferente dos bancos de dados relacionais em que o conteúdo, o formato e os tipos de dados são restritos, obrigando que todas as linhas numa mesma tabela sigam o mesmo formato. É como se no banco baseado em documentos as tabelas fossem livres de restrições, onde cada linha pudesse variar o formato e o conteúdo. De acordo com os documentos acima, podemos representar por exemplo, <b>cidadesVisitadas</b> como um array ou <b>endereços</b> como uma lista de documentos embutidos dentro do documento principal.

Existem muitos banco de dados orientados a documentos no mercado, como MongoDB, CouchDB, Terrastore, OrientDB, RavenDB, o Lotus Notes e muitos outros. Entretanto, para explicar os conceitos desses tipos de bancos de dados, esse artigo utilizará o MongoDB.

No MongoDB, cada instância do banco de dados possui vários bancos de dados. Cada banco de dados de cada instância pode ter várias coleções. Comparado a bancos relacionais, uma instância de um banco de dados relacional é o mesmo que uma instância no MongoDB, os schemas no relacional são similares a banco de dados da instância do MongoDB e as tabelas do relacional seriam coleções no MongoDB. Quando um documento vai ser armazenado no MongoDB, é preciso especificar em qual banco de dados e em qual coleção o documento vai ser armazenado.

### 2.5.1 Consistência

A consistência num banco de dados MongoDB é configurável. O MongoDB possui o conceito de conjunto de réplicas. Um conjunto de réplicas é um grupo de instâncias do MongoDB que possuem os mesmos dados. No MongoDB, existe um servidor primário (Primary) que recebe todas as operações de escritas. Todas as outras instâncias, chamadas de secundárias (secondaries) replicam os dados da instância primária de forma a possuir o mesmo conjunto de dados.

O servidor primário aceita todas as operações de escritas oriundas de aplicações clientes. Entretanto, um conjunto de réplicas só pode possuir um único servidor primário. Uma vez que apenas um único servidor do cluster aceita operações de escrita, a estratégia de utilizar conjunto de réplicas provê consistência estrita, a qual garante que qualquer leitura por um dado dentro do conjunto de réplicas sempre obterá o valor mais atualizado.

![MongoDB Diagrama](http://docs.mongodb.org/manual/_images/replica-set-read-write-operations-primary.png)

### 2.5.2 Transações

O MongoDB não faz utilização de transações tal qual nos bancos relacionais. Por outros lado, o banco garante operações atômicas na manipulação de um único documento. Dessa forma, ao manipular um documento, as operações só podem obter dois resultados: sucesso ou falha.

### 2.5.3 Disponibilidade

De acordo com o Teorema CAP, só podemos obter 2 dos 3 desejos: Consistência, Disponibilidade e Tolerância a Partições. Não é possível obter os 3 ao mesmo tempo de acordo com esse teorema. Dessa forma, os banco de dados orientados a documentos buscam melhorar a disponibilidade através da replicação os dados numa topologia mestre-escravo. Os mesmos dados estão disponíveis em vários nós de um cluster com um só mestre. Entretanto, mesmo que o servidor mestre (primário) falhe, ainda assim é possível fazer consultas aos dados.

No MongoDB as replicações dos dados entre o servidor primário e os escravos é feita de forma assíncrona. Os nós do cluster elegem um servidor primário entre eles. Se todos os nós do cluster possuem direitos de votos iguais, alguns nós podem ser favorecidos por estarem mais próximos aos outros servidores, por ter mais memória RAM, ou outro critério. Dessa forma, existem alguns critérios para a "votação". Entretanto, essa votação pode ser influenciada através de configurações no próprio banco de dados.

Se um servidor primário falhar, os nós restantes do cluster votam um novo mestre e todas as operações de escritas são então redirecionadas para esse novo mestre eleito. Quando o antigo mestre voltar a ficar disponível, ele se tornará um escravo e terá perdido o trono.

### 2.5.4 Quando utilizar?

Bancos de dados orientados a documentos podem ser utilizados para uma série de casos, como Log de Eventos, Sistemas Gerenciadores de Conteúdo, blogs, análise de dados web, análise de dados em tempo real, aplicações de loja virtuais, entre muitos outros casos. 

Em relação aos logs de eventos, as aplicações precisam utilizar formas diferentes de log de acordo com suas necessidades. Numa empresa como a DATAPREV, existem váris aplicações que fazem seus logs com estrutura e conteúdos diversos. Um banco de dados baseado em documentos, por suportar vários tipos diferentes de conteúdo, poderia atuar como uma base central de logs para a empresa. Esse tipo de abordagem facilitaria bastante o armazenamento e o gerenciamento de logs das mais diversas aplicações a nível corporativo.

Uma vez que banco de dados de documentos não possuem um esquema de dados bem definido como nos relacionais, gerenciadores de conteúdo podem fazer um ótimo uso desse tipo de banco, pois podem armazenar os mais diversos tipos de conteúdo, como comentários de usuários, registros de usuários, perfis, entre outros. Blogs por exemplo, que possuem em seus posts conteúdos variados, encontrariam num banco de dados orientado a documentos um ótimo recurso.

As aplicações de análise de dados em tempo real podem fazer um bom uso dos bancos de documentos, uma vez que partes dos documentos podem ser atualizadas, tornando fácil o armazenamento de visitas por página, visitas únicas e outras métricas podem ser ainda adicionadas sem alterar o esquema de dados. As funcionalidades que o banco oferecem beneficiariam bastante uma análise de dados rápida, principalmente levando em consideração que a leitura é bem mais rápida que num banco relacional.

Entretanto, nem tudo são flores. Os bancos de dados orientados a documentos não devem ser utilizados em contextos que requeiram operações complexas, que exijam múltiplos passos e que tenham que ocorrer de forma atômica. Para casos assim, é melhor a abordagem relacional. Também não se deve utilizar documentos quando a estrutura do agregado armazenado no documento varia com frequência.
                                                                                                                                                                           

### 2.6 Bancos de Dados baseados em Família de Colunas

Existem vários bancos de dados de família de colunas como o Cassandra e o Amazon SimpleDB, entre outros. Esses bancos de dados fazem uso de uma estrutura parecida com a chave-valor, com a sutileza de que as chaves são mapeadas para valores agrupados em várias famílias de colunas, onde cada família de coluna em si é um mapa de dados.

Para compreender melhor o armazenamento em famílias de colunas, esse artigo fará uso do Cassandra para explicar os conceitos. Outros bancos também serão mencionados quanto pertinente.

Os bancos de dados orientados a famílias de colunas, armazenam os dados em famílias de colunas como se fossem linhas que possuem várias colunas associadas à chave da linha. A chave da linha é nada mais do que um identificador único da linha armazenada. As famílias de colunas são grupos de dados relacionados que normalmente são acessados em conjunto. Por exemplo, Usuário e Perfil seriam  dados acessados frequentemente em conjunto, enquanto Usuário e Compras não.

Assim como outros nos outros bancos NoSQL abordados até aqui, apesar de termos uma estrutura flexível, o esqueleto inicial é montado visando consultas ou acessos frequentemente realizados, de tal forma a otimizar o modelo do banco à necessidade da aplicação.

![Modelo Familia de Colunas](http://kellabyte.com/wp-content/uploads/2012/02/cassandra-columnfamily.png)

A figura acima, mostra de forma simples a estrutura da família de colunas do banco de dados Cassandra. É possível notar que existe uma única chave (Row Key) para várias colunas. Cada coluna possui pelo menos três atributos: o nome da coluna, um valor e um timestamp. Cada família de colunas pode ter 1 ou mais colunas, podendo inclusive haver famílias de colunas com números de colunas diferentes.

É importante notar que no Cassandra a unidade básica de operação é uma coluna e essa própria coluna é uma estrutura de chave-valor em si, como mencionado anteriormente, onde o nome da coluna se comporta como uma chave. Dessa forma, existem dois tipos de chave: a chave da linha e a chave da coluna. Um observador mais atento perceberia essa estrutura como um hash dentro de outro ou em outras palavras, um banco chave-valor dentro de outro.

O timestamp é um atributo importante nas colunas, pois é através dele que os dados são expirados, conflitos de escritas são resolvidos, entre outros benefícios para o funcionamento do banco como um todo. Esse atributo é sempre obrigatório em todas as colunas. Especifiquemos então a estrutura de uma coluna, fazendo uso da terminologia JSON:

	{
		nomeDaColuna: "nomeCompletoUsuario",
		valor: "José Guilherme Macedo Vieira",
		timestamp: 12345667890
	}

No exemplo acima, a chave ou nome da coluna é "nomeCompletoUsuario", enquanto o valor é "José Guilherme Macedo Vieira" e o timestamp 12345667890. Como o timestamp é um valor numérico, não deve ser utilizado com aspas duplas. Uma estrutura mais complexa, utilizando uma família de colunas seria de tal forma:

	//Família de Coluna
	{ //Inicio da Linha 1
	"jose-guilherme" : {
		nome: "José Guilherme",
		sobrenome: "Macedo Vieira",
  		ultimaVisita: "22/04/2014"
		}

	//Inicio da Linha 2
	"Yago-Pikachu" : {
		nome: "Yago",
		sobrenome: "Pikachu",
		localidade: "Belém"
		}
	}

No exemplo acima, temos 2 linhas na família de colunas, sendo a primeira com a chave da linha "jose-guilherme", com 3 colunas cada uma com as chaves "nome", "sobrenome" e "ultimaVisita", enquanto a segunda tem a chave da linha "Yago-Pikachu", com 3 colunas com as chaves "nome", "sobrenome" e "localidade". É importante observar que as colunas não precisam ter os mesmos nomes, muito menos os mesmos conteúdos. Inclusive, é possível que uma linha tenha mais colunas que a outra, como no exemplo abaixo:

	//Família de Coluna
	{ //Inicio da Linha 1
	"jose-guilherme" : {
		nome: "José Guilherme",
		sobrenome: "Macedo Vieira",
		sexo: "Masculino",
  		ultimaVisita: "22/04/2014"
		}

	//Inicio da Linha 2
	"Yago-Pikachu" : {
		nome: "Yago",
		sobrenome: "Pikachu",
		localidade: "Belém"
		}
	}

Para ficar mais claro, analogamente, uma família de coluna seria uma tabela num banco de dados relacional, no qual uma chave identifica a linha e uma linha consiste em várias colunas. A diferença é que no banco orientado a colunas cada linha não precisa ter necessariamente as mesmas colunas, com as mesmas chaves cada e colunas podem ser adicionadas a uma linha a qualquer momento, sem adicionar as mesmas colunas a outras linhas.

Uma informação importante é que o Cassandra armazena as famílias de colunas em keyspaces. Um keyspace é como se fosse uma instância de banco de dados relacional onde todas as colunas relacionadas àquela aplicação são armazenadas. Para criar famílias de colunas é preciso criar um keyspace antes, pois toda família de coluna tem que pertencer a um keyspace.

### 2.6.1 Consistência

Quando uma escrita é recebeida pelo Cassandra, o dado é primeiramente gravado num log de commits, depois gravado para uma estrutura em memória chamada <b>memtable</b>. Uma operação de escrita só é considerada bem sucedida, caso os dados tenham sido gravados no log de commits e na memtable. Todas as escritas são armazenadas em memória e de tempos em tempos são movidas para uma estrutura persistente conhecida como <b>SSTable</b>. As SSTables não aceitam uma nova escrita até que sejam limpas. Caso haja alterações nos dados, uma nova SSTable é criada para armazenar a alteração. Obviamente, todo esse processo gera bastante lixo, com SSTables não utilizadas e devido a isso a coleta desse lixo é feita através de um processo chamado compactação.

O Cassandra faz uso de várias estratégias de consistência. Essas estratégias são configuradas no banco de dados de forma a adequar o banco de dados à realidade da aplicação. As formas de consistência que o Cassandra pode assumir está fora do escopo desse artigo e você pode obter essa informação <a href="http://www.datastax.com/documentation/cassandra/2.0/cassandra/dml/dml_config_consistency_c.html">aqui</a>.

### 2.6.2 Transações

O Cassandra não possui suporte a transações da forma tradicional. Entretanto, o banco fornece atomicidade em operações a nível de linhas, o que significa que inserir ou atualizar colunas para uma determinada linha de coluna, será tratada como uma operação única com dois resultados possíveis: sucesso ou falha. Os dados são gravados primeiro em logs e depois na memtable, só sendo considerados se ambas as operações forem bem sucedidas. Caso um nó falhe, o log é utilizado para aplicar as mudanças no nó.

### 2.6.3 Quando utilizar?

- Log de Eventos

- Blogs e Gerenciadores de Conteúdo

- Contadores (Ex. contar visitantes de uma página)

- Conteúdo com Tempo Expirável

### 2.8 Conclusão

Para concluir esse artigo é preciso salientar a grande lição que fica ao analisar as características dos bancos NoSQL. Cada banco de dados foi projetado para atender um propósito específico, com problemas diferentes. Cada banco busca resolver um determinado problema da maneira mais performática possível, buscando sempre atender a critérios que são importantes no contexto atual, como por exemplo a disponibilidade e durabilidade dos dados.

Em geral, quando se utiliza uma única forma de armazenamento para todos os problemas possíveis, acabamos por criar soluções com baixo desempenho. Isso ocorre porque armazenar dados transacionais, fazer cache de informações de sessão, percorrer estruturas em grafos como relações entre entidades, são problemas bem distintos. Mesmo em bases relacionais, os requisitos são bem diferentes para soluções OLAP e OLTP.

Com muita frequência vemos soluções que buscam resolver problemas distintos utilizarem as mesmas soluções de armazenamento de dados, culminando em baixa performance. Bases relacionais são boas para assegurar que relacionamentos entre entidades existem. Entretanto, se quisermos descobrir novos relacionamentos entre dados utilizando o mesmo banco relacional, será bem difícil. Bancos relacionais são bons com relacionamentos já existentes e não em descobrir novas relações.

Se observarmos, ao utilizar um banco de dados relacional para todos os tipos de problemas para uma plataforma de e-commerce por exemplo, a arquitetura ficaria mais ou menos assim:

![Arquitetura BD Relacional](https://dl.dropboxusercontent.com/u/33955026/e-commerceSGBDR.png)

Como se pode ver, todos os dados são armazenados dentro de um único banco de dados. Informações de sessão de usuário, o carrinho de compras, dados de pedidos, estão todos juntos. Nem todos esses dados armazenados possuem os mesmos requisitos de disponibilidade, consistência ou backup. Nesse momento, cabe se perguntar: Realmente é preciso armazenar informações de sessão com as mesmas regras de backup dos dados de pedidos? Os requisitos de disponibilidade das informações de sessão é igual aos demais dados armazenados?

Ao se fazer essas perguntas, fica mais claro que as aplicações lidam com tipos variados de problemas e nem sempre uma única forma de armazenamento consegue resolvê-los de forma satisfatória, causando um baixo desempenho na aplicação como um todo. Pior: ao executar operações não performáticas numa base de dados, compromete outras operações para a qual a base foi projetada. Nesse contexto que surge a necessidade de adotar formas diferentes de persistência para problemas diferentes, culminando no termo <b>persistência poliglota</b>, uma vez que aplicação deve saber "falar" com bancos de dados que falam "línguas" (possuem estruturas/formas de consulta diferentes) diferentes.

### 2.8.1 Falando Várias Línguas

Foi demonstrado anteriormente que as aplicações que falam uma única língua (possuem um único banco de dados) terminam por não ter um bom desempenho. Foi demonstrado anteriormente uma situação de uma plataforma de comércio eletrônico e que essa aplicação poderia ficar bastante lenta ao falar apenas a língua do banco relacional. Com o intuito de resolver esse problema, é preciso ensinar a aplicação a falar outras línguas (bancos de dados), de forma a ganhar mais desenvoltura para obter as informações, culminando em melhor desempenho.

No contexto do e-commerce mostrado anteriormente, uma estrutura de armazenamento chave-valor poderia ser utilizada para armazenar os dados do carrinho de compras antes do pedido ser confirmado, como também armazenar as informações de sessão do usuário. Como vimos anteriormente, esse tipo de banco é ideal para esse tipo de dado. O armazenamento chave-valor faz sentido porque o carrinho de compras é geralmente acessado por um ID/Chave e uma vez confirmado e pago pelo consumidor, os dados podem ser salvos no banco de dados relacional. De forma semelhante, a informação de sessão do usuário também é consultada pelo ID do usuário. Dessa forma, o banco de dados relacional não será utilizado para armazenar dados transientes. 

A utilização de um banco de dados chave-valor faz com que a carga no banco de dados relacional seja aliviada, conforme arquitetura disposta na figura abaixo:

![Com Riak](https://dl.dropboxusercontent.com/u/33955026/e-commerce1.jpg)

A diminuição da carga no banco de dados culminará em um melhor desempenho na aplicação como um todo. O desempenho será aumentado não só pela diminuição da carga, como também pela facilidade com que os bancos chave-valor têm de lidar com as estruturas armazenadas neles. Bancos relacionais não são tão performático quanto bancos chave-valor para lidar com estruturas em hash/mapa.

Se fôssemos enumerar as possibilidades de utilização de múltiplos bancos de dados com estruturas diversas, o artigo seria demasiadamente extenso, uma vez que há uma miríade de soluções de armazenamento possíveis. O importante é compreender que a tendência de agora em diante é utilizar bancos de dados que resolvem determinados problemas de forma nativa, ou seja, são projetados especificamente para aquele tipo de problema.

A chegada dos produtos NoSQL é um desafio para programadores, arquitetos de software e DBAs. É preciso projetar com inteligência e muito embora as aplicações fiquem mais complexas do ponto de vista arquitetural, serão muito mais performáticas e escaláveis do que em arquiteturas com um único banco de dados. Os DBAs terão de aprender a administrar bancos de dados que falam outras línguas além do SQL, como por exemplo, o CQL do Cassandra. Os arquitetos terão que projetar as aplicações levando em conta os requisitos não funcionais e que dados devem ser armazenados em quais bancos de dados. Os programadores terão que aprender a manipular dados que utilizam as mais diversas estruturas. É um mundo completamente novo e que tem que ser desbravado, principalmente se olharmos dentro do contexto da DATAPREV, que ainda não faz uso de soluções NoSQL.

Ao se escolher quaisquer tecnologias dentro de uma empresa, vai chegar um momento em que será preciso lidar com questões como licenças, ferramentas, drivers, auditoria, segurança, entre outros. Entretanto, a grande maioria das soluções NoSQL são open-source, com comunidade de desenvolvedores bastante ativa, inclusive com companhias que fornecem suporte comercial. Alguns banco de dados possuem boas ferramentas para trabalhar e outros não. É preciso escolher bem.

Uma outra questão é em relação à segurança da informação, uma vez que a maioria dos bancos de dados NoSQL não possuem funcionalidades muito robustas no que se refere a segurança de dados, especialmente na possibilidade de criar usuários e atribuir privilégios. A responsabilidade da segurança da informação fica a critério da aplicação.

Por fim, existe uma forte tendência de utilizar bancos de dados NoSQL para fins de Business Intelligence e sistemas analíticos no geral por serem muito mais performáticos que bancos relacionais utilizados para esse fim. Entretanto, muitas empresas já utilizam ferramentas ou outros mecanismos de extração de dados e é preciso garantir que esses mecanismos possam falar com bancos NoSQL. Existem ferramentas como o Pentaho, que é capaz de falar com vários bancos de dados NoSQL.

O desafio é muito grande e depende de bastante capacitação. Entretanto, acredito que a DATAPREV tem mentes capacitadas para lidar com esse novo desafio de criar aplicações modernas voltadas para o alto desempenho em clusters, fazendo uso da persistência poliglota.




## Referências
<Lista referências bibliográficas, matérias na intranet, ferramentas internas etc>


n/
</markdown></p>
