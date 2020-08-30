from flask import jsonify, request, Response
import simplejson as json
from app import app

def getKnowledge():
   with open('./app/mapek/knowledge/knowledge.json', 'r') as fp:
      data = json.load(fp)
      return data

def getObjectifs():
   with open('./app/mapek/knowledge/objectifs.json', 'r') as fp:
      data = json.load(fp)
      return data

@app.route('/')
def server_is_up():
   return "<h1>Server is up</h1>"


@app.route('/params', methods=['GET'])
def getParams():
   return getObjectifs()["params"]

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
   
