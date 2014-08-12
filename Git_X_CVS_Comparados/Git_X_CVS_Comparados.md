---
remark: metadados para a ser usado pelo parser de conversão para pdf ou odt
date: 28 de fevereiro de 2014
tipo_artigo: Artigo técnico de Infraestrutura de TIC
title: Git X CVS um comparativo entre sistemas de controle de versão centralizado e descentralizado.
abstract: Bem, pessoal. É sabido que estamos adotando o Git, um sistema de controle de versão descentralizado, para suprir necessidades de gerenciamento de fontes, a princípio, nas áreas de Suporte e Sustentação. Este sistema irá subsidiar o funcionamento de projetos bem maiores, começando pelo sistema de automação de configurações e gerenciamento/provisionamento de servidores. Este artigo tem por objetivo, fazer um comparativo entre o Git e o nosso bem conhecido CVS, clareando os entendimentos do que é o novo sistema.
author:
- affiliation: DEST
  name: Alex de Castro Araujo
responsibility:
- affiliation: DEST
  name: Diogo Costa Martins Pizaneschi
diretoria: 'Diretoria de Infraestrutura de TIC - DIT'
superintendencia: 'Superintendência de Planejamento e Suporte de TIC - SUPS'
departamento: 'Departamento de Suporte de TIC - DEST'
tags:
- controle de versão
- distribuído
- fontes
- infraestrutura
- git
...

Desafios
========

Neste artigo, abordaremos características e funcionalidades do Git e CVS de forma clara, dando uma visão geral do que é o Git.
Iniciaremos com um resumo do que são estes dois sistemas. e os benefícios da adoção de um sistema de versionamento descentralizado. 

Benefícios
==========

Bem, pessoal. É sabido que estamos adotando o Git, um sistema de controle de versão descentralizado, para suprir necessidades de gerenciamento de fontes, a princípio, nas áreas de Suporte e Sustentação. Este sistema irá subsidiar o funcionamento de projetos bem maiores, começando pelo sistema de automação de configurações e gerenciamento/provisionamento de servidores.


Introdução
==========

O objetivo deste artigo é fazer um comparativo entre o Git e o nosso bem conhecido CVS, clareando os entendimentos do que é o novo sistema.
A princípio, todos os sistemas de versionamento obedecem basicamente a algumas premissas: Manter arquivos de dados em repositórios centralizados ou descentralizados, de forma a compartilhá-los, mantendo controle de versões e alterações, bem como o histórico de suas mudanças. As diferenças estão na interface, funcionalidades extras e sobretudo, segurança e performance.

Todavia, iremos tentar de forma clara e objetiva, identificar as características e diferenças dos dois sistemas e, por fim mostrar brevemente o funcionamento do Git, usando como referência [@ID-GitDoc] e [@GitBottomUp2009].


Resumo comparativo
==================

Em um breve resumo comparativo, começando pelo CVS, um ótimo sistema centralizado, no modelo cliente-servidor. Podemos ressaltar como principais pontos positivos sua Maturidade - Está em uso desde o início dos anos 80; E, por ser centralizado, torna mais simples políticas e controle de acesso.

Os pontos negativos mais marcantes, podemos citar a baixa performance com operações em branches e não implementar transações atômicas. Isto significa que, se o servidor cair durante um commit longo, você pode corromper dados no repositório. Não é uma situação comum, mas possível;

O GIT é um sistema de paradigma descentralizado. Isto traz inúmeras vantagens. Como você tem a cópia de todo o repositório, tem pouca dependência de recursos de rede  Ótimo para equipes de desenvolvimento geograficamente distribuídas. No Git sua workspace é um clone de todo o repositório, incluindo branches e tags, melhorando bastante a performance nas trocas de contexto e operações em branches. Na verdade, nem mesmo é necessário estar conectado na rede  Como cada elemento (fonte) do repositório armazena toda sua árvore histórica, você pode interagir com o repositório central posteriormente, mesmo que tenha gerado outros branches do que você já esteja trabalhando.

Não há necessidade de se conectar a um servidor remoto ou ainda, fechar seu projeto para fazer o checkout em outro diretório. Apenas git-checkout [nome-do-branch] resolve o problema.

Mesmo quando necessário executar um merge, não é preciso estar conectado a um servidor remoto, visto que você tem todos os branches no seu clone do repositório. Você pode criar, um novo branch para trabalhar os merges, tratando os conflitos de forma incremental sem afetar o branch principal. Desta forma, quando tudo estiver corrigido, você pode criar os patches necessários ou fazer o merge com o branch principal.

Se o desenvolvimento do branch principal andou algumas versões enquanto você estava desenvolvendo a sua revisão, você ainda pode usar artífícios como o rebase para sincronizar seu branch com o principal em uma árvore histórica mais linear. Vamos falar sobre isto mais a frente.

Uma outra vantagem em ser um sistema distribuído, é a possíbilidade conectar a repositórios de outros desenvolvedores e compartilhar códigos sem afetar o repositório central. 

Outra grande sacada do Git é o conceito de stash. Imagine que você esteja em meio à codificação de algum fonte que você não considere que valha a pena ainda fazer um commit e você é solicitado a interromper este primeiro trabalho para priorizar outra funcionalidade. Você pode utilizar o comando git stash para manter seu primeiro trabalho paralisado até que tenha demandado as pendências. O comando git stash cria um tag especial que não é commitada, além de não atender a comandos de push ou pull.


Características e Funcionalidades
---------------------------------

Nesta tabela, mostraremos comparativamente as características e funcionalidades dos dois sistemas:

+-----------------------------------+------------------------------+----------------------------------------+
|Atributo                           |CVS                           |GIT                                     |
+===================================+==============================+========================================+
|Linguagem de programação           |C                             |C, Shell Script e Perl                  |
+-----------------------------------+------------------------------+----------------------------------------+
|Método de armazenamento            |Changeset: São armazenadas    |                                        |
|                                   |apenas as diferenças dos      |                                        |
|                                   |arquivos commitados.          |                                        |
+-----------------------------------+------------------------------+----------------------------------------+
|Escopo de alterações               |Em nível de arquivos          |Toda a árvore/subarvore de diretórios   |
|                                   |                              |                                        |
+-----------------------------------+------------------------------+----------------------------------------+
|Identificadores de revisão         |Númérico                      |Hash SHA-1                              |
+-----------------------------------+------------------------------+----------------------------------------+
|Protocolo utilizado para           |Pserver e ssh                 |custom (git), custom sobre ssh, HTTP,   |
|sincronizar alterações             |                              |HTTPS, rsync, e-mail e bundles          |
+-----------------------------------+------------------------------+----------------------------------------+
|Garantia de commits atômicos – Ou  |Não                           |Sim                                     |
|todas as alterações são aplicadas, |                              |                                        |
|ou nenhuma                         |                              |                                        |
+-----------------------------------+------------------------------+----------------------------------------+
|Renomeação de arquivos com         |Não                           |Parcialmente (Apenas se o conteúdo do   |
|retenção do histórico de versão    |                              |arquivo não for extremamente alterado)  |
+-----------------------------------+------------------------------+----------------------------------------+
|Capacidade de merge em arquivos    |Não                           |Sim                                     |
|alterados em determinado branch    |                              |                                        |
|que tenha sido  renomeado em outro |                              |                                        |
+-----------------------------------+------------------------------+----------------------------------------+
|Capacidade de versionar e          |Não                           |Sim                                     |
|armazenar links simbólicos         |                              |                                        |
+-----------------------------------+------------------------------+----------------------------------------+
|Capacidade de disparar eventos     |Parcial                       |Sim                                     |
|antes ou depois de ações, como     |                              |                                        |
|commits, por exemplo               |                              |                                        |
+-----------------------------------+------------------------------+----------------------------------------+
|Integração de revisões com         |Não                           |Sim (a partir da versão 1.7.9)          |
|assinaturas digitais, como PGP,    |                              |                                        |
|por exemplo                        |                              |                                        |
+-----------------------------------+------------------------------+----------------------------------------+
|Rastreamento de merges, garantindo |Não                           |Sim                                     |
|que apenas alterações necessárias  |                              |                                        |
|sejam aplicadas em operações de    |                              |                                        |
|merge em branches distintos        |                              |                                        |
+-----------------------------------+------------------------------+----------------------------------------+
|Conversão de caracteres de         |Sim                           |Sim                                     |
|terminação de linha para adequação |                              |                                        |
|ao sistema operacional hospedeiro  |                              |                                        |
+-----------------------------------+------------------------------+----------------------------------------+
|Tags – Nomes significativos para   |Sim                           |Sim                                     |
|revisões específicas               |                              |                                        |
+-----------------------------------+------------------------------+----------------------------------------+
|Internacionalização – Suporte a    |Parcialmente (Apenas GUI)     |Parcialmente (Apenas GUI)               |
|múltiplos idiomas e sistemas       |                              |                                        |
|operacionais                       |                              |                                        |
+-----------------------------------+------------------------------+----------------------------------------+
|Suporte a nomes de arquivo UNICODE |Não                           |Sim (A partir da versão 1.7.10)         |
+-----------------------------------+------------------------------+----------------------------------------+
|Suporte a grandes repositórios     |Sim                           |Parcial (Ainda existem problemas com    |
|(com mais de 1 Gb, por exemplo)    |                              |repositórios muito grandes.             |
+-----------------------------------+------------------------------+----------------------------------------+
|Expansão de palavras-chave, como   |Sim (Utiliza modelo RCS, que  |Não (A  comunidade Git não reconhece    |
|números de revisão, por exemplo    |aciona palavras-chave no      |esta como uma boa funcionalidade)       |
|                                   |formato $chave:valor$ no      |                                        |
|                                   |arquivo editado.              |                                        |
+-----------------------------------+------------------------------+----------------------------------------+
|Commits interativos – Capacidade   |Não                           |Sim                                     |
|de commitar apenas parte das       |                              |                                        |
|alterações em um arquivos          |                              |                                        |
+-----------------------------------+------------------------------+----------------------------------------+
|Capacidade de incluir referências  |Sim                           |Sim (com git-submodule)                 |
|externas na árvore de fontes       |                              |                                        |
+-----------------------------------+------------------------------+----------------------------------------+
|Checkout parcial de apenas um      |Sim                           |Não                                     |
|objeto ou subdiretório do          |                              |                                        |
|repositório                        |                              |                                        |
+-----------------------------------+------------------------------+----------------------------------------+
|Preservação de timestamps,         |Sim                           |Não                                     |
|sobrescrevendo o tempo de commit   |                              |                                        |
|sobre o do filesystem do sistema   |                              |                                        |
|operacional hospedeiro             |                              |                                        |
+-----------------------------------+------------------------------+----------------------------------------+


Comandos Básicos e Avançados
----------------------------

Na tabela a seguir, mostramos comandos básicos e avançados disponíveis nos dois sistemas:

+---------------+---------------------------------------------------+---------------------+---------------------+
| Comando       | Descrição                                         | CVS                 | GIT                 |
+===============+===================================================+=====================+=====================+
|Init           |inicia repositório vazio                           |init                 |init [--bare]        |
+---------------+---------------------------------------------------+---------------------+---------------------+
|Clone          |cria uma instância identica de um repositório vazio|N/A                  |clone                |
+---------------+---------------------------------------------------+---------------------+---------------------+
|Pull           |Baixa revisões do repositório remoto para o local  |N/A                  |fetch                |
|               |                                                   |                     |(pull=fetch+merge)   |
+---------------+---------------------------------------------------+---------------------+---------------------+
|Push           |Faz o upload de revisões locais para               |N/A                  |push                 |
|               |o repositório remoto                               |                     |                     |
+---------------+---------------------------------------------------+---------------------+---------------------+
|Local branch   |Cria um branch que não existe no repositório remoto|N/A                  |branch               |
+---------------+---------------------------------------------------+---------------------+---------------------+
|Checkout       |Cria um cópia de trabalho local de um repositório  |checkout             |checkout             | 
|               |remoto                                             |                     |                     |
+---------------+---------------------------------------------------+---------------------+---------------------+
|Update         |Atualiza os arquivos de uma cópia de trabalho com  |update               |pull                 |
|               |as últimas versões de um repositório               |                     |                     |
+---------------+---------------------------------------------------+---------------------+---------------------+
|Add            |Marca determinados arquivos para serem adicionados |add                  |add                  |
|               |ao repositório no próximo commit                   |                     |                     |
+---------------+---------------------------------------------------+---------------------+---------------------+
|Remove         |Marca determinados arquivos para serem removidos   |rm                   |rm                   |
|               |no próximo commit                                  |                     |                     |
+---------------+---------------------------------------------------+---------------------+---------------------+
|Move           |Marca arquivos específicos para serem movidos      |N/A                  |mv                   |
|               |a um novo local no próximo commit                  |                     |                     |
+---------------+---------------------------------------------------+---------------------+---------------------+
|Revert         |Restaura uma cópia de arquivo de trabalho          |remove (depois)      |revert               |
|               |do repositório                                     |update               |                     |
+---------------+---------------------------------------------------+---------------------+---------------------+
|Generate bundle|cria um arquivo que contenha um conjunto           |N/A                  |bundle               |
|               |comprimido de mudanças para um dado repositório    |                     |                     |
+---------------+---------------------------------------------------+---------------------+---------------------+
|Rebase         |Adiciona commits locais a um repositório que já    |N/A                  |rebase               |
|               |evoluiu, mantendo histórico linear de alterações   |                     |                     |
+---------------+---------------------------------------------------+---------------------+---------------------+
|Copy           |Marca determinados arquivos para serem copiados no |N/A                  |cp(depois) add       |
|               |próximo commit                                     |                     |                     |
+---------------+---------------------------------------------------+---------------------+---------------------+
|Merge          |Aplica a diferença entre dois arquivos em uma      |update -j            |merge                |
|               |cópia de trabalho                                  |                     |                     |
+---------------+---------------------------------------------------+---------------------+---------------------+
|Commit         |Grava as mudanças no repositório                   |commit               |commit               |
+---------------+---------------------------------------------------+---------------------+---------------------+
|Aliases        |cria aliaes para comandos específicos ou           |No arquivos          |No arquivo           |
|               |combinações de comandos                            |'.cvsrc'             |'.gitconfig'         |
+---------------+---------------------------------------------------+---------------------+---------------------+
|Lock/Unlock    |Cria bloqueios exclusivos em arquivos, prevenindo  |edit -x/unedit       |N/A                  |
|               |que sejam alterados por outrem                     |                     |                     |
+---------------+---------------------------------------------------+---------------------+---------------------+
|Shelve /       |Põe de lado temporariamente, total/parcialmente,   |N/A                  |stash/stash pop      |
| Unshelve      |as mudanças em um diretório de trabalho            |                     |                     |
+---------------+---------------------------------------------------+---------------------+---------------------+
|Rollback       |Remove um patch  ou revisão do histórico           |admin -o             |reset HEAD^          |
+---------------+---------------------------------------------------+---------------------+---------------------+
|Chery-pick     |Move apenas algumas revisões de um branch para     |Apenas com CVSNT     |chery-pick           |
|               |outro, ao invés de executar um merge total         |                     |                     |
+---------------+---------------------------------------------------+---------------------+---------------------+
|Bisect         |Pesquisa binária sobre o histórico de fontes por   |Apenas com CVSNT     |bisect               |
|               |mudança que tenha introduzido ouconsertado uma     |                     |                     |
|               |regressão                                          |                     |                     |
+---------------+---------------------------------------------------+---------------------+---------------------+
|Incoming       |Consulta as diferenças entre o repositório local   |N/A                  |incoming/outgoing    |
|Outgoing       |e remoto                                           |                     |                     |
+---------------+---------------------------------------------------+---------------------+---------------------+
|Grep           |Procura por linhas que batam com o padrão passado  |N/A                  |grep                 |
|               |no repositório                                     |                     |                     |
+---------------+---------------------------------------------------+---------------------+---------------------+
|Record         |Inclui apenas algumas das mudanças em um arquivo no|N/A                  |add -p               |
|               |commit                                             |                     |                     |
+---------------+---------------------------------------------------+---------------------+---------------------+

Conclusão
=========

Ambos os sistemas têm suas vantagens e desvantagens. O Git se apresenta como uma ótima opção para gerenciamento de fontes e versionamento. Por sua característica como sistema distribuído e baseado em snapshots, oferece muito mais funcionalidades no que tange performance, rastreamento e colaboração. Além disso, encontra-se em pleno desenvolvimento e evolução. O CVS por outro lado, apesar de estar no mercado há bastante tempo e ter sedimentado sua comunidade de desenvolvimento , sua evolução já cessou. Atualmente só há esforços para manutenção e não novas funcionalidades. 


Referências
===========


---
remark: metadados com alguns dados para listar referências bibliográficas. Use quantos identificadores (ID) necessitar para listar as diferentes referências usadas no artigo
references:
- id: ID-GitDoc
  title: "Git Documentation"
  container-title: Source Control
  URL: 'http://git-scm.com/documentation'
  accessed:
    day: 01
    month: 2
    year: 2014
  publisher: Git Community
  type: webpage

- id: GitBottomUp2009
  title: "Git from the bottom up"
  author:
  - family: Wiegley
    given: John
  container-title: Source Control
  URL: 'http://ftp.newartisans.com/pub/git.from.bottom.up.pdf'
  type: article
  issued:
    year: 2009
    month: 12
    day: 2
  
...
