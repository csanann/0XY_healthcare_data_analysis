# file: /0XY_healthcare_data_analysis/backend/app.py

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from mongodb_interaction import get_all_records, get_record_by_id
from eda import load_data, analyse
import os

app = Flask(__name__, static_folder='../static')
CORS(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


@app.route('/records', methods = ['GET'])
def records():
    records = get_all_records()
    return jsonify(records)
  
@app.route('/record/<id>', methods = ['GET'])  
def record(id):
    record = get_record_by_id(id)
    return jsonify(record)
    
@app.route('/analyse', methods = ['GET'])
def analyse_endpoint():
    df = load_data('data/data-ori.csv')
    
    variable = request.args.get('variable')
    
    if variable not in [ 'HAEMATOCRIT', 'HAEMOGLOBINS', 'ERYTHROCYTE', 'LEUCOCYTE', 'THROMBOCYTE', 'MCH', 'MCHE', 'MCV', 'AGE', 'SEX', 'SOURCE']:
        return jsonify({'error': 'Invalid variable'}), 400
        
    df = analyse(df, variable)
    return df.to_json(orient = 'records')