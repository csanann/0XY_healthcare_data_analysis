#file: 0XY_healthcare_data_analysis/backend/data_loading.py

import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(file_buffer):
  df = pd.read_csv(file_buffer)
  
  #check bug
  if len(df) <= 1:
    raise ValueError("Need more than 1 sample to split data.")
  
  #split data into typical train/val/test
  df_train, df_test = train_test_split(df, test_size=0.2, random_state=42)
  df_val, df_test = train_test_split(df_test, test_size=0.5, random_state=42)
  
  X_train, y_train = df_train.drop(columns=['target']), df_train['target']
  X_val, y_val = df_val.drop(columns=['target']), df_val['target']
  
  return X_train, X_val, y_train, y_val
  