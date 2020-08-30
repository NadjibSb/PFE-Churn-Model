from flask import jsonify, request, Response
import simplejson as json
from app import app



@app.route('/')
def server_is_up():
   return "<h1>Server is up</h1>"

"""
from app.mapek.monitor import Monitor
@app.route('/monitor')
def monitor():
   monitor = Monitor()
   monitor.notify("monitor")
   return 'Monitoring ...'
   """
