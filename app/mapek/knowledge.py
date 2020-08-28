import time
import json

class Knowledge:
    __instance = None
    __dict = {}
    
    @staticmethod 
    def getInstance():
        if Knowledge.__instance == None:
            Knowledge()
            print("Loaded JSON:")
            print(Knowledge.__dict)
        return Knowledge.__instance
        
    def __init__(self):
        if Knowledge.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Knowledge.__instance = self
            try:
                Knowledge.__dict = self.loadJson()
            except:
                Knowledge.__dict = {}


    def saveJson(self):
        with open('knowledge.json', 'w') as fp:
            json.dump(Knowledge.__dict, fp,indent=4)


    def loadJson(self):
        with open('knowledge.json', 'r') as fp:
            data = json.load(fp)
            return data

    
    def save(self,superKey,key,value):
        if superKey not in Knowledge.__dict:
            Knowledge.__dict[superKey]= {}
        if key not in Knowledge.__dict[superKey]:
            Knowledge.__dict[superKey][key]= {}
        dic = Knowledge.__dict[superKey][key]
        for k in value:
            dic[k] = value[k]
        if "history" not in dic:
            dic["history"] = []
        if (len(dic["history"])!=0) and (dic["history"][-1]["value"]==value):
            dic["history"][-1]["date"]= time.time()
        else:
            dic["history"].append({"date": time.time(), "value": value}) 
        self.saveJson()
    
    def get(self,key):
        return Knowledge.__dict[key]
