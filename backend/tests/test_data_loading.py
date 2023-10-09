# file: 0XY_healthcare_data_analysis/backend/tests/test_data_loading.py

import sys
sys.path.insert(0, '/home/runner/work/0XY_healthcare_data_analysis')

import pandas as pd
from backend.data_loading import load_data

def test_load_data():
    data_file_path = '/data/data-ori.csv'
    df = load_data(data_file_path)
    
    assert isinstance(df, pd.DataFrame)
    
    assert df.shape[0] > 0
    assert df.shape[1] > 0
    
    expect_cols = ['HAEMATOCRIT', 'HAEMOGLOBINS', 'ERYTHROCYTE', 'LEUCOCYTE']
    assert set(expect_cols).issubset(set(df.columns))
    assert df.loc[0, 'HAEMATOCRIT'] == 321
    assert df.loc[100, 'ERYTHROCYTE'] == 4.41
    assert df.isnull().sum().sum() == 0