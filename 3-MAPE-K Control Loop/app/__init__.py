from flask import Flask
import time
# Suppressing Warnings
import warnings
warnings.filterwarnings('ignore')
from flask_cors import CORS


app = Flask(__name__)

CORS(app)
from app import views