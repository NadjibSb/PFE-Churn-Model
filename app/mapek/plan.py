from app.observer import Observer
from app.mapek.execute import Execute



class Plan(Observer):
    def notify(self):
        print("\n--------\nPlanning ...")
        execute = Execute()
        execute.notify()