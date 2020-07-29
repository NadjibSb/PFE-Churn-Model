import requests
from flask import jsonify
import json 

from app import model

DB_SERVER = "http://localhost:3000/customer"

def predictAll():
    count = requests.get(DB_SERVER+"/count").json()

    if "pages" in count: 
        for p in range(1,count["pages"]+1):
            print(p)
            data_array = requests.get(DB_SERVER+"/all/{0}".format(p)).json()
            pred = model.predict(data_array)
            updated = requests.post(DB_SERVER+"/update", json = json.loads(pred), headers={"Content-Type":"application/json"})
        return json.dumps({"updated": True, "pages_updated": count["pages"]})
    
    else:
        e = json.dumps({"error": "unexpected value", "data": count})
        return e



def evaluate():
    count = requests.get(DB_SERVER+"/count").json()
    data_array=[]

    if "pages" in count: 
        for p in range(1,3):
            print(p)
            data_array += requests.get(DB_SERVER+"/all/{0}?churn=1&pred_churn=1".format(p)).json()
            print(len(data_array))
    else:
        e = json.dumps({"error": "unexpected value", "data": count})
        return e


    evaluation = model.evaluate(data_array)
    return json.dumps(evaluation)