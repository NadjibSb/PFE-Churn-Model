from flask import Flask
import time
from app.mapek.monitor import Monitor
# Suppressing Warnings
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)
from app import views


'''
monitor = Monitor()
while 1:
    monitor.notify("monitor")
    time.sleep(2)
'''

