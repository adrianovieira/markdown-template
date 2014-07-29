# coding: utf-8
'''
App: Webhook
description: permitir hook de conversão pandoc em "documentos/artigos"
author: Adriano dos Santos Vieira
character encoding: UTF-8
'''
from flask import Flask, request, json
import requests
import ConfigParser

app = Flask(__name__)

'''
getConfig: obtem dados de configuracao do ambiente
'''
def getConfig():
  Config = ConfigParser.ConfigParser()
  '''
  obtem dados de configuracao padrao
  '''
  try:
    Config.read('webhook-dist.cfg')
  except:
    return False

  app.setup['gitlab_url'] = Config.get('enviroment', 'gitlab_url')
  app.setup['webhook_user'] = Config.get('enviroment', 'webhook_user')
  app.setup['webhook_pass'] = Config.get('enviroment', 'webhook_pass')
  app.setup['production'] = Config.get('enviroment', 'production')
  app.setup['template_path'] = Config.get('enviroment', 'template_path')
  app.setup['pandoc'] = Config.get('enviroment', 'pandoc')
  app.setup['pdflatex'] = Config.get('enviroment', 'pdflatex')
  app.setup['make'] = Config.get('enviroment', 'make')
  app.setup['DEBUG_LEVEL'] = Config.get('enviroment', 'DEBUG_LEVEL')
  app.setup['DEBUG'] = Config.get('enviroment', 'DEBUG')

  '''
  obtem dados de configuracao personalizados
  '''
  try:
    Config.read('webhook.cfg')
    if Config.get('enviroment', 'gitlab_url'):
      app.setup['gitlab_url'] = Config.get('enviroment', 'gitlab_url')
    if Config.get('enviroment', 'webhook_user'):
      app.setup['webhook_user'] = Config.get('enviroment', 'webhook_user')
    if Config.get('enviroment', 'webhook_pass'):
      app.setup['webhook_pass'] = Config.get('enviroment', 'webhook_pass')
    if Config.get('enviroment', 'production'):
      app.setup['production'] = Config.get('enviroment', 'production')
    if Config.get('enviroment', 'template_path'):
      app.setup['template_path'] = Config.get('enviroment', 'template_path')
    if Config.get('enviroment', 'pandoc'):
      app.setup['pandoc'] = Config.get('enviroment', 'pandoc')
    if Config.get('enviroment', 'pdflatex'):
      app.setup['pdflatex'] = Config.get('enviroment', 'pdflatex')
    if Config.get('enviroment', 'make'):
      app.setup['make'] = Config.get('enviroment', 'make')
    if Config.get('enviroment', 'DEBUG_LEVEL'):
      app.setup['DEBUG_LEVEL'] = Config.get('enviroment', 'DEBUG_LEVEL')
    if Config.get('enviroment', 'DEBUG'):
      app.setup['DEBUG'] = Config.get('enviroment', 'DEBUG')
  except:
    print "WARNING: can't read custom-config file."
    pass

  return True

'''
CONTANTES
avaliar "modulo: logging"
'''
DEBUG_LEVEL0 = 0
DEBUG_LEVEL1 = 1 # mostra algumas mensagens na console
DEBUG_INTERATIVO = 9 # ipdb ativado: "ipdb.set_trace()"

'''
Gitlab status
'''
GL_STATUS = {
   'merge_request':'merge_request',
   'cannot_be_merged':'cannot_be_merged'
   }

@app.route('/',methods=['GET', 'POST'])
def index():
   app_msg_status = ''
   if request.method == 'GET':
        return 'Aplicacao para webhook! \n Use adequadamente!'

   elif request.method == 'POST':
    print app.setup
    if app.setup['DEBUG'] == 'True' and int(app.setup['DEBUG_LEVEL']) == DEBUG_INTERATIVO:
       import ipdb; ipdb.set_trace() # ativado para debug interativo

    hookdata = json.loads(request.data)
    hookdata_ok = False
    try:
      app_msg_status = "not a merge request"
      if hookdata['object_kind'] or hookdata['object_attributes']:
        if hookdata['object_kind'] != GL_STATUS['merge_request']:
          raise
        if hookdata['object_attributes']:
          if hookdata['object_attributes']['merge_status'] == GL_STATUS['cannot_be_merged']:
            app_msg_status = "cannot be merged"
            raise # caso nao possa ser feito merge via gitlab "merge request invalido"
    except: # IndexError: ou caso nao seja "merge_request"
        print 'Aplicacao webhook para "Merge Request"! \n Use adequadamente!'
        status = '{"status": "ERROR", "message": "'+app_msg_status+'"}'
        return status

    print "\nProcessing merge request ...\n"

    print hookdata # ['object_attributes']['source_branch']

    return '{"status": "OK"}'

'''
Inicia aplicação
'''
app.setup = {} # global de configuracao

if __name__ == '__main__':
  if getConfig(): # obtem dados de configuracao inicial
     if app.setup['DEBUG'] == 'True':
        app.debug = True
        app.run(host='0.0.0.0')
     else:
        app.run()
  else:
    print "ERROR: trying to read dist-config file."
