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
import gitlab

app = Flask(__name__)

'''
commentMR: post comment to Merge Request

@params:
  id: The ID of a project (required)
  merge_request_id: ID of merge request (required)
  note: Text of comment (required)
'''
def commentMR(target_project_id, merge_request_id, note):
  #POST /projects/:id/merge_request/:merge_request_id/comments
  commented = False

  print "target_project_id: {}".format(target_project_id)+\
        ", merge_request_id: {}".format(merge_request_id)+\
        ", note: "+note

  return commented

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
Gitlab status and merge_status
'''
GL_STATE = {
   'CLOSED':'closed',
   'OPENED':'opened'
   }

GL_STATUS = {
   'merge_request':'merge_request',
   'cannot_be_merged':'cannot_be_merged',
   'can_be_merged':'can_be_merged'
   }

@app.route('/',methods=['GET', 'POST'])
def index():
   app_msg_status = ''
   if request.method == 'GET':
        return 'Aplicacao para webhook! \n Use adequadamente!'

   elif request.method == 'POST':

    ok_git=app.gitlab = gitlab.Gitlab(app.setup['gitlab_url'])

    ok_git=app.gitlab.login(app.setup['webhook_user'], app.setup['webhook_pass'])

    if app.setup['DEBUG'] == 'True' and int(app.setup['DEBUG_LEVEL']) == DEBUG_INTERATIVO:
       import ipdb; ipdb.set_trace() # ativado para debug interativo

    webhook_data = json.loads(request.data)

    print webhook_data

    try:
      app_msg_status = "not a merge request"
      if webhook_data['object_kind'] or webhook_data['object_attributes']:
        if webhook_data['object_kind'] != GL_STATUS['merge_request']:
          raise

        if webhook_data['object_attributes']:
          if webhook_data['object_attributes']['state'] == GL_STATE['OPENED']:
            if webhook_data['object_attributes']['merge_status'] == GL_STATUS['cannot_be_merged']:
              app_msg_status = "cannot be merged"

              app.gitlab.addcommenttomergerequest(webhook_data['object_attributes']['target_project_id'], \
                        webhook_data['object_attributes']['id'], \
                        'merge não aceito. Verique "branch" e solicite novamente!')
              raise # caso nao possa ser feito merge via gitlab "merge request invalido"
          else:
            app_msg_status = "MR "+webhook_data['object_attributes']['state']+\
                             " - "+webhook_data['object_attributes']['merge_status']
            raise

    except: # IndexError: ou caso nao seja "merge_request"
        print 'Aplicacao webhook para "Merge Request"! \n Use adequadamente!'
        status = '{"status": "ERROR", "message": "'+app_msg_status+'"}'
        return status

    if webhook_data['object_attributes']['state'] == GL_STATE['OPENED'] and \
       webhook_data['object_attributes']['merge_status'] == GL_STATUS['can_be_merged']:
      print "\nProcessing merge request ...\n"

      # simples adição de comentário ao merge request
      app.gitlab.addcommenttomergerequest(webhook_data['object_attributes']['target_project_id'], \
                webhook_data['object_attributes']['id'], \
                'Processing merge request ...['+webhook_data['object_attributes']['merge_status']+']')

      #print webhook_data # ['object_attributes']['source_branch']

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
