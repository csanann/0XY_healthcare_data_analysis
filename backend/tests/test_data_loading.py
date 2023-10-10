# file: 0XY_healthcare_data_analysis/backend/tests/test_data_loading.py

import sys
import pandas as pd
from backend.data_loading import load_data
import os

def test_load_data():
    data_file_path = os.path.join(os.path.dirname(__file__), '../data/data-ori.csv')
    with open(data_file_path, 'r') as f:
        df_train, df_val, df_test = load_data(f)
    
    #check bug
    print("Train DataFrame:")
    print(df_train.head())
    print("Validation DataFrame:")
    print(df_val.head())
    print("Test DataFrame:")
    print(df_test.head())
    
    assert isinstance(df_train, pd.DataFrame)
    assert isinstance(df_val, pd.DataFrame)
    assert isinstance(df_test, pd.DataFrame)
    
    assert df_train.shape[0] > 0
    assert df_val.shape[0] > 0
    assert df_test.shape[0] > 0
    
    expect_cols = ['HAEMATOCRIT', 'HAEMOGLOBINS', 'ERYTHROCYTE', 'LEUCOCYTE']
    assert set(expect_cols).issubset(set(df_train.columns))

    assert df_train.isnull().sum().sum() == 0
    assert df_val.isnull().sum().sum() == 0
    assert df_test.isnull().sum().sum() == 0