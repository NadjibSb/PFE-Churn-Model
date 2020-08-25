from app.observer import Observer
from app.mapek.plan import Plan
from app.mapek.knowledge import Knowledge



class Analyse(Observer):
    __instance = None

    @staticmethod 
    def getInstance():
        if Analyse.__instance == None:
            Analyse()
        return Analyse.__instance
        
    def __init__(self):
        if Analyse.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Analyse.__instance = self


    def notify(self):
        print("\n--------\nAnalysing ...")
        toPlan=False

        knowledge = Knowledge.getInstance()
        data = knowledge.get("Monitor")
        for key in data:
            modelInfo = data[key]
            if ("accurency" in modelInfo) & (modelInfo["accurency"]>0.95):
                print(key+" adapt")
                knowledge.save("Analyse",key,{"to_adapt": True})
                toPlan=True
            else:
                print(key+" pass")
                knowledge.save("Analyse",key,{"to_adapt": False})

        if toPlan:
            plan = Plan.getInstance()
            plan.notify()