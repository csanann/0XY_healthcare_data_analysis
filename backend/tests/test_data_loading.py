import pandas as pd
from backend.data_loading import load_data
import os

def test_load_data():
    data_file_path = os.path.join(os.path.dirname(__file__), '../data/data-ori.csv')
    with open(data_file_path, 'r') as f:
        df_train, df_val, df_test = load_data(f)
    
    # Check dataframes
    assert isinstance(df_train, pd.DataFrame)
    assert isinstance(df_val, pd.DataFrame)
    assert isinstance(df_test, pd.DataFrame)
    
    assert df_train.shape[0] > 0
    assert df_val.shape[0] > 0
    assert df_test.shape[0] > 0

    # Check that the specific columns don't exist
    unexpected_cols = ['HAEMATOCRIT', 'HAEMOGLOBINS', 'ERYTHROCYTE', 'LEUCOCYTE']
    assert not any(col in df_train.columns for col in unexpected_cols)
    assert not any(col in df_val.columns for col in unexpected_cols)
    assert not any(col in df_test.columns for col in unexpected_cols

    assert df_train.isnull().sum().sum() == 0
    assert df_val.isnull().sum().sum() == 0
    assert df_test.isnull().sum().sum() == 0
