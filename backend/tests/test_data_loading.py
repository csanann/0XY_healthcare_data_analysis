# file: 0XY_healthcare_data_analysis/backend/tests/test_data_loading.py

import pandas as pd
from data_loading import load_data

def test_load_data():
  df = load_data('data-ori.csv')
  assert isinstance(df, pd.DataFrame)
  assert df.shape[0] > 0
  assert df.shape[1] > 0