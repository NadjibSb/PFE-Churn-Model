from app.observer import Observer
from app.plan import Plan



class Analyse(Observer):
    def notify(self,message):
        print(message)
        plan = Plan()
        plan.notify("planning...")