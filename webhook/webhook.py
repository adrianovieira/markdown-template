from flask import Flask, request, json
import requests

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
   if request.method == 'GET':
        return 'Aplicacao para webhook! \n Use adequadamente!'

   elif request.method == 'POST':
         #hookdata = request.data
        print request.data
        #print "Dados webhook: {}".format(hookdata)
        #print "Dados: ".format(hookdata)
        print "Ola, adriano"
        return "OK"

if __name__ == '__main__':
   app.debug = True
   app.run()
