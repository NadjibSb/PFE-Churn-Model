import time
import requests
import json
from app.observer import Observer
from app.analyse import Analyse


DB_SERVER = "http://localhost:3000/customer"


class Monitor(Observer):
    def notify(self,message):
        print(message)
        analyse = Analyse()
        analyse.notify("analysing...")

