from flask import Flask, render_template, request, redirect, jsonify
import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
import logging
from sqlalchemy.sql import func
from database import load_data_from_db, load_job_fromDB,    push_application_data_to_db
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)


    
@app.route("/")

def hello_world():
  JOBS=load_data_from_db()
  return render_template('index.html', jobs=JOBS)
  

# '''This function retrieves a list of jobs from the database and returns them as JSON data. The data is read-only and cannot be modified. This function serves as an API endpoint for accessing job listings.'''
@app.route("/api/jobs")

def list_jobs():
  JOBS=load_data_from_db()
  return jsonify(JOBS)
    

@app.route("/job/<id>")

def show_job(id):
  job = load_job_fromDB(id)
  if not job:
    return "Not Found", 404
  return  render_template('jobpage.html', job=job)
#   #return jsonify(job)
@app.route("/job/<int:id>/apply", methods=['POST'])
def apply_to_job(id):
    data = request.form.to_dict()
    logging.debug(f"Received application data: {data}")
    job = load_job_fromDB(id)
    if not job:
        return "Job Not Found", 404
    try:
        push_application_data_to_db(id, data)
        logging.info(f"Application data for job {id} inserted successfully")
        return render_template('applicationSubmitted.html', applications=data, job=job)
    except Exception as e:
        logging.error(f"Error applying to job: {e}")
        return "An error occurred while processing your application", 500

  
'''if request.method == 'POST':
        try:
            data = request.form
            return jsonify(data)
        except Exception as e:
            return jsonify({'error': str(e)})
    else:
        return jsonify({'error': 'Only POST requests are allowed for this route'})'''

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)
