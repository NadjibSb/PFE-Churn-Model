from app.observer import Observer



class Execute(Observer):
    def notify(self):
        print("\n--------\nExecuting ...")
        print('---------------')