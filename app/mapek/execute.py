from app.mapek.observer import Observer



class Execute(Observer):
    __instance = None

    @staticmethod 
    def getInstance():
        if Execute.__instance == None:
            Execute()
        return Execute.__instance
        
    def __init__(self):
        if Execute.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Execute.__instance = self


    def notify(self):
        print("\n--------\nExecuting ...")
        print('---------------')