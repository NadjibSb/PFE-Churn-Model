from app.observer import Observer
from app.execute import Execute



class Plan(Observer):
    def notify(self,message):
        print(message)
        execute = Execute()
        execute.notify("executing...")