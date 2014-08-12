---
remark: metadados para a ser usado pelo parser de conversão para pdf
date: 18 de março de 2014
tipo_artigo: Artigo técnico de Infraestrutura de TIC
title: Novo Deployment Pipeline da Dataprev
abstract: O Deployment Pipeline é a materialização do Processo de Entrega Contínua da Dataprev. Consiste em um conjunto de estágios sequenciais, atuando desde checkout do código-fonte de um produto até sua implantação nos ambientes corporativos. Assim como ocorre numa linha de montagem industrial, os produtos devem percorrer uma "esteira de produção" até alcançar seu estágio final, onde uma nova versão do produto é lançada, desde que atinja os critérios mínimos de qualidade exigidos.
author:
- affiliation: DEAT/DIAS
  name: Flávio Augusto Almeida Valones Xavier
responsibility:
- affiliation: DEAT/DIAS
  name: Cícero Soares Vieira
diretoria: 'Diretoria de Infraestrutura de TIC - DIT'
superintendencia: 'Superintendência de Planejamento e Suporte de TIC - SUPS'
departamento: 'Departamento de Arquitetura Técnica - DEAT'
tags:
- Integracao Continua
- Entrega Continua
- Deployment Pipeline
- DevOps
- Automacao
- Qualidade
...
	 
Desafios e Benefícios
=====================
 
Este trabalho visa definir os pilares base para evolução do atual ambiente de integração contínua. É importante que as mudanças sejam inseridas de forma gradual, para que seja possível se adaptar a nova filosofia de trabalho sem inserir uma sobrecarga de novos requisitos de uma só vez. Vale salientar que o ambiente fornece as ferramentas mas não executa todas as atividades do processo sozinho, é preciso empenho das áreas envolvidas, provendo alguns requisitos como: testes unitários, testes de desempenho, massa de dados para testes, ambientes de execução de testes, configurações dos ambientes e aplicações, etc. O objetivo final deste trabalho é alcançar os seguintes benefícios, dentre outros:

- Automatizar e padronizar o ciclo de vida de desenvolvimento e implantação dos produtos, reduzindo necessidade de esforço manual;
- Agilizar o processo dos ciclos de lançamento, reduzindo o tempo necessário para entregar novas versões;
- Garantir um nível mínimo de qualidade para os produtos;
- Permitir lançar uma nova versão a qualquer momento;
- Garantir o rastreamento entre a versão do código-fonte e a versão dos binários;
- Melhorar a integração entre as equipes de desenvolvimento, QA e operações (DevOps);
 
Introdução
==========
 
Integração Contínua @ThoughtWorksCI é a prática de integrar e testar o novo código produzido em cada mudança em relação a base de código existente. Consiste em um conjunto de boas práticas  como automação de compilação, teste contínuo e análise de qualidade de código. Entrega Contínua (@ThoughtWorksCD e @XebiaCDE) vai mais além e automatiza a implantação de software em QA, ambientes de pré-produção e produção. Entrega Contínua permite que as organizações possam implantar produtos a qualquer momento, automatizando o processo através de um Deployment Pipeline, reduzindo os riscos envolvidos, a necessidade de esforço manual e o tempo total dos ciclos lançamento.

O Deployment Pipeline, por sua vez, necessita que algumas premissas básicas sejam atendidas:

- Código gerenciado em um sistema de controle de versões;
- Compilação e empacotamento do código executado de forma centralizada e automatizada;
- Testes automatizados e tratados como parte integrante do ciclo de desenvolvimento;
- Aplicações implantadas de forma automática, em um ou mais ambientes;

O Deployment Pipeline é organizado em estágios sequenciais, por sua vez subdivididos em grupos de tarefas, executadas por um conjunto de ferramentas distintas operando de forma integrada. Funciona como uma linha de montagem industrial, os produtos percorrem uma *"esteira de produção"*, se ocorrer alguma falha ao longo da *"esteira"*, deve-se descartar a versão corrente, corrigir as falhas encontradas e reiniciar o processo. Se tudo correr bem, ao final da esteira tem-se uma nova versão do produto aprovada segundo os critérios mínimos de qualidade.
 
Estágios do Deployment Pipeline
===============================

Inicialmente o Deployment Pipeline será composto de apenas dois estágios, mas futuramente serão adicionadas gradativamente novas etapas, afim de cobrir outras funcionalidades, como testes de desempenho, testes de aceitação manuais, etc.

A figura abaixo apresenta o Deployment Pipeline inicial:

![Deployment Pipeline da Dataprev](imagens/pipeline.png)

Estágio Inicial: Commit Stage
-----------------------------

Este estágio basicamente abrange a execução das práticas da Integração Contínua. O processo inicia-se com os desenvolvedores efetuando *"commit"* de mudanças no sistema de controle de versões (VCS em inglês). Neste ponto, o sistema de Integração Contínua (IC) responde ao *"commit"*, desencadeando uma nova instância do pipeline. O primeiro estágio do pipeline compila o código, executa testes de unidade, realiza a análise do código. Se todos os testes passarem e o código for aprovado, o código executável é empacotado em arquivos binários e armazenado em um repositório de artefatos. 

Este estágio é subdividido nas seguintes tarefas:

1. **Checkout do código-fonte a partir do VCS:** A ferramenta utilizada oficialmente pela DRD será o Starteam^[Starteam (http://www.borland.com/products/starteam/)], e pela DIT será o GIT^[GIT (http://git-scm.com/)], porém outras ferramentas , como o CVS, também são suportadas.
2. **Compilação do código e execução dos testes unitários:** O Maven^[Maven (http://maven.apache.org/)] é a ferramenta atualmente adotada, mas outras opções são suportadas (Gradle ou Ant + Ivy). Já os testes unitários são construídos com o framework JUnit^[JUnit (http://junit.org/)]. As dependências necessárias para compilação  e execução dos testes são obtidas a partir do gerenciador de repositórios Nexus^[Nexus (http://www.sonatype.org/nexus/)]. 
3. **Análise estática do código:** O SonarQube^[SonarQube (http://www.sonarqube.org/)] avalia diversas métricas de qualidade do código baseada na avaliação de um conjunto de plugins utilizados internamente pela ferramenta (PMD, Checkstyle, Findbugs, Squid, Jacoco, dentre outros);
4. **Geração e Publicação dos Pacotes:** O Maven gera os pacotes e os publica no Nexus;
5. **Versionamento dos Fontes:** código-fonte recebe Tag correspondente a versão do pacote gerado;


Acceptance Stage
----------------

O segundo estágio do pipeline é composto pelos testes de aceitação automatizados de execução mais prolongada. O servidor de IC efetua a implantação da aplicação em um ambiente de testes e então invoca a execução da suíte de testes de aceitação através de uma ferramenta de gerenciamento dedicada a este propósito. Esta etapa será acionado automaticamente com a conclusão bem sucedida da primeira fase do pipeline. Inicialmente será utilizado um ambiente pré-alocado, posteriormente este ambiente deverá ser provisionado automaticamente através da ferramenta Puppet[^1]. 

Este estágio executa as seguintes tarefas:

1. **Implantação da Configuração da aplicação:** A ferramenta utilizada ainda deve ser definida, podendo ser o ITCM^[CA IT Client Automation (http://www.ca.com/us/~/media/files/solutionbriefs/it_client_mgr_sb_154008.aspx)], Puppet^[Puppet (http://puppetlabs.com/)] ou Rundeck^[Rundeck (http://rundeck.org/)];
2. **Implantação dos pacotes em ambiente de testes:** mesmo caso da tarefa anterior, ITCM ,Puppet ou Rundeck;
3. **Limpeza e povoamento do Banco de Dados com massa de testes:** Checkout VCS + framework Java (ex: DBUnit, Flyway, LiquidBase);
4. **Execução dos testes de aceitação automatizados (funcionais, interface, integração):** Silk Central^[Silk Central http://www.borland.com/products/silkcentral/)]; em conjunto com o Silk Test;


Ferramentas do Deployment Pipeline
==================================

O conjunto de ferramentas de automação necessárias para viabilizar o Deployment Pipeline inicial deve ser composto por:

- **Coordenação de Pipeline/Release**, que define e orquestra os estágios no Deployment Pipeline, atribuindo os responsáveis por executar cada tarefa, coordenando e acompanhando todo o processo de gerenciamento necessário para gerar uma nova versão de um produto. Esta tarefa será desempenhada por plugins instalados na ferramenta Jenkins;
- **Integração Contínua**, que lida com o checkout do código-fonte do VCS, a construção, execução dos testes unitários, agregação dos componentes da release e do empacotamento dos binários. Esta tarefa será desempenhada pelo próprio Jenkins^[Jenkins (http://jenkins-ci.org/)];
- **Repositório de Binários**, responsável por armazenar e versionar as releases produzidas no Deployment Pipeline. A ferramenta responsável pelo gerenciamento de repositórios será o Nexus;
- **Gerenciador de Provisionamento/Configuração**, que trata da criação e configuração sob demanda dos ambientes de destino. Este item não fará parte da versão inicial, mas será incluído em versões futuras e utilizará a ferramenta Puppet;
- **Automação de Deployment**, que trata da distribuição e implantação dos binários nos ambientes de  Desenvolvimento, testes, controle de qualidade, etc. Esta tarefa será desempenhada pelo ITCM ,Puppet ou Rundeck;
- **Automatização de Testes**, que trata da execução automatizada dos diversos tipos de testes, como testes unitários, de integração, funcionais, de regressão, de desempenho, etc. Esta tarefa será desempenhada pela ferramenta SilkCentral, que se integra com as demais ferramentas de execução de testes (SikTest, SilkPerformer, etc.).
 
Conclusão
=========
 
Como se pode perceber neste artigo, o Deployment Pipeline disponibiliza os recursos pra a implementação da Entrega Contínua, mas não é autossuficiente e precisa do empenho das várias áreas envolvidas no processo para que possa ser efetivado de fato. É importante também inserir essas mudanças de forma gradual para que sua adoção não se torne algo impraticável. Todos os requisitos e como proceder para utilizar o novo ambiente serão detalhados no novo **Processo de Entrega Contínua** (em desenvolvimento).
 
Referências
===========

[^1]: [@PuppetLabseBook] 
 
---
remark: metadados com alguns dados para listar referências bibliográficas. Use quantos identificadores (ID) necessitar para listar as diferentes referências usadas no artigo
references:
- id: PuppetLabseBook
  title: "Continous Delivery: What It Is and How to Get Started"
  URL: 'https://puppetlabs.com/sites/default/files/CDebook.pdf'
  accessed:
    month: 3
    year: 2014
  publisher: Puppet Labs
  type: book

- id: ThoughtWorksCI
  title: "Continuous Integration"
  URL: 'http://www.thoughtworks.com/pt/continuous-integration'
  type: webpage
  publisher: ThoughtWorks, Inc.
  accessed:
    year: 2013
    month: 03
    
- id: ThoughtWorksCD
  title: "Continuous Delivery"
  URL: 'http://www.thoughtworks.com/pt/continuous-delivery'
  type: webpage
  publisher: ThoughtWorks, Inc.
  accessed:
    year: 2013
    month: 03
    
- id: XebiaCDE
  title: "Introducing Continous Delivery in the Enterprise"
  URL: 'http://continuousdelivery.xebia.com/sites/default/bestanden/nl/Whitepaper%20Xebia%20Continuous%20Delivery.pdf'
  type: article
  publisher: Xebia Nederland b.v.
  accessed:
    year: 2013
    month: 03

...
