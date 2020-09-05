from flask import jsonify, request, Response
import simplejson as json
from app import app

'''
from flask_socketio import SocketIO, emit
socketio = SocketIO(app, async_mode='eventlet')
socketio.emit('newnumber', {'number': 11111111111111111111})
socketio.run(app, debug=True)
'''
@app.route('/')
def server_is_up():
   return "<h1>Server is up</h1>"


@app.route('/params', methods=['GET','POST'])
def getParams():
   if request.method == 'GET':
      return getObjectifs()["params"]
   elif request.method == 'POST':
      content = request.json
      saved = getObjectifs()["params"]
      if 'accurency' in content:
         if (content['accurency']<=1) and (content['accurency']>0):
            saved['accurency'] = float(content['accurency'])
      if 'frequency' in content:
         saved['frequency'] = int(content['frequency'])
      setObjectifs({"params":saved})
      return saved



@app.route('/info', methods=['GET'])
def getInfos():
   data = getKnowledge()["Monitor"]
   info = {}
   for k in data:
      info[k]=[]
      hist = data[k]["history"]
      for value in hist:
         info[k].append({"date": value["date"] , "accurency": value["value"]["accurency"]})
   return info



@app.route('/monitor', methods=['GET'])
def monitor():
   data = getKnowledge()["Status"]
   for k in data :
      info = data[k]
      if "start_adapt_time" in info:
         info.pop('start_adapt_time', None)
   return data
   




def getKnowledge():
   with open('./app/mapek/knowledge/knowledge.json', 'r') as fp:
      data = json.load(fp)
      return data

def getObjectifs():
   with open('./app/mapek/knowledge/objectifs.json', 'r') as fp:
      data = json.load(fp)
      return data


def setObjectifs(data):
   with open('./app/mapek/knowledge/objectifs.json', 'w') as fp:
      json.dump(data, fp,indent=4)








