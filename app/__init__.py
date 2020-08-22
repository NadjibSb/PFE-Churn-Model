from flask import Flask
import time
# Suppressing Warnings
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)
#from app import views


from app.mapek.monitor import Monitor
from app.mapek.knowledge import Knowledge


k = Knowledge.getInstance()
k.save("test",3333333)
print(k.get("test"))

'''
monitor = Monitor()
while 1:
    monitor.notify("monitor")
    time.sleep(2)
'''

