---
remark: metadados para a ser usado pelo parser de conversão para pdf
date: 27 de junho de 2014
tipo_artigo: Artigo técnico de Infraestrutura de TIC
title: Implantação de Alta Disponibilidade para as Aplicações do MTE
abstract: Este artigo apresenta um resumo do trabalho realizado para implantar o ambiente de alta disponibilidade para as aplicações do MTE, utilizando JBoss EAP 6.1 e JAVA 6.
author:
- affiliation: DSAA
  name: Álvaro Teixeira Gonçalves
responsibility:
- affiliation: DSAA
  name: Claudio Yuassa Tokoro
diretoria: 'Diretoria de Infraestrutura de TIC - DIT'
superintendencia: 'Superintendência de Planejamento e Suporte de TIC - SUPS'
departamento: 'Departamento de Suporte de TIC - DEST'
tags:
- Tech0xA
- JBoss
- EAP
- Java
- disponibilidade
- MTE
...

Introdução
==========

O servidor de aplicação JBoss EAP 6.1 juntamente com o JAVA 6 proveem recursos para ambientes robustos, de alto desempenho e alta disponibilidade. Por esse motivo estas foram as tecnologias escolhidas e utilizadas para as aplicações do MTE.

Desafios
========

Implantar INFRA com suporte à alta disponibilidade para as aplicações do MTE em plataforma atualizada e compatível com replicação de sessão.

Benefícios e/ou recomendações
=============================

Este artigo apresenta o trabalho realizado.

O Cliente MTE
=============

O Cliente MTE atualmente possui uma representação significativa para a DATAPREV:
- São mais de 7.100 Pontos de Atendimento.
- Acesso via WEB e através dos Postos de Atendimento cadastrados pelo MTE. 
- Média de 200.000 Acessos/Atendimentos diários

Os sistemas/aplicações do MTE
=============================

O Cliente MTE hospeda as seguintes aplicações (on-line) nos ambientes da DATAPREV:
- IMO - Intermediação de Mão-de-Obra.
- SD - Seguro Desemprego.
- CAGED - Cadastro Geral de Empregados e Desempregados.
- CBO - Classificação Brasileira de Ocupações.
- PROGER - Programa de Geração de Emprego e Renda.
- GC / PNQ - Gestão de Convênios
- SPPE - Portal MTE
- SAA - Sistema de Autorização e Acesso (futuramente será substituído pelo GERID)

A Proposta
==========
 
Nosaa proposta consiste em implantar uma nova infraestrutura:

Antes da Implantação:
---------------------

- Servidores de Apresentação APACHE v2.2.15 com Mod_JK.
- Servidores de Aplicação JBoss v.4.2.2-GA. 
- JAVA 5.
- Servidores RHEL 5.0 - 64 bits.

Depois da Implantação:
----------------------

- Servidores de Apresentação APACHE v2.2.15 com Mod_Cluster.
- Servidores de Aplicação JBoss EAP 6.1. 
- JAVA 6.
- Servidores RHEL 6.3 - 64 bits.

Desvantagens da INFRA antes da implantação:
-------------------------------------------

- Versão dos Servidores de Aplicação (JBoss) desatualizada.
- Versão do JAVA muito antiga e em desuso.
- Tipo de balanceamento.
- Recuperação do serviço não existe e o usuário perde sempre sua sessão (retrabalho).
- Gerenciamento descentralizado.

Vantagem da INFRA proposta:
---------------------------

- Versão dos Servidores de Aplicação (JBoss) atualizada.
- Versão do JAVA atualizada e já atendendo novas funcionalidades das aplicações.
- Tipo de balanceamento - Inteligente e dinâmico, com cálculos efetuados nas informações dos servidores de aplicação e apresentação.
- Recuperação do serviço com recuperação de falhas (INFRA capaz de efetuar a replicação da sessão do usuário).
- Gerenciamento Centralizado.
- Elasticidade do Ambiente.

Esforço Envolvido na Implantação:
---------------------------------

- Necessidade de adaptação em todas as aplicações para que funcionem no novo ambiente.
- Instalação e Configuração dos softwares em todos os servidores criados para atender todos os ambientes (desenvolvimento, homologação, testes automatizados, treinamento e produção).
- Configuração dos Alertas e Itens de Monitoramento dos novos ambientes.
- Sincronização do Cronograma do Projeto com as datas já pré-acordadas com o Cliente.

Ganhos adicionais obtidos com a implantação:
============================================

- Conexões SSL fechadas diretamente no switch de conteúdo.
- Segregação TOTAL do Tráfego INTERNET do Tráfego dos Postos de Atendimento
- Ambiente de Desenvolvimento com total autonomia da UD.
- Facilidade de Provisionamento

Conclusão
=========

- Ambiente preparado e apto para implantação de replicação de sessão de acordo com o Plano de Ação 2014 e com todas as certificações do padrão J2EE 6.
- Servidores com melhor capacidade e maior robustez para um melhor atendimento do Cliente.
- Total integração com a tecnologia de CLOUD COMPUTING (nuvem) adotada pela DATAPREV.

Referências
===========

---
remark: metadados com alguns dados para listar referências bibliográficas. Use quantos identificadores (ID) necessitar para listar as diferentes referências usadas no artigo
references:
- id: Manual
  title: "JBoss EAP 6.1 Administration and Configuration Guide"
  author: Red Hat
  - family: EAP
    given: JBoss
  container-title:
  URL: 'https://access.redhat.com/site/documentation/en-US/JBoss_Enterprise_Application_Platform/6.2/html-single/Administration_and_Configuration_Guide/index.html'
  accessed:
    day: 29
    month: abr.
    year: 2014
  publisher: Red Hat.
  type: ebook
  issued:
    year: 2014
    month: abr.
...