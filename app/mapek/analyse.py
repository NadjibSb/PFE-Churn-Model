from app.observer import Observer
from app.mapek.plan import Plan
from app.mapek.knowledge import Knowledge



class Analyse(Observer):
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
            plan = Plan()
            plan.notify()