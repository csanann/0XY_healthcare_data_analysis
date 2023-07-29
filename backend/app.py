# file: /0XY_healthcare_data_analysis/backend/app.py

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# import data analysis and MongoDB connection
# from .data_loading import load_data
#from .data_analysis import analyse_data
#from .database import get_all_records, get_record_by_id

@app.route('/')
def home():
   # records = get_all_records()
    # return jsonify(records)
    return "Welcome to the Heathcare Data Analysis API!"

@app.route('/records', methods = ['GET'])
def records():
   
    return "This endpoint will return all records."
  
@app.route('/record/<id>', methods = ['GET'])  
def record(id):
    #record = get_record_by_id(id)
    # return jsonify(record)
    return f"This endpoint will return record {id}."
    
@app.route('/analyse', methods = ['GET'])
def analyse():
    
    return "This endpoint will return analysis results."
    
if __name__=='__main__':
    app.run(host = '0.0.0.0', debug = True)
