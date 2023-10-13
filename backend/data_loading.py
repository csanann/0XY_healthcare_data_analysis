import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(file_buffer):
    df = pd.read_csv(file_buffer)
  
    # Split data into typical train/val/test
    df_train, df_test = train_test_split(df, test_size=0.2, random_state=42)
    df_val, df_test = train_test_split(df_test, test_size=0.5, random_state=42)
  
    return df_train, df_val, df_test
