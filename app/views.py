from app import app
from flask import jsonify, request


@app.route('/')
def hello():
	var = "Hello World! Ooredoo Stage"
	print(var)
	return var



@app.route('/test', methods=['GET'])
def server_is_up():
   return "<h1>Server is up 2</h1>"


@app.route('/predict', methods=['POST'])
def predict():

   #return "args: {0}".format(request.args.get('key'))
   return "args: {0}".format(request.get_json())

