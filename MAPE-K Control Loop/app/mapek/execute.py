
import time
import os
import codecs
import requests
from app.mapek.observer import Observer
from app.mapek.knowledge import Knowledge

BASE_PATH = os.path.dirname(__file__)
CHURN_SERVER = "http://localhost:5001"

class Execute(Observer):
    __instance = None

    @staticmethod 
    def getInstance():
        if Execute.__instance == None:
            Execute()
        return Execute.__instance
        
    def __init__(self):
        if Execute.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Execute.__instance = self


    def notify(self,modelInfo):
        print("\n--------\nExecuting ...")
        file_data = codecs.open('{0}/models/model{1}.pickle'.format(BASE_PATH,modelInfo["id"]), 'rb').read()
        req = requests.post(CHURN_SERVER+'/adapt',data=file_data,headers={'model_id':str(modelInfo["id"])})
        print(req)
        req = requests.get(CHURN_SERVER+'/predictAll').json()
        print(req)


        knowledge = Knowledge.getInstance()
        data = requests.get(CHURN_SERVER+"/evaluate").json()
        for key in data:
            content = data[key]
            knowledge.save("Monitor",key,content)
            content["status"] = 1
            knowledge.save("Status",key,content,False)
        
        self.updateStatus(modelInfo["name"])
        print('---------------')

    

    def updateStatus(self,key):
        knowledge = Knowledge.getInstance()
        status = knowledge.get("Status")[key]
        end = time.time()
        duration = end - status["start_adapt_time"]
        knowledge.save("Status",key,{"status":1, "last_adapt_time": end, "last_adapt_duration": duration},False)