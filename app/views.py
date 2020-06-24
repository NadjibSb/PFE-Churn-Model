from app import app
from app import model
from flask import jsonify, request

import pandas as pd

@app.route('/')
def server_is_up():
   return "<h1>Server is up 2</h1>"


@app.route('/predict', methods=['GET'])
def predict():
	#data = request.get_json()

	data = [[7001865778,34.047,355.074,268.321,24.11,78.68,7.68,15.74,99.84,304.76,0.0,0.0,0.0,0.0,0.0,0.0,40.31,178.53,312.44,26.83,104.23,423.28,4,9,11,74,384,283,0.0,1.0,2.0,0.0,154.0,50.0,33.53333333333333,24,15,1,27,8,12,0,1.0,0.0,3.0,60.0,6.0,21.0,1.0,182.735,0.0],
	[7001625959,167.69,189.058,210.226,11.54,55.24,37.26,143.33,220.59,208.36,0.0,0.0,0.0,0.0,0.0,0.0,155.33,412.94,285.46,370.04,519.53,395.03,5,4,2,168,315,116,0.0,0.0,0.0,0.0,0.0,0.0,36.766666666666666,24,2,11,26,20,11,0,13.0,7.0,17.0,60.0,60.0,60.0,0.0,0.0,0.0]]
	#data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
	#df = pd.DataFrame.from_dict(data["data"])
	#return "data: \n{0}".format(type(data["data"]))
	#return "type: {0} \n data: {1}".format(type(data),data)
	return model.predict(data)

   #return "args: {0}".format(request.args.get('key'))
	#return "args: {0}".format(request.get_json())

