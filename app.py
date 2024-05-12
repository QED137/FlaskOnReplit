from flask import Flask, render_template, request, redirect, jsonify
import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func
from database import load_data_from_db
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)


    
@app.route("/")

def hello_world():
  JOBS=load_data_from_db()
  return render_template('index.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)
