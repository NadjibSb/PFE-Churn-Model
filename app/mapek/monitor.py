import time
import requests
import json
from app.observer import Observer
from app.mapek.analyse import Analyse
from app.mapek.knowledge import Knowledge


DB_SERVER = "http://localhost:5001"


class Monitor(Observer):
    __instance = None

    @staticmethod 
    def getInstance():
        if Monitor.__instance == None:
            Monitor()
        return Monitor.__instance
        
    def __init__(self):
        if Monitor.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Monitor.__instance = self


    def notify(self):
        print("\n--------\nmonitoring ...")

        knowledge = Knowledge.getInstance()
        data = {
                "Model_2": {
                    "id": 2,
                    "accurency": 0.9804
                },
                "Model_0": {
                    "id": 0,
                    "accurency": 0.9416
                },
                "Model_1": {
                    "id": 1,
                    "accurency": 0.9823
                }
            }
        #data = requests.get(DB_SERVER+"/evaluate").json()
        for key in data:
            knowledge.save("Monitor",key,data[key])

        analyse = Analyse.getInstance()
        analyse.notify()

