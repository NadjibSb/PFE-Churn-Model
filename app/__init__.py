from flask import Flask
import time
# Suppressing Warnings
import warnings
warnings.filterwarnings('ignore')



app = Flask(__name__)
from app import views