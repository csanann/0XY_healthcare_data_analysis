#file: 0XY_healthcare_data_analysis/backend/data_loading.py

import pandas as pd

def load_data(filepath):
  df = pd.read_csv(filepath)
  return df