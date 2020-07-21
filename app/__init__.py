from flask import Flask
# Suppressing Warnings
import warnings
warnings.filterwarnings('ignore')


app = Flask(__name__)

from app import views
