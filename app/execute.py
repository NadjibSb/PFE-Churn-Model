from app.observer import Observer



class Execute(Observer):
    def notify(self,message):
        print(message)
        print('---------------')