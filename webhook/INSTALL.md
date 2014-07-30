WebHook
=======

Webhook simples para realizar conversão automatizada de documentos/artigos para PDF.

Estrutura do diretório
----------------------

```
README.md:                   Este documento
INSTALL.md                   Instruções para instalação desse hook web
webhook.py                   A aplicação para hook web do repositório
                             *documentos/artigos* no gitlab
webhook-dist.cfg:            Arquivo de configuração padrão (obrigatório)
requirements.txt:            Requisitos padrão para a aplicação
requirements-ipdb.txt:       Requisitos para debug interativo
teste/                       Alguns scripts NodeJS para teste de POST neste hook

```

Instalação
----------

1. Considere avaliar a necessidade de criação de ambiente virtual, principalmente se instalando para contribuir com o desenvolvimento deste *web hook*.  
   ```virtualenv --help```
1. Instale os requisitos necessários para a aplicação  
   ```pip install -r requirements.txt```  
1. Crie o arquivo ```webhook.cfg``` com os dados específicos do ambiente em que está para ser instalado.  
   Tenha como referência os parâmetros contidos no arquivo ```webhook-dist.cfg```.  
