# file: /0XY_healthcare_data_analysis/backend/app.py

from flask import Flask, jsonify, request
from flask_cors import CORS
from mongodb_interaction import get_all_records, get_record_by_id
from eda import load_data, analyse

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
def analyse_endpoint():
    df = load_data('data/data-ori.csv')
    
    variable = request.args.get('variable')
    # plot_type = request.args.get('plot_type')
    
    if variable not in [ 'HAEMATOCRIT', 'HAEMOGLOBINS', 'CRYTHROCYTE', 'LEUCOCYTE', 'THROMBOCYTE', 'MCH', 'MCHE', 'MCV', 'AGE', 'SEX', 'SOURCE']:
        return jsonify({'error': 'Invalid variable'}), 400
        
    # if plot_type not in ['histogram', 'boxplot', 'violin', 'correlation']:
    #     return jsonify({ 'error': 'Invalie plot type'}), 400
        
    # plot = eda.analyse(variable)
    df = analyse(df, variable)
    return df.to_json(orient = 'records')
        
    # return send_file(plot, minetype = 'image/png')

    
    
if __name__=='__main__':
    app.run(host = '0.0.0.0', debug = True)
