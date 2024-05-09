from flask import Flask, render_template, request, redirect
import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

JOBS =[
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Tübingen, Germany',
    'Sallary' : '€15.000'
    
  },
  {
    'id': 2,
    'title': 'Data Engineer',
    'location': 'Münich, Germany',
    'Sallary' : '€34.000'

  },
  {
    'id': 3,
    'title': 'Machine Learning Expert',
    'location': 'Berlin, Germany',
    'Sallary' : '€115.000'

  }
]
    
@app.route("/")

def hello_world():
  
  return render_template('index.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)
