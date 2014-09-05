WebHook
=======

*Web Hook* para realizar conversão automatizada de documentos/artigos para PDF

A fazer
-------

- ~~Criar roteiro de instalação desse Web Hook~~
- ~~Definir e implementar método para disponibilizar o PDF gerado~~
- ~~Definir regra para exclusão de arquivos temporários gerados pelo Web Hook~~

Estrutura do diretório
----------------------

```texinfo
README.md:                   Este documento
INSTALL.md                   Instruções para instalação desse Web Hook
webhook.py                   A aplicação para Web Hook do repositório
                             *documentos/artigos* no gitlab
webhook-dist.cfg:            Arquivo de configuração padrão (obrigatório)
requirements.txt:            Requisitos padrão para a aplicação
requirements-ipdb.txt:       Requisitos para debug interativo
teste/                       Alguns scripts NodeJS para teste de POST neste hook

```
