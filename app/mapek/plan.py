## imports
import pandas as pd
import numpy as np
import os

from app.observer import Observer
from app.mapek.execute import Execute
from app.mapek.knowledge import Knowledge

BASE_PATH = os.path.dirname(__file__)

class Plan(Observer):
    __instance = None

    @staticmethod 
    def getInstance():
        if Plan.__instance == None:
            Plan()
        return Plan.__instance
        
    def __init__(self):
        if Plan.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Plan.__instance = self



    def notify(self):
        print("\n--------\nPlanning ...")

        knowledge = Knowledge.getInstance()
        data = knowledge.get("Analyse")
        for key in data:
            modelInfo = data[key]
            if modelInfo["to_adapt"]:
                print(key+" adapting ...")
                df = pd.read_csv("{0}/../dataset/clustered_{1}.csv".format(BASE_PATH,modelInfo["id"]),index_col="index")
                print("load dataset {0} : ".format(modelInfo["id"])+str(df.shape))  


                execute = Execute.getInstance()
                execute.notify()

        