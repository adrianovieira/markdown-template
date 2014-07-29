from flask import Flask, request, json
import requests


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

'''
a ser extraido para arquivo de configuracoes
avaliar "modulo: logging"
'''
debug = True
debug_level = DEBUG_LEVEL0
#debug_level = DEBUG_INTERATIVO

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
   app_msg_status = ''
   if request.method == 'GET':
        return 'Aplicacao para webhook! \n Use adequadamente!'

   elif request.method == 'POST':
        if debug and debug_level == DEBUG_INTERATIVO:
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

if __name__ == '__main__':
   if debug:
      app.debug = True
      app.run(host='0.0.0.0')
   else:
      app.run()
