---
date: 28 de fevereiro de 2014
tipo_artigo: Artigo técnico de Infraestrutura de TIC
title: Mascaramento de dados – O Caso CNIS
abstract: 'Em vista da necessidade de se manter a confidencialidade dos dados do cliente, a provisão de um grande volume de dados reais para o desenvolvimento e teste de aplicações é um dos grandes desafios encontrados na Dataprev.  
Testes ganham em qualidade quando realizados com informações verídicas, mas ao mesmo tempo é vital que - ao serem disponibilizados em bancos de dados com controle de acesso menos restrito - estas sejam protegidas de visualização e identificação por parte dos desenvolvedores.  
O Oracle Data Masking endereça este problema através de funcionalidades que propõem trazer flexibilidade e usabilidade ao processo de definição e execução da descaracterização de dados; buscando proteger informações reais enquanto estas estejam disponíveis para realização do desenvolvimento e teste dos sistemas.'
author:
- affiliation: SUPS
  name: Matheus Correia Ferreira
responsibility:
- affiliation: DIPT
  name: Bruno Cesar Cardoso Maria
diretoria: 'Diretoria de Infraestrutura de TIC - DIT'
superintendencia: 'Superintendência de Planejamento e Suporte de TIC - SUPS'
departamento: 'Departamento de Arquitetura Técnica - DEAT'
tags:
- Dados
- Mascaramento
- Sigilo
- Informações
...

# Desafios

As Empresas devem buscar mecanismos para proteger os dados que estão sob sua guarda, uma vez que é de suma importância a confidencialidade das informações de seus clientes. Estas informações podem ser, entre outras, de propriedade intelectual, dados de identificação de usuários ou informações classificadas como restritas.

Muitas vezes, para propósitos de desenvolvimento, homologação e testes de aplicações, surgem cenários nos quais a utilização de dados reais de produção torna-se necessária. Entretanto, muitas dessas informações não podem ser simplesmente copiadas para esses ambientes devido ao fato de que - por definição - bancos de dados de desenvolvimento, homologação e testes de aplicação podem e devem ser acessados com facilidade para validação das funcionalidades do sistema.  

Dessa forma, a existência de dados reais no seu estado bruto nesses ambientes ocasionaria graves problemas de segurança e confidencialidade. Deve-se, portanto, buscar uma solução que facilite a disponibilização de grandes volumes de dados descaracterizados para testes e desenvolvimento; protegendo as informações do cliente e suportando validações nas quais a aplicação deverá tratar dados que se assemelham tanto em quantidade quanto em natureza aos valores existentes em um ambiente de produção.

# Benefícios

- Geração de dados totalmente funcionais com características semelhantes aos dados originais;
- Reaproveitamento de scripts PL/SQL com operações de mascaramento de dados;
- Disponibilização de uma biblioteca de formatos de mascaramento padronizada;
- A automação do processo de mascaramento de dados, através da inclusão dos scripts PL/SQL com operações de mascaramentos de dados em jobs a serem agendados. 

# Introdução

Empresas que lidam com tecnologia da informação devem sempre zelar pela confidencialidade dos dados recebidos e tratados pelos sistemas que estão sob sua responsabilidade. Devido a esse importante requisito da segurança da informação, o acesso a muitos desses dados deve ser permitido apenas às pessoas com os devidos privilégios.

Entretanto, algumas situações que surgem naturalmente durante o ciclo de desenvolvimento de um sistema requerem que estejam disponibilizados, em geral para a realização de diferentes tipos de testes, dados que sejam semelhantes às informações que a aplicação tratará quando for movida para um ambiente produtivo. Ao mesmo tempo que esses dados devem manter características de formato e integridade, a natureza de seu conteúdo deve ser modificada para que qualquer identificação de seu valor real seja inviável.

O problema ganha ainda mais complexidade quando considera-se que, em geral, sistemas da Dataprev possuem grandes volumes de dados. Logo, para que o desempenho de aplicações seja corretamente aferido, é vital que o volume de dados em bancos de dados destinados a tais verificações seja o mais próximo possível do real.

Cria-se então uma situação na qual é imperativa a existência de grandes volumes de dados reais em diversos ambientes e - simultaneamente - se deva garantir que o estado dessas informações respeite os princípios de confidencialidade requeridos e esperados pelos clientes.

É interessante que essas informações descaracterizadas sejam providas através de um processo simples, rápido e bem definido. A option Oracle Data Masking [@OraDataMaskingSensitive, pp. 16-1 a 16-26] busca atender a essas necessidades oferecendo recursos para a substituição de dados sensíveis por dados fictícios. Sua grande flexibilidade para definição de estratégias de descaracterização traz alto grau de customização para as operações de mascaramento e permite que configurações sejam definidas de maneira aderente ao que requerem os dados a serem processados.

Acessível via Oracle Enterprise Manager, esta option oferece uma solução de automação completa para o provisionamento de base de dados de testes criadas a partir de bases de produção.

# Mascaramento de Dados

O mascaramento de dados é o processo de substituição de informações sensíveis por dados transformados porém acessíveis pelas aplicações. O processo de descaracterização é baseado em regras de mascaramento que são definidas em uma biblioteca central.  

A importância do mascaramento de dados surge quando ocorre o provisionamento de ambientes de testes, homologação, e outros a partir de ambientes de produção. Estes ambientes são acessados por usuários internos e externos, e não é desejável ou mesmo permitido o acesso destes a informações sigilosas e sensíveis.

    Figura 1: Exemplo de mascaramento de dados

## Dados Sensíveis

Dados sensíveis são aqueles classificados como confidenciais, aqueles regulamentados por normas de segurança da informação, por políticas governamentais ou aqueles que devem estar de acordo com práticas estabelecidas por regras de negócio dos sistemas.

Cada organização deve determinar quais dados são classificados como sensíveis, estando em acordo com as regulamentações específicas daquela empresa, do governo e das normas de segurança vigente.

Uma lista contendo os dados que são considerados sensíveis deve ser publicada corporativamente, tendo o aceite de todas as áreas envolvidas. 

Um lista padrão contendo dados sensíveis pode incluir os exemplos abaixo: 

- Nome pessoal; 
- Nome do cliente; 
- Número do empregado; 
- Número da conta bancária; 
- Número do cantão de crédito; 
- Número de identificação civil.

## Implementando o Mascaramento de Dados

A Oracle desenvolveu [@OraDataMaskingBestPratice] uma abordagem que envolve 4 etapas para a implementação do mascaramento de dados. Estas etapas são: 

1. Procurar: Esta fase envolve a identificação e catalogação de dados sensíveis ou regulamentados através de toda empresa. O objetivo deste exercício é obter uma lista completa de elementos de dados sensíveis específicos para a organização e descobrir as tabelas e colunas associadas em todas as bases de dados que contêm os dados sensíveis.   
2. Avaliar: Nesta fase ocorre a identificação dos algoritmos de mascaramento que representam as técnicas ideais para substituir os dados sensíveis originais.   
3. Segurança: Este e os próximos passos podem ser iterativos. O processo de mascaramento é executado para proteger os dados confidenciais através de tentativas de mascaramento sobre os dados sensíveis. Uma vez que o processo de mascaramento é concluído, o ambiente para teste é liberado para testes da aplicação.   
4. Teste: A aplicação é testada com os dados mascarados, para saber se estes podem ser entregues a outros usuários que não sejam de produção. Se a rotina tiver que ser ajustada, a base de dados é restaurada ao estado pré-mascarado, os algoritmos de mascaramento são reavaliados e o processo de mascaramento é reexecutado.

    Figura 2: Passos do processo de mascaramento de dados

## Oracle Enterprise Manager

O Oracle Enterprise Manager é uma solução integrada, que permite a automação do gerenciamento, da monitoração, da manutenção e disponibilidade de um ambiente corporativo de banco de dados e aplicações. O Oracle Data Masking é um pacote integrado ao Oracle Enterprise Manager.

## Oracle Data Masking

Esta option oferece uma solução para provisionamento de base de dados de testes criadas a partir de bases de produção, oferecendo recursos para a substituição de dados sensíveis por dados fictícios.

A execução do mascaramento de dados através do Oracle Data Masking é, basicamente, realizada através de quatro passos:

- Criação de formato de mascaramento
- Criação de definição de mascaramento
- Geração do script do mascaramento
- Execução do script

Com a realização dessas quatro etapas, é possível realizar a descaracterização tanto de colunas de uma determinada tabela quanto de um banco de dados completo.

### Biblioteca de Formatos de Mascaramento

A biblioteca de formatos de mascaramento contém uma coleção de formatos  prontos para serem utilizados. Eles definem o processo que será usado para transformar dados reais em informações mascaradas.

A criação de um formato é realizada através da escolha entre um ou mais tipos de formato que são disponibilizados pelo Oracle Data Masking.

A tabela 1 lista os tipos disponíveis e traz uma breve descrição de cada um.

Alguns tipos de mascaramento listados são combináveis. Ou seja, eles podem ser combinados com outros tipos de mascaramento para gerar máscaras mais complexas. É possível, por exemplo, para um campo do tipo VARCHAR, criar um formato cujo valor de saída seja a concatenação de um número aleatório “Random Numbers” com uma string aleatória “Random Strings”.


---------------------------------------------------------------------------------------
Tipo                    Descrição
----------------------- ---------------------------------------------------------------
Array List              Troca valor da coluna por um dos valores em lista definida pelo usuário

Delete                  Deleta o registro por completo (em geral, depende de condições)

Fixed Number            Troca valor da coluna por um número fixo definido pelo usuário

Fixed String            Troca valor da coluna por uma string fixa definida pelo usuário

Null Value              Troca valor da coluna por valor nulo

Preserve Original Data  Preserva o valor original da coluna

Random Dates            Troca valor da coluna por data aleatória gerada

Random Decimal Numbers  Troca valor da coluna por número decimal aleatório

Random Digits           Gera valores dentro de um intervalo de número de dígitos especificado

Random Numbers          Gera números dentro de um intervalo de valores determinado

Random Strings          Gera strings dentro de um intervalo de número de caracteres especificado

Shuffle                 Realiza o embaralhamento dos valores de uma determinada coluna

SQL Expression          Expressões simples em SQL são usadas para mascarar os dados

Substitute              Utiliza um método de substituição baseado em uma função Hash

Substring               Gera substrings de acordo com valores de posição inicial e comprimento

Table Column            Seleciona os valores de uma coluna específica para realizar o mascaramento

Truncate                Deleta todos os dados contidos em uma coluna independente de condições

User-Defined Function|   Mascaramento é feito com uma função PL/SQL criada pelo próprio usuário
---------------------------------------------------------------------------------------

Tabela 1: Passos do processo de mascaramento de dados

### Definições de Mascaramento

Uma definição de mascaramento define uma operação de descaraterização de dados a ser implementada em uma ou mais tabelas de uma base de dados. 

Enquanto formatos de mascaramento meramente definem os tipos de formatos que serão usados, as definições são as responsáveis pela definição do processo de mascaramento, uma vez que elas atrelam um ou mais formatos a colunas de tabelas de um banco de dados.

Uma nova definição de máscara pode ser criada ou uma definição já existente pode ser utilizada para uma operação de mascaramento. Para criar uma nova definição de mascaramento, especifica-se a coluna da tabela para a qual os dados devem ser mascarados e o formato de mascaramento. 
	
Além de criar o relacionamento entre colunas e formatos, as definições de mascaramento são responsáveis por duas das principais funcionalidades do Oracle Data Masking: a manutenção da integridade referencial de campos mascarados; e a possibilidade da construção de processos de mascaramento condicionais, que adicionam mais flexibilidade e customização às opções de mascaramento.

A integridade referencial é mantida de maneira automática [segundo @DTPTechReviewSTPB072013]. Ao selecionar uma coluna que seja referenciada por outras tabelas, o Oracle Data Masking automaticamente lista todas essas chaves estrangeiras e realiza a sua descaracterização em conjunto com a chave original, fazendo com que o resultado do mascaramento de determinado valor seja igual para todas as colunas interligadas.

    Figura 3: Mascaramento com integridade referencial

Ocasionalmente, é possível que existam colunas em tabelas diferentes que sejam dependentes das colunas mascaradas sem que essa relação esteja declarada no banco de dados através de referências. Nesse caso, o Oracle Data Masking permite que o usuário especifique quais colunas são essas para que o processo de descaracterização também respeite essas relações.

Por sua vez, o mascaramento condicional é facilmente configurável através da interface da option e permite que uma mesma coluna seja mascarada por diferentes tipos de formato escolhidos de acordo com valores de demais campos.
	
Por exemplo, é possível especificar que, os salários de funcionários somente serão mascarados se ultrapassarem um valor especificado, ou que registros de pessoas que ocupam cargos de direção devem ser deletados por completo enquanto que os demais funcionários terão seus dados descaracterizados.

    Figura 4: Mascaramento condicional

### Geração e Execução do Script de Mascaramento

Com as informações contidas na definição do mascaramento, o Oracle Data Masking gera um script que descreve passo a passo o processo de descaracterização que será realizado.

É possível visualizar tanto um sumário do script, que é uma lista dos comandos de banco de dados que serão usados para mascarar as colunas selecionadas, ou o script completo, que - no formato PL/SQL - inclui funções, procedimentos, e outros comandos que serão necessários durante a operação.

O script pode ser executado imediatamente, agendado para um momento posterior, ou salvo em formato “.sql” para futura execução manual.
	
Por fim, é possível selecionar se o mascaramento será realizado sob a própria tabela que foi utilizada para a especificação da definição de mascaramento, fazendo com que a tabela e valores originais sejam perdidos; ou se as tabelas a serem descaracterizadas devem ser clonadas para que o processo seja realizado sobre seus clones. De acordo com a opção selecionada, o Oracle Data Masking faz as alterações necessárias no script.

# Conclusão

Para a realização de testes funcionais e de performance, é vital que seja possível – com facilidade – prover consideráveis volumes de dados reais aos desenvolvedores e testadores que utilizarão os ambientes apropriados para estas tarefas.

Como deve-se sempre prezar pela confidencialidade das informações do cliente, torna-se muito importante que seja implementado um processo claro e bem definido para que esses dados sejam disponibilizados de uma maneira que preserve a integridade da base de dados enquanto elimina qualquer possibilidade de identificação dos dados verídicos.

O Oracle Data Masking contém uma grande gama de opções que permitem dar flexibilidade às configurações de descaracterização dos dados, fazendo com que as diversas particularidades e necessidades de cada base de dados sejam atendidas pelo conjunto de estratégias de mascaramento disponíveis.

Ambientes destinados a testes e desenvolvimento podem, então, trazer representações fiéis do que a aplicação encontrará em um ambiente produtivo. Dessa forma, não só existem ganhos consideráveis no valor agregado aos sistemas durante o seu ciclo de desenvolvimento, como também são respeitadas a segurança e a confidencialidade das informações dos clientes da empresa.

# Referências {.allowframebreaks}

---
references:
- id: OraDataMaskingSensitive
  title: "Oracle Database Real Application Testing User's Guide, 11g Release 2 (11.2)"
  author:
  - family: Chan
    given: Immanuel
  - family: Zampiceni
    given: Mike
  container-title: Database
  volume: 11g 2
  URL: 'http://docs.oracle.com/cd/E11882_01/server.112/e41481/tdm_data_masking.htm'
  issue: 4
  publisher: Oracle Corporation
  page: 16.1-16.26
  type: book
  language: pt-BR
  issued:
    year: 2013
    month: 7

- id: OraDataMaskingBestPratice
  title: "Data Masking Best Practice"
  author:
  - family: Ahmed
    given: Waleed
  - family: Athreya
    given: Jagan
  container-title: Database
  volume: 12c
  URL: 'www.oracle.com/us/products/database/data-masking-best-practices-161213.pdf'
  issue: 4
  publisher: Oracle Corporation
  page: 11-14
  type: article
  issued:
    year: 2013
    month: 6

- id: DTPTechReviewSTPB072013
  title: "Parecer Técnico Oracle Data Masking"
  author:
  - family: Pickel
    given: Ana Cristina Lobo
  container-title: Database
  URL: ' http://www-arquitetura/index.php?q=node/249'
  publisher: Dataprev
  page: 1-6
  type: article
  issued:
    year: 2013
    month: 7
...
