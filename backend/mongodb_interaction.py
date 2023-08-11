#file: backend/mongodb_interaction.py

from pymongo import MongoClient
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

MONGODB_URI = 'mongodb://locahost:27017/'
client = MongoClient(MONGODB_URI)
db = client['heath_records_db']


def load_data_to_db(data_filepath):
  df = pd.read_csv(data_filepath)
  df.reset_index(inplace = True)
  df.rename(columns = {'index': 'patient_id'}, inplace = True)
  
  records = df.to_dict(orient = 'records')
  db.health_records.insert_many(records)
  print("Data loaded into MongoDB successfully!")
  
def get_all_records():
  records = db.health_records.find()
  return records
  
def get_record_by_id(id):
  record = db.health_records.find_one({'patient_id': id})
  return record
  
if __name__ == "__main__":
  load_data_to_db("data/data-ori.csv")
