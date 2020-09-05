
import time

from app.mapek.monitor import Monitor
from app.mapek.knowledge import Knowledge


def run():
    monitor = Monitor()
    knowledge = Knowledge.getInstance()
    params = knowledge.get("params")

    while True:
        monitor.notify()
        time.sleep(params["frequency"])

