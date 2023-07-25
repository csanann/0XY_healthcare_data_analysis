# file: 0XY_healthcare_data_analysis/backend/tests/test_data_loading.py

import sys
import os
from pathlib import Path

current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(current_directory))

import pandas as pd
from data_loading import load_data
 
def test_load_data():
  print("Current working directory:", os.getcwd())
  print("Contents of the 'data' directory:", os.listdir('data'))
  
  if sys.platform.startswith("win"):
    data_file_path = Path('data/data-ori.csv')
  else:
    data_file_path = Path('data/data-ori.csv')
    
  df = load_data(data_file_path)
  assert isinstance(df, pd.DataFrame)
  assert df.shape[0] > 0
  assert df.shape[1] > 0