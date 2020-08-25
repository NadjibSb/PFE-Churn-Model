from app.observer import Observer
from app.mapek.execute import Execute
from app.mapek.knowledge import Knowledge



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

                execute = Execute.getInstance()
                execute.notify()

        