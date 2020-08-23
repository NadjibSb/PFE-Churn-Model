from flask import Flask
import time
# Suppressing Warnings
import warnings
warnings.filterwarnings('ignore')

from app.mapek.monitor import Monitor



monitor = Monitor()
monitor.notify()
#time.sleep(2)


app = Flask(__name__)
#from app import views