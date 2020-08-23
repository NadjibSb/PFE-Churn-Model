from app.observer import Observer
from app.mapek.plan import Plan



class Analyse(Observer):
    def notify(self):
        print("\n--------\nAnalysing ...")
        plan = Plan()
        plan.notify()