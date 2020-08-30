
import time

from app.mapek.monitor import Monitor


def run():
    #time.sleep(10)
    monitor = Monitor()
    monitor.notify()