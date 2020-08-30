from threading import Thread
import time

from app import app
from app.mapek.monitor import Monitor


def runAPI():
    app.run(port=5002)

def runMAPEK():
    time.sleep(10)
    monitor = Monitor()
    monitor.notify()


if __name__ == '__main__':
    Thread(target = runAPI).start()
    Thread(target = runMAPEK).start()