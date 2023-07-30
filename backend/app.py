# file: /0XY_healthcare_data_analysis/backend/app.py

from flask import Flask, jsonify, request
from flask_cors import CORS
from mongodb_interaction import get_all_records, get_record_by_id

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Welcome to the Heathcare Data Analysis API!"

@app.route('/records', methods = ['GET'])
def records():
    records = get_all_records()
    return jsonify(records)
  
@app.route('/record/<id>', methods = ['GET'])  
def record(id):
    record = get_record_by_id(id)
    # return f"This endpoint will return record {id}."
    return jsonify(record)
    
@app.route('/analyse', methods = ['GET'])
def analyse():
    # df = load_data('data/data-ori.csv')
    # histogram_data = get_age_histogram_data(df)
    # return jsonify(histogram_data)
    return " This endpoint will return the analysis result."
    
if __name__=='__main__':
    app.run(host = '0.0.0.0', debug = True)
