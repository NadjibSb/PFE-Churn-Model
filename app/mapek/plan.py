from app.observer import Observer
from app.mapek.execute import Execute



class Plan(Observer):
    def notify(self,message):
        print(message)
        execute = Execute()
        execute.notify("executing...")