import time
import json

class Knowledge:
    __instance = None
    __dict = {}
    __objectifs = {}
    
    @staticmethod 
    def getInstance():
        if Knowledge.__instance == None:
            Knowledge()
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
            try:
                Knowledge.__objectifs = self.loadObjectifs()
            except:
                raise Exception("Can't load ./app/mapek/knowledge/objectifs.json")


    def saveJson(self):
        with open('./app/mapek/knowledge/knowledge.json', 'w') as fp:
            json.dump(Knowledge.__dict, fp,indent=4)


    def loadJson(self):
        with open('./app/mapek/knowledge/knowledge.json', 'r') as fp:
            data = json.load(fp)
            return data

    def loadObjectifs(self):
        with open('./app/mapek/knowledge/objectifs.json', 'r') as fp:
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
        if key in Knowledge.__dict:
            return Knowledge.__dict[key]
        elif key in Knowledge.__objectifs:
            return Knowledge.__objectifs[key]
        else:
            return None
