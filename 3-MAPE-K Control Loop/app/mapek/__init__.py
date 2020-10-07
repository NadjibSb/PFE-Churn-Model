
import time

from app.mapek.monitor import Monitor
from app.mapek.knowledge import Knowledge


def run():
    monitor = Monitor()
    knowledge = Knowledge.getInstance()

    while True:
        params = knowledge.get("params")
        monitor.notify()
        time.sleep(params["frequency"])

