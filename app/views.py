from app import app
from flask import jsonify, request


@app.route('/')
def server_is_up():
   return "<h1>Server is up</h1>"