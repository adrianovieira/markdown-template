WebHook
=======

Webhook simples para realizar conversão automatizada de documentos/artigos para PDF

A fazer
-------

```um monte de código ainda precisa ser escrito```

Estrutura do diretório
----------------------

```markdown
README.md:                   Este documento
INSTALL.md                   Instruções para instalação desse hook web
webhook.py                   A aplicação para hook web do repositório
                             *documentos/artigos* no gitlab
webhook-dist.cfg:            Arquivo de configuração padrão (obrigatório)
requirements.txt:            Requisitos padrão para a aplicação
requirements-ipdb.txt:       Requisitos para debug interativo
teste/                       Alguns scripts NodeJS para teste de POST neste hook

```