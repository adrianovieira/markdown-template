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
a ser extraido para arquivo de configuracoes
avaliar "modulo: logging"
'''
debug = True
debug_level = DEBUG_LEVEL0

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
   if request.method == 'GET':
        return 'Aplicacao para webhook! \n Use adequadamente!'

   elif request.method == 'POST':
        if debug and debug_level == DEBUG_INTERATIVO:
           import ipdb; ipdb.set_trace() # ativado para debug interativo

        hookdata = json.loads(request.data)
        hookdata_ok = False
        try:
            if hookdata['object_kind']:
               if hookdata['object_kind'] != 'merge_request':
                  raise
        except: # IndexError: ou caso nao seja "merge_request"
            print 'Aplicacao webhook para "Merge Request"! \n Use adequadamente!'
            return '{"status": "ERROR", "message": "not a merge request"}'

        print "\nProcessing merge request ...\n"

        print hookdata # ['object_attributes']['source_branch']

        return '{"status": "OK"}'

if __name__ == '__main__':
   if debug:
      app.debug = True
      app.run(host='0.0.0.0')
   else:
      app.run()
