from flask import jsonify, request, Response
import simplejson as json

from app import app


@app.route('/')
def server_is_up():
   return "<h1>Server is up</h1>"
