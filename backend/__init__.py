# file: /0XY_healthcare_data_analysis/backend/__init__.py

from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from backend.mongodb_interaction import load_data, analyse, get_all_records, get_record_by_id
import os

# Connect to MongoDB
MONGODB_URI = 'mongodb://localhost:27017/'
client = MongoClient(MONGODB_URI)
db = client['health_records_db']

def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=['GET'])
    def home():
        return app.send_static_file('index.html')

    @app.route('/records', methods=['GET'])
    def records():
        records = get_all_records()
        return jsonify(records)

    @app.route('/record/<id>', methods=['GET'])
    def record(id):
        record = get_record_by_id(id)
        return jsonify(record)

    @app.route('/analyse', methods=['GET'])
    def analyse_endpoint():
        df = load_data('data/data-ori.csv')
        variable = request.args.get('variable')
        
        if variable not in ['HAEMATOCRIT', 'HAEMOGLOBINS', 'ERYTHROCYTE', 'LEUCOCYTE', 'THROMBOCYTE', 'MCH', 'MCHE', 'MCV', 'AGE', 'SEX', 'SOURCE']:
            return jsonify({'error': 'Invalid variable'}), 400
            
        df = analyse(df, variable)
        return df.to_json(orient='records')

    return app
