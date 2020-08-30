from threading import Thread
import time

from app import app as flaskApp
import app.mapek as mapek


def runAPI():
    flaskApp.run(port=5002)

def runMAPEK():
    mapek.run()


if __name__ == '__main__':
    Thread(target = runAPI).start()
    Thread(target = runMAPEK).start()