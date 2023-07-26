#file: backend/mongodb_interaction.py

from pymongo import MongoClient
import pandas as pd
from pymongo.collection import Collection

def load_data_to_db(data_filepath):
  client = MongoClient('mongodb://localhost:27017/')
  db = client['health_records_db']
  
  df = pd.read_csv(data_filepath)
  df.reset_index(inplace = True)
  df.rename(columns = {'index': 'patient_id'}, inplace = True)
  
  records = df.to_dict(orient = 'records')
  db.health_records.insert_many(records)
  print("Data loaded into MongoDB successfully!")
  
if __name__ == "__main__":
  load_data_to_db("data/data-ori.csv")
