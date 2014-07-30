from flask import Flask, request
app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def init():

  print request.data

  return "[ OK ]"

if __name__ == "__main__":
  app.debug = True
  app.run(host='0.0.0.0')
