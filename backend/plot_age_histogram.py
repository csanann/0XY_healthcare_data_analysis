# file: 0XY_healthcare_data_analysis/backend/plot_age_histogram.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data-ori.csv')

def plot_age_histogram(df):

  plt.figure(figsize=(8, 6))
  plt.hist(df['AGE'], bins=20, color='skyblue', edgecolor='black')
  plt.xlabel('Age')
  plt.ylabel('Frequency')
  plt.title('Age Distribution')
  plt.grid(True)
  plt.savefig('age_histogram.png')
  plt.show()
